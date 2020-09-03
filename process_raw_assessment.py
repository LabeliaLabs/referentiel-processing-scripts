# -*- coding: utf-8 -*-
"""
Parses the DSRC assessment .md file and generates:
1) a structured .json file, meant to be directly uploaded in the web platform
2) a neat template for easily adding score points per answer item
"""

import sys
import os
import re
import json
import glob
from datetime import datetime


def match_question_type(regex_string):
    """Link the description of the question type to a type of question in the database : radio or checkbox"""
    if "unique" in regex_string:
        return "radio"
    else:
        return "checkbox"


def main():

    # Initialize a dictionary
    dict = {}

    # Open and read the text file
    # Current directory, where the assessment and the script should be both present
    directory = os.path.dirname(sys.argv[0])
    filepath = directory + glob.glob("assessment.md")[0]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, "r", encoding="utf-8") as fp:
        raw = fp.read()

        # Capture all sections of the assessment
        match_each_sections = re.findall(r'[\#]{3,}\s[Section]+\s(?P<section_id>[0-9]+)[\-\s]+(?P<title>.+)\n\n(?P<description>(.|\n)+?)\n\n\[', raw)
        # print(match_each_sections)  # DEBUG

        # Initialize the dict (version and sections dict)
        print("Please, enter the version of the assessment, (like '1.4'): ")
        version = input()
        dict["version"] = version
        print("Please, enter the name of the assessment: ")
        name = input()
        dict["name"] = name
        now = datetime.now()
        dict["timestamp"] = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        dict["sections"] = {}

        for section_data in match_each_sections:
            dict["sections"]["section " + section_data[0]] = {
                "order_id": section_data[0],
                "name": section_data[1],
                "description": section_data[2],
                "elements": {}
            }

        # Capture all assessment elements
        match_each_element = re.findall(r'(Q[0-9.]{3}(.|\n)+?---\n)', raw)
        # print(match_each_element)  # DEBUG

        for el in match_each_element:

            # Capture each component of the element

            match_id = re.search(r'Q(?P<section_id>[0-9])\.(?P<evaluation_item_id>[0-9])\s:', el[0])
            match_title = re.search(r'Q[0-9.]{3,5}\s:\s\*\*(?P<title>.+)\*\*', el[0])
            match_condition = re.search(r'_\(Condition\s:\sR[0-9.]{3,5}\s\<\>\s(?P<item_id>[0-9a-z.]{5,8})\)_', el[0])
            match_question_text = re.search(r'(?P<question_text>.*(\s:|\s\?|\.))\n\nR[0-9.]{3}', el[0])
            match_answer_type = re.search(r'_\((?P<answer_type>Type.+)\)_', el[0])
            match_answer_hint = re.search(r'_\((?P<answer_hint>.+)\)_\n\n-\s\[', el[0])  # Not used

            # Group answer_item_id is section_id.element_id.choice_id (5.2.b)
            match_answer_items = re.findall(r'-\s\[\s]\s(?P<answer_item_id>\d{1,2}.\d{1,2}.\D)\s(?P<answer_item_text>[^\|\n]+)(\s\|\s_\((?P<answer_item_type>.+)\)_)?\n', el[0])

            match_explanation = re.search(r'(Expl[0-9.]+)\s:<\/summary>\n\n(?P<expl>(.|\n)+?)\n\n<', el[0])
            match_resources = re.search(r'(Ressources[0-9.]+)\s:<\/summary>\n\n(?P<resource>(.|\n)+?)<', el[0])

            match_resource_items = []
            if match_resources:
                match_resource_items = re.findall(r'-\s\((?P<type>.+?)\)\s(?P<text>.+)\n', match_resources.group('resource'))

            # elem_id = match_id.group('section_id') + "." + match_id.group('evaluation_item_id')
            # print(elem_id, 'n/a' if not match_title else match_title.group('title'))  # DEBUG
            # print(elem_id, 'n/a' if not match_condition else match_condition.group('item_id'))  # DEBUG
            # print(elem_id, 'n/a' if not match_question_text else match_question_text.group('question_text'))  # DEBUG
            # print(elem_id, 'n/a' if not match_answer_type else match_answer_type.group('answer_type'))  # DEBUG
            # print(elem_id, 'n/a' if not match_answer_hint else match_answer_hint.group('answer_hint'))  # DEBUG
            # print(elem_id, 'n/a' if not match_answer_items else match_answer_items)  # DEBUG
            # print(elem_id, 'n/a' if not match_explanation else match_explanation.group('expl'))  # DEBUG
            # print(elem_id, 'n/a' if not match_resources else match_resources.group('resource'))  # DEBUG

            # Populate the dictionary in the corresponding section
            # Calculate the value to add
            section = "section " + match_id.group('section_id')
            evaluation_item = "element " + match_id.group('evaluation_item_id')

            dict["sections"][section]["elements"][evaluation_item] = {
                'order_id': 'n/a' if not match_id else match_id.group('evaluation_item_id'),
                'name': 'n/a' if not match_title else match_title.group('title'),
                'condition': 'n/a' if not match_condition else match_condition.group('item_id'),
                'question_text': 'n/a' if not match_question_text else match_question_text.group('question_text'),
                'question_type': 'n/a' if not match_answer_type else match_question_type(match_answer_type.group('answer_type')),
                'answer_hint': 'n/a' if not match_answer_hint else match_answer_hint.group('answer_hint'),
                'explanation_text': 'n/a' if not match_explanation else match_explanation.group('expl'),
                'resources': {},
                'answer_items': {},
            }

            for i, item in enumerate(match_resource_items):
                dict["sections"][section]["elements"][evaluation_item]['resources'][i] = {
                    'resource_type': item[0],
                    'resource_text': item[1],
                }

            depends_on = ""
            for item in match_answer_items:
                is_concerned_switch = 1 if item[3] else 0
                dict["sections"][section]["elements"][evaluation_item]['answer_items'][item[0]] = {
                    'order_id': item[0][-1],
                    'answer_text': item[1],
                    'is_concerned_switch': is_concerned_switch,
                    'depends_on': depends_on,
                }
                # If this answer item sets conditions on the others, so we change depends_on value to its order_id
                if is_concerned_switch:
                    depends_on = item[0][-1]

    # Generate the .json file of the assessment
    json_filename = f'assessment-{dict["version"]}.json'
    with open(json_filename, 'w', encoding="utf-8") as fp:
        json.dump(dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)

    # Create a neat, easy-to-read and easy-to-write-in scoring template

    txt_lines = []
    sections_dict = dict["sections"]
    nb_sections = len(sections_dict)

    txt_lines.append(f'Assessment version : [{dict["version"]}]\n')
    txt_lines.append("Scoring version : [1.0]\n")
    txt_lines.append("\n")

    for i in range(1, nb_sections+1):

        section_idx = "section " + str(i)

        txt_lines.append(f'# {section_idx} - {sections_dict[section_idx]["name"]}\n')
        txt_lines.append("\n")

        elements_dict = sections_dict[section_idx]["elements"]
        nb_elements = len(elements_dict)

        for j in range(1, nb_elements+1):

            element_idx = "element " + str(j)

            txt_lines.append(f'## Q{i}.{j} - {elements_dict[element_idx]["name"]}\n')

            items_dict = elements_dict[element_idx]["answer_items"]
            for k, v in items_dict.items():
                txt_lines.append(f'0.00 [{k}] {v["answer_text"]}\n')

            txt_lines.append("\n")

        txt_lines.append("\n")

    template_filename = "scoring_template.txt"
    with open(template_filename, 'w', encoding="utf-8") as f:
        f.writelines(txt_lines)


if __name__ == '__main__':
    main()
