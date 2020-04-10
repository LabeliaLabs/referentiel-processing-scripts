# -*- coding: utf-8 -*-
"""
Deserialize the DSRC assessment and generates a structured json.
"""

import sys
import os
import re


# import json
# import numpy as np
# import pandas as pd


def main():
    # Initialize a dictionnary
    dict = {}

    # Open and read the text file

    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, "r", encoding="utf-8") as fp:
        raw = fp.read()

        # Capture all assessment elements
        match = re.findall(r'Q(?P<id>[0-9.]{3})\s:\s(?P<title>.*)\s{1,2}\n(?P<content>(.|\n)*?)---', raw)
        # for i in range(11, 16): # DEBUG
            # print(match[i]) # DEBUG

        for el in match:
            dict['element' + el[0]] = {
                'section': el[0][0],
                'id': el[0],
                'title': el[1],
                'content': el[2],
            }
        # print(dict) # DEBUG

        for el in dict.values():

            # print(el['content']) # DEBUG

            # Capture an optional condition and the question text
            match_question = re.findall(r'(_\((?P<condition>Condition.+?)\)_\s\s\n)?(?P<question_text>.*(:|\?|\.))\n\nR[0-9.]{3}', el['content'])
            # print(el['id'], match_question)  # DEBUG
            el['condition'] = match_question[0][1]
            el['question_text'] = match_question[0][2]

            # Capture the answer type and the answer hint
            match_answer = re.findall(r'R[0-9.]{3}\s:\s\s\n_\((?P<answer_type>Type.+)\)_\s\s\n_\((?P<answer_hint>.+)\)_', el['content'])
            # print(el['id'], match_answer) # DEBUG
            el['answer_type'] = match_answer[0][0]
            el['answer_hint'] = match_answer[0][1]

            # Capture an optional explanation
            match_expl = re.findall(r'summary>\n\n(?P<expl>(.|\n)+)\n\n</details', el['content'])
            # print(el['id'], match_expl)  # DEBUG
            if not match_expl:
                el['expl'] = ''
            else:
                el['expl'] = match_expl[0][0]

            # Structure all answer content into separate structured items
            match_answer_items = re.findall(r'-\s\[\s]\s(?P<answer_item_id>\d.\d.\D)\s(?P<answer_item_text>[^\|\n]+)(?P<answer_item_type>\|.+)?\n', el['content'])
            print(el['id'], match_answer_items) # DEBUG
            el['answer_items'] = {}
            for item in match_answer_items:
                el['answer_items'][item[0]] = {
                    'item_text': item[1],
                    'item_type': item[2],
                }

        print(dict['element3.2']) # DEBUG

    # Generate the .json file


if __name__ == '__main__':
    main()
