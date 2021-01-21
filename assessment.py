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
from datetime import datetime
from pathlib import Path


def match_question_type(regex_string):
    """Link the description of the question type to a type of question in the database : radio or checkbox"""
    if "unique" in regex_string:
        return "radio"
    else:
        return "checkbox"


class Assessment:
    def __init__(
            self,
            filename=None,
            version=None,
            name=None,
            language=None,
            prev_scores_assessment_version=None,
            prev_scores_filename=None,
    ):

        # Misc.
        self.directory = os.path.dirname(sys.argv[0])

        # Initialize basic descriptors
        self.filename = filename
        self.raw_assessment_filepath = f"input_files/{self.filename}"
        if not os.path.isfile(self.raw_assessment_filepath):
            print(f"File path {self.raw_assessment_filepath} does not exist. Exiting...")
            sys.exit()
        self.version = version
        self.name = name
        self.language = language

        # Initialize upgrade table related infos
        self.upgrade_table_filename = f"assessment-{self.version}_upgrade_table.json"
        self.upgrade_table_filepath = Path.cwd() / "input_files" / self.upgrade_table_filename
        if not os.path.isfile(self.upgrade_table_filepath):
            print(f"Upgrade table filepath {self.upgrade_table_filepath} does not exist. Exiting...")
            sys.exit()

        # Initialize old scoring related infos
        self.prev_scores_assessment_version = prev_scores_assessment_version
        self.prev_scores_filename = prev_scores_filename
        self.prev_scores_filepath = Path.cwd() / "processed_files" / self.prev_scores_filename
        if not os.path.isfile(self.prev_scores_filepath):
            print(f"Previous scores filepath {self.prev_scores_filepath} does not exist. Exiting...")
            sys.exit()

        # Initialize dictionary to store results from parsing the raw assessment
        self.dict = {}
        self.dictionarize_raw_assessment()

        # Attributes related to processing
        self.assessment_json_version_filename = f"assessment-{self.version}-{self.language}.json"
        self.assessment_json_version_filepath = f"processed_files/{self.assessment_json_version_filename}"
        self.scoring_template_filename = f"scoring_template-{self.version}.txt"
        self.scoring_template_filepath = f"intermediary_files/{self.scoring_template_filename}"
        self.scoring_version = None
        self.scoring_json_version_filename = None
        self.scoring_json_version_filepath = None

    def dictionarize_raw_assessment(self):

        self.dict["version"] = self.version
        self.dict["name"] = self.name
        self.dict["language"] = self.language
        now = datetime.now()
        self.dict["timestamp"] = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        self.dict["sections"] = {}

        with open(self.raw_assessment_filepath, "r", encoding="utf-8") as fp:
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
                match_resources = re.search(r"(Ress?ources[0-9.]+)\s:<\/summary>\n\n(?P<resource>(.|\n)+?)<", el[0])
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

        with open(self.assessment_json_version_filepath, 'w', encoding="utf-8") as fp:
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

        # Indicate old scores infos in the scoring template for the new assessment
        txt_lines.append(f"Pre-filled score values are fetched from {self.prev_scores_filename}\n")
        txt_lines.append(f"(only for answer items set to 1 in {self.upgrade_table_filename} vs. version"
                         f" {self.prev_scores_assessment_version})\n")
        txt_lines.append(f"(answer items not set to 1 are pre-filled with '....' so you can identify them quickly)\n")
        txt_lines.append("\n")

        print(f"Now opening the upgrade table for your new assessment (version {self.version})")
        with open(self.prev_scores_filepath, "r", encoding="utf-8") as prev_scoring_file, \
                open(self.upgrade_table_filepath, "r", encoding="utf-8") as upgrade_table_file:
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
                        if upgrade_table["diff_per_version"][self.prev_scores_assessment_version]["answer_items"][k] \
                                == 1:
                            pre_fill = prev_scores[k]
                        if v["is_concerned_switch"] == 1:
                            pre_fill = '-nc-'
                        txt_lines.append(f'{pre_fill} [{k}] {v["answer_text"]}\n')

                    txt_lines.append("\n")

                txt_lines.append("\n")

        # Create the scoring template text file
        with open(self.scoring_template_filepath, 'w', encoding="utf-8") as f:
            f.writelines(txt_lines)

    def process_scoring_template_to_json(self):

        # Initialize a dictionary
        temp_dict = {}

        # Check if there is indeed the scoring template with the standardized name, in the /intermediary_files folder
        if not os.path.isfile(self.scoring_template_filepath):
            print(f"File path {self.scoring_template_filepath} does not exist. Exiting...")
            sys.exit()

        with open(self.scoring_template_filepath, "r", encoding="utf-8") as fp:
            raw = fp.read()

            # Capture and fill the version numbers the user has filled in
            assessment_version = re.search(r"Assessment\sversion\s:\s\[(?P<version_nb>.+)\]", raw).group("version_nb")
            if assessment_version != self.version:
                raise Warning(f"Careful here! You are processing a scoring template indicating assessment version "
                              f"{assessment_version}, but you are currently operating with an Assessment instance "
                              f"which version is {self.version}")
            self.scoring_version = re.search(r"Scoring\sversion\s:\s\[(?P<version_nb>.+)\]", raw).group("version_nb")

            # Capture all answer items, their scoring config, and add items ids as keys and weights as values
            all_answer_items = re.findall(
                r"(?P<nb_points>\d{1,2}.?\d{0,2}|-nc-)\s\[(?P<item_id>\d{1,2}.\d{1,2}.\D)\]", raw)
            for item in all_answer_items:
                nb_points = 0 if item[0] == '-nc-' else item[0]
                temp_dict[item[1]] = str(nb_points)  # We need the values as string for the import in the platform

        # Generate the .json file of the assessment
        self.scoring_json_version_filename = f"assessment-{assessment_version}_scoring-{self.scoring_version}.json"
        self.scoring_json_version_filepath = f"processed_files/{self.scoring_json_version_filename}"
        with open(self.scoring_json_version_filepath, 'w', encoding="utf-8") as fp:
            json.dump(temp_dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)

    def enrich_assessment_with_scoring_recap(self):

        self.dict["enriched_with_scoring"] = {"scoring_version": self.scoring_version,
                                              "total_max_score": 0,
                                              "recap_per_section": {},
                                              }
        with open(self.scoring_json_version_filepath, 'r', encoding="utf-8") as scoring_file:

            scoring = json.load(scoring_file)

            for k, v in scoring.items():

                # First, delinearize the answer_item_id
                parse_k = re.search(r"(?P<s_id>\d{1,2}).(?P<e_id>\d{1,2}).(?P<a_id>\D)", k)
                section_id = parse_k.group("s_id")
                element_id = parse_k.group("e_id")

                # Second, convert the scoring value from string to float
                score_value = float(v)

                # Then we add it to the assessment (for the enriched version)
                self.dict["sections"]["section "+section_id]["elements"]["element "+element_id]["answer_items"][k][
                    "score_value"] = score_value

            # Now that we have the score values for each answer item, we'll compute the max score per element
            # There is a trick to compute this "max score" though: ...
            # ... for elements with multiple answers possible, it is the sum
            # ... but for elements with a unique answer, it is the max

            total_max_score = 0

            sections_dict = self.dict["sections"]
            nb_sections = len(sections_dict)
            for i in range(1, nb_sections+1):
                section_idx = "section " + str(i)
                section_max_score = 0

                elements_dict = sections_dict[section_idx]["elements"]
                nb_elements = len(elements_dict)
                for j in range(1, nb_elements+1):
                    element_idx = "element " + str(j)
                    element_max_score = 0
                    element_type = elements_dict[element_idx]["question_type"]

                    items_dict = elements_dict[element_idx]["answer_items"]
                    for k, v in items_dict.items():
                        if element_type == "checkbox":
                            element_max_score += v["score_value"]
                        elif element_type == "radio":
                            element_max_score = max(element_max_score, v["score_value"])

                    elements_dict[element_idx]["element_max_score"] = element_max_score
                    section_max_score += element_max_score

                sections_dict[section_idx]["section_max_score"] = section_max_score
                self.dict["enriched_with_scoring"]["recap_per_section"][section_idx] = section_max_score
                total_max_score += section_max_score

            self.dict["enriched_with_scoring"]["total_max_score"] = total_max_score

        with open(self.assessment_json_version_filepath, 'w', encoding="utf-8") as fp:
            json.dump(self.dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)

    def enrich_assessment_with_non_concerned_recap(self):

        temp_non_concerned = {}
        temp_conditional = {}

        # Loop over sections
        sections_dict = self.dict["sections"]
        nb_sections = len(sections_dict)
        for i in range(1, nb_sections + 1):
            section_idx = "section " + str(i)

            # Loop over elements
            elements_dict = sections_dict[section_idx]["elements"]
            nb_elements = len(elements_dict)
            for j in range(1, nb_elements + 1):
                element_idx = "element " + str(j)
                element_has_nc = False
                element_is_conditional = True if elements_dict[element_idx]["condition"] != "n/a" else False

                # Loop over answer items
                items_dict = elements_dict[element_idx]["answer_items"]
                for k, v in items_dict.items():
                    if v["is_concerned_switch"] == 1:
                        element_has_nc = True

                if element_has_nc:
                    temp_non_concerned[f"{i}.{j}"] = round(elements_dict[element_idx]["element_max_score"] / 2.0, 3)
                if element_is_conditional:
                    temp_conditional[f"{i}.{j}"] = round(elements_dict[element_idx]["element_max_score"] / 2.0, 3)

        self.dict["non_concerned_recap"] = {"non_concerned_in_element": temp_non_concerned,
                                            "conditional_elements": temp_conditional,
                                            }

        with open(self.assessment_json_version_filepath, 'w', encoding="utf-8") as fp:
            json.dump(self.dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)
