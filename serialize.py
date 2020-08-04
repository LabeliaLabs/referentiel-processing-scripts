# -*- coding: utf-8 -*-
"""
Parses the DSRC assessment .md file and generates a json file.
The json file resulting this script aims to be updated to the django platform whitout required modifications
"""

import sys
import os
import re
import json
import glob
import pandas as pd


def match_question_type(regex_string):
    """Link the description of the question type to a type of question in the database : radio or checkbox"""
    if "unique" in regex_string:
        return "radio"
    else:
        return "checkbox"


def treat_explanations(explanation):
    """
    Manage the explanation strings whether it contains external links or not
    :param explanation: string
    :return: string (explanation text) and dictionary (links
    """
    links = {}

    # group 2 is the link's name, group 3 is the url
    external_links = re.findall(r'\[(.*)\]\((http.*)\)', explanation) # Match with all the external links
    print("Explanation regex link", external_links)

    # For each link, we remove it to the text (the "http...") and add the link to the links dictionary
    # It will create an external_link in the platform
    for link in external_links:

        # Group 1 is all the explanation before the link, group 2 is the link's name, group 3 is the url
        # group 4 is expl after
        data_to_replace = re.findall(r'(.*)\[(.*)\]\((http.*)\)(.*\n?.*)', explanation)
        print("DATA REPLACE", data_to_replace)
        explanation = explanation.replace(data_to_replace[0][2], '') # Delete the link int the explanation
        links[link[0]] = {
            "name": link[0],
            "link": link[1],
            "type": "explication",
            "additional text": "",
        }
    return explanation, links


def treat_resources(resources):
    """
    Manage the resources strings whether it contains external links or not
    :param resources: string
    :return: string (resources text) and dictionary (links
    """
    links = {}
    # group 2 is the link's name, group 3 is the url
    # Match with the external links but do not work when there are several for one line so tricks
    external_links = re.findall(r'(.*)\[(?P<name>.*)\]\((?P<link>http.*)\)\*?(?P<addtional>.*)', resources)

    print("regex external links", external_links)
    for link in external_links:
        # Group 1 is useless text before the link (but need to check if not a link not caught within)
        # Group 2 is the link's name, group 3 is the url
        # Group 4 is explanation of the resource (author, etc)
        links[link[1]] = {
            "name": link[1],
            "link": link[2],
            "type": "ressource",
            "additional text": link[3],
        }

        # If the line has multiple links, we check the rests which is, with this regex, the 1st group
        rest = link[0]
        while "http" in rest:
            print("rest", rest)
            regex = re.findall(r'(.*)\[(.*)\]\((http.*)\)\*?(.*)', rest)

            links[regex[0][1]] = {
                "name": regex[0][1],
                "link": regex[0][2],
                "type": "ressource",
                "additional text": regex[0][3],
            }
            rest = regex[0]

    return links


