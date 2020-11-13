# -*- coding: utf-8 -*-
"""
Parses the DSRC assessment `.md` file and generates:
1) a structured `.json` file, meant to be directly uploaded in the web platform
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


class Assessment:
    def __init__(self):

        # Misc.
        self.directory = os.path.dirname(sys.argv[0])

        # Initialize basic descriptors
        self.filename = None
        self.name = None
        self.version = None
        self.get_infos_from_user()

        # Initialize dictionary to store results from parsing the raw assessment
        self.dict = {}
        self.dictionarize_raw_assessment()

    def get_infos_from_user(self):

        # Ask user for the filename of the raw assessment to process, the version number, the assessment name
        print("Please, enter the filename for the raw assessment you wish to process:")
        self.filename = input()
        print("Please, enter the version of the assessment, (like '0.6'): ")
        self.version = input()
        print("Please, enter the name of the assessment: ")
        self.name = input()

    def dictionarize_raw_assessment(self):

        self.dict["version"] = self.version
        self.dict["name"] = self.name
        now = datetime.now()
        self.dict["timestamp"] = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        self.dict["sections"] = {}

        # Open and read the text file
        # (from the current directory, where the assessment and the script should be both present)
        filepath = self.directory + glob.glob("raw_files/" + self.filename)[0]
        if not os.path.isfile(filepath):
            print("File path {} does not exist. Exiting...".format(filepath))
            sys.exit()
        with open(filepath, "r", encoding="utf-8") as fp:
            raw = fp.read()

            # Capture all sections of the assessment
            match_each_sections = re.findall(
                r"[\#]{3,}\s[Section]+\s(?P<section_id>[0-9]+)[\-\s]+(?P<title>.+)\n\n(?P<description>(.|\n)+?)\n\n\[", raw)
            # print(match_each_sections)  # DEBUG

            for section_data in match_each_sections:
                self.dict["sections"]["section " + section_data[0]] = {
                    "order_id": section_data[0],
                    "name": section_data[1],
                    "description": section_data[2],
                    "elements": {}
                }

            # Capture all assessment elements
            match_each_element = re.findall(r"(Q[0-9.]{3}(.|\n)+?---\n)", raw)
            # print(match_each_element)  # DEBUG

            for el in match_each_element:

                # Capture each component of the element
                match_id = re.search(r"Q(?P<section_id>[0-9])\.(?P<evaluation_item_id>[0-9])\s:", el[0])
                match_title = re.search(r"Q[0-9.]{3,5}\s:\s\*\*(?P<title>.+)\*\*", el[0])
                match_condition = re.search(r"_\(Condition\s:\sR[0-9.]{3,5}\s\<\>\s(?P<item_id>[0-9a-z.]{5,8})\)_", el[0])
                match_question_text = re.search(r"(?P<question_text>.*(\s:|\s\?|\.))\n\nR[0-9.]{3}", el[0])
                match_answer_type = re.search(r"_\((?P<answer_type>Type.+)\)_", el[0])
                match_answer_hint = re.search(r"_\((?P<answer_hint>.+)\)_\n\n-\s\[", el[0])  # Not used
                match_answer_items = re.findall(
                    r"-\s\[\s]\s(?P<answer_item_id>\d{1,2}.\d{1,2}.\D)\s(?P<answer_item_text>[^\|\n]+)(\s\|\s_\((?P<answer_item_type>.+)\)_)?\n", el[0])
                match_explanation = re.search(r"(Expl[0-9.]+)\s:<\/summary>\n\n(?P<expl>(.|\n)+?)\n\n<", el[0])
                match_resources = re.search(r"(Ressources[0-9.]+)\s:<\/summary>\n\n(?P<resource>(.|\n)+?)<", el[0])
                match_resource_items = []
                if match_resources:
                    match_resource_items = re.findall(r"-\s\((?P<type>.+?)\)\s(?P<text>.+)\n", match_resources.group('resource'))

                # elem_id = match_id.group('section_id') + "." + match_id.group('evaluation_item_id')  # DEBUG
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

                self.dict["sections"][section]["elements"][evaluation_item] = {
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
                    self.dict["sections"][section]["elements"][evaluation_item]['resources'][i] = {
                        'resource_type': item[0],
                        'resource_text': item[1],
                    }

                for item in match_answer_items:
                    is_concerned_switch = 1 if item[3] else 0
                    self.dict["sections"][section]["elements"][evaluation_item]['answer_items'][item[0]] = {
                        'order_id': item[0][-1],
                        'answer_text': item[1],
                        'is_concerned_switch': is_concerned_switch,  # Boolean, responsible for the intra element conditions
                    }

    def dump_to_json_file(self):
        """Generate the .json file of the assessment"""

        json_filename = f'processed_files/assessment-{self.dict["version"]}.json'
        with open(json_filename, 'w', encoding="utf-8") as fp:
            json.dump(self.dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)

    def create_scoring_template(self):
        """Create a neat, easy-to-read and easy-to-write-in scoring template"""

        # Initialize key elements
        txt_lines = []
        sections_dict = self.dict["sections"]
        nb_sections = len(sections_dict)

        txt_lines.append(f'Assessment version : [{self.version}]\n')
        txt_lines.append("Scoring version : [1]\n")
        txt_lines.append("\n")

        # Open upgrade table for the new assessment, and ask user for which old version to check
        print(f"Now opening the upgrade table for your new assessment (version {self.version})")
        upgrade_table_filename = f'assessment-{self.version}_upgrade_table.json'
        upgrade_table_filepath = self.directory + glob.glob("processed_files/" + upgrade_table_filename)[0]
        if not os.path.isfile(upgrade_table_filepath):
            print(f"Upgrade table filepath {upgrade_table_filepath} does not exist. Exiting...")
            sys.exit()
        print("Enter the assessment old version number to look for in the upgrade table "
              "(old scoring config will be fetched for answer items set to 1):")
        prev_scores_assessment_version = input()

        # Ask user for which old version of scoring to fetch scoring config from in order to pre-fill the template
        print("Enter the filename of the previous scoring file to be used to pre-fill the scoring template for this "
              "new assessment version "
              "(note: it is assumed it is located in /processed_files relatively to your working directory):")
        prev_scores_filename = input()
        prev_scores_filepath = self.directory + glob.glob("processed_files/" + prev_scores_filename)[0]
        if not os.path.isfile(prev_scores_filepath):
            print(f"Previous scores filepath {prev_scores_filepath} does not exist. Exiting...")
            sys.exit()

        # Indicate those infos in the scoring template for the new assessment
        txt_lines.append(f"Pre-filled score values are fetched from {prev_scores_filename}\n")
        txt_lines.append(f"(only for answer items set to 1 in {upgrade_table_filename} vs. version {prev_scores_assessment_version})\n")
        txt_lines.append(f"(answer items not set to 1 are pre-filled with '....' so you can identify them quickly)\n")
        txt_lines.append("\n")

        with open(prev_scores_filepath, "r", encoding="utf-8") as prev_scoring_file, \
                open(upgrade_table_filepath, "r", encoding="utf-8") as upgrade_table_file:
            prev_scores = json.load(prev_scoring_file)
            upgrade_table = json.load(upgrade_table_file)

            # Start filling in the template by looping over sections
            for i in range(1, nb_sections+1):
                section_idx = "section " + str(i)
                txt_lines.append(f'# {section_idx} - {sections_dict[section_idx]["name"]}\n')
                txt_lines.append("\n")

                # Within a given section, loop over elements
                elements_dict = sections_dict[section_idx]["elements"]
                nb_elements = len(elements_dict)
                for j in range(1, nb_elements+1):
                    element_idx = "element " + str(j)
                    txt_lines.append(f'## Q{i}.{j} - {elements_dict[element_idx]["name"]}\n')

                    # Within a given element, loop over answer items
                    items_dict = elements_dict[element_idx]["answer_items"]
                    for k, v in items_dict.items():
                        # Fetch score value of previous version to facilitate completion
                        pre_fill = '....'
                        if upgrade_table["diff_per_version"][prev_scores_assessment_version]["answer_items"][k] == 1:
                            pre_fill = prev_scores[k]
                        if v["is_concerned_switch"] == 1:
                            pre_fill = '-nc-'
                        txt_lines.append(f'{pre_fill} [{k}] {v["answer_text"]}\n')

                    txt_lines.append("\n")

                txt_lines.append("\n")

        # Create the scoring template text file
        template_filename = f"raw_files/scoring_template-{self.version}.txt"
        with open(template_filename, 'w', encoding="utf-8") as f:
            f.writelines(txt_lines)


def main():

    new_assessment = Assessment()

    # Create the .json file of the assessment
    new_assessment.dump_to_json_file()

    # Create the scoring template, pre-filled with scoring config from a previous version
    new_assessment.create_scoring_template()


if __name__ == '__main__':
    main()
