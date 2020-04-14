# -*- coding: utf-8 -*-
"""
Parses the DSRC assessment .md file and generates a json file.
"""

import sys
import os
import re
import json

import pandas as pd


def main():
    # Initialize a dictionary
    dict = {}

    # Open and read the text file

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, "r", encoding="utf-8") as fp:
        raw = fp.read()

        # Capture all assessment elements
        match_each_element = re.findall(r'(Q[0-9.]{3}(.|\n)+?---\n)', raw)
        # print(match_each_item[11]) # DEBUG

        for el in match_each_element:

            # Capture each component of the element
            match_id = re.search(r'Q(?P<id>[0-9.]{3})\s:', el[0])
            match_title = re.search(r'Q[0-9.]{3}\s:\s\*\*(?P<title>.+)\*\*', el[0])
            match_condition = re.search(r'_\((?P<condition>Condition.+?)\)_', el[0])
            match_question_text = re.search(r'(?P<question_text>.*(\s:|\s\?|\.))\n\nR[0-9.]{3}', el[0])
            match_answer_type = re.search(r'_\((?P<answer_type>Type.+)\)_', el[0])
            match_answer_hint = re.search(r'_\((?P<answer_hint>.+)\)_\n\n-\s\[', el[0])
            match_answer_items = re.findall(r'-\s\[\s]\s(?P<answer_item_id>\d.\d.\D)\s(?P<answer_item_text>[^\|\n]+)(\s\|\s_\((?P<answer_item_type>.+)\)_)?\n', el[0])
            match_expl = re.search(r'summary>\n\n(?P<expl>(.|\n)+?)\n\n</details', el[0])

            # print(match_id.group('id'), 'n/a' if not match_title else match_title.group('title')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_condition else match_condition.group('condition')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_question_text else match_question_text.group('question_text')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_answer_type else match_answer_type.group('answer_type')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_answer_hint else match_answer_hint.group('answer_hint')) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_answer_items else match_answer_items) # DEBUG
            # print(match_id.group('id'), 'n/a' if not match_expl else match_expl.group('expl')) # DEBUG

            # Populate the dictionary
            dict['element' + match_id.group('id')] = {
                'section': match_id.group('id')[0],
                'id': match_id.group('id'),
                'title': 'n/a' if not match_title else match_title.group('title'),
                'condition': 'n/a' if not match_condition else match_condition.group('condition'),
                'question_text': match_question_text.group('question_text'),
                'answer_type': 'n/a' if not match_answer_type else match_answer_type.group('answer_type'),
                'answer_hint': match_answer_hint.group('answer_hint'),
                'answer_items': {},
                'expl': 'n/a' if not match_expl else match_expl.group('expl'),
            }

            for item in match_answer_items:
                dict['element' + match_id.group('id')]['answer_items'][item[0]] = {
                    'item_text': item[1],
                    'item_type': item[3],
                }

    # Print a table view of the dictionary (for debug purposes)
    mylist = []
    for key in dict.keys():
        mylist.append(
            [dict[key]['id'],
             dict[key]['title'],
             dict[key]['condition'],
             dict[key]['question_text'],
             dict[key]['answer_type'],
             dict[key]['answer_hint'],
             dict[key]['expl'],
             ])
    mydf = pd.DataFrame(mylist, columns=['id', 'title', 'condition', 'question_text', 'answer_type', 'answer_hint', 'expl'])
    pd.set_option('max_columns', 10)
    pd.set_option('max_colwidth', 10)
    # print(mydf) # DEBUG

    # Generate the .json file
    with open('assessment.json', 'w', encoding="utf-8") as fp:
        json.dump(dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)

if __name__ == '__main__':
    main()