def main():
    # Initialize a dictionary
    dict = {}

    # Open and read the text file
    # Current directory, where the assessment and the script should be both present
    directory = os.path.dirname(sys.argv[0])
    filepath = directory+"/"+glob.glob("assessment.md")[0]
    print("filepath", filepath)

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, "r", encoding="utf-8") as fp:
        raw = fp.read()

        # capture all the sections
        # Group 2 is to be sure it is a section, group 3 is the id, group 5 is the title, group 6 is the description
        # Which may contains \n
        # TODO can be improved to catch all until the double \n\n at the end of the description
        match_each_sections = re.findall(r'([\#]{3,})\s([Section]+)\s([0-9]+)([\-\s]+)(.+)\n+(.*\n?.*)', raw)
        print(match_each_sections)

        for section_data in match_each_sections:
            dict["section "+section_data[2]] = {
                "order_id": section_data[2],
                "name": section_data[4],
                "description": section_data[5],
                "elements": {}
            }

        # Capture all assessment elements
        match_each_element = re.findall(r'(Q[0-9.]{3}(.|\n)+?---\n)', raw)
        print(match_each_element) # DEBUG

        for el in match_each_element:

            # Capture each component of the element
            # Group 1 is the section id and group 2 is the question id
            match_id = re.findall(r'Q([0-9])\.([0-9])\s:', el[0])

            match_title = re.search(r'Q[0-9.]{3}\s:\s\*\*(?P<title>.+)\*\*', el[0])

            # TODO change in assessment.md how the conditions are written : <>1.5.a (is choice id)
            match_condition = re.search(r'_\((?P<condition>Condition.+?)\)_', el[0])

            # Group question_text (group 1) is the question_text
            match_question_text = re.search(r'(?P<question_text>.*(\s:|\s\?|\.))\n\nR[0-9.]{3}', el[0])

            # Group answer_type either "Type : réponse unique" or "Type : réponses multiples possibles"
            match_answer_type = re.search(r'_\((?P<answer_type>Type.+)\)_', el[0])

            match_answer_hint = re.search(r'_\((?P<answer_hint>.+)\)_\n\n-\s\[', el[0])  # Not used

            # Group answer_item_id is section_id.element_id.choice_id (5.2.b)
            # Group answer_item_type is for the conditions intra element (check is it always the case)
            match_answer_items = re.findall(r'-\s\[\s]\s(?P<answer_item_id>\d.\d.\D)\s(?P<answer_item_text>[^\|\n]+)(\s\|\s_\((?P<answer_item_type>.+)\)_)?\n', el[0])

            # Group explanation
            match_expl = re.search(r'(Expl[0-9.]+)\s:<\/summary>\n\n(?P<expl>(.|\n)+?)\n\n<', el[0])

            # Ressources group
            match_resource = re.search(r'(Ressources[0-9.]+)\s:<\/summary>\n\n(?P<resource>(.|\n)+?)\n\n<', el[0])

            # print(match_id.group('id'), 'n/a' if not match_title else match_title.group('title')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_condition else match_condition.group('condition')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_question_text else match_question_text.group('question_text')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_answer_type else match_answer_type.group('answer_type')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_answer_hint else match_answer_hint.group('answer_hint')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_answer_items else match_answer_items) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_expl else match_expl.group('expl')) # DEBUG

            # Populate the dictionary in the corresponding section
            # Calculate the value to add
            print("match ID", match_id)
            section = "section "+match_id[0][0]

            print("DIC", dict, section)

            dict[section]["elements"]['element' + match_id[0][1]] = {
                'order_id': match_id[0][1],
                'name': 'n/a' if not match_title else match_title.group('title'),
                'condition': 'n/a' if not match_condition else match_condition.group('condition'), # TODO
                'question_text': match_question_text.group('question_text'),
                'question_type': 'n/a' if not match_answer_type else match_question_type(match_answer_type.group('answer_type')),
                'answer_hint': match_answer_hint.group('answer_hint'),
                'answer_items': {},
                'explanation text': 'n/a' if not match_expl else treat_explanations(match_expl.group('expl'))[0],
                'explanation links': 'n/a' if not match_expl else treat_explanations(match_expl.group('expl'))[1],
                'resources': 'n/a' if not match_resource else treat_resources(match_resource.group('resource')),
            }

            depends_on = ""
            for item in match_answer_items:

                dict[section]["elements"]['element' +match_id[0][1]]['answer_items'][item[0]] = {
                    'order_id': item[0][-1],
                    'answer_text': item[1]+item[3],
                    'depends_on': depends_on,
                }
                # If this choice sets conditions on the others, so we change depends_on value to its order_id
                if item[3]:
                    depends_on = item[0][-1]


    # mylist = []
    # for key in dict.keys():
    #     mylist.append(
    #         [dict[key]['id'],
    #          dict[key]['title'],
    #          dict[key]['condition'],
    #          dict[key]['question_text'],
    #          dict[key]['answer_type'],
    #          dict[key]['answer_hint'],
    #          dict[key]['expl'],
    #          ])
    # mydf = pd.DataFrame(mylist, columns=['id', 'title', 'condition', 'question_text', 'answer_type', 'answer_hint', 'expl'])
    # pd.set_option('max_columns', 10)
    # pd.set_option('max_colwidth', 10)
    # print(mydf) # DEBUG

    # Generate the .json file
    with open('assessment.json', 'w', encoding="utf-8") as fp:
        json.dump(dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)

if __name__ == '__main__':
    main()
