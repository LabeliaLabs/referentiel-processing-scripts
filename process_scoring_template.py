# -*- coding: utf-8 -*-
"""
Parses the scoring template .txt file and generates a structured .json file,
meant to be directly uploaded in the web platform.
"""

import sys
import os
import re
import json
import glob
from datetime import datetime


def main():

    # Initialize a dictionary
    dict = {}

    # Ask user for the filename of the scoring template to process
    print("Please, enter the filename for the scoring template you wish to process:")
    filename = input()

    # Open and read the text file
    # Current directory, where the assessment and the script should be both present
    directory = os.path.dirname(sys.argv[0])
    filepath = directory + glob.glob("raw_files/" + filename)[0]

    if not os.path.isfile(filepath):
        print(f"File path {filepath} does not exist. Exiting...")
        sys.exit()

    with open(filepath, "r", encoding="utf-8") as fp:
        raw = fp.read()

        # Capture and fill the version numbers, used to name the json file
        assessment_version = re.search(r'Assessment\sversion\s:\s\[(?P<version_nb>.+)\]', raw)
        scoring_version = re.search(r'Scoring\sversion\s:\s\[(?P<version_nb>.+)\]', raw)
        assessment_version = assessment_version.group("version_nb")
        scoring_version = scoring_version.group("version_nb")

        # Add the current date into the json name file
        now = datetime.now()
        str_now = now.strftime("%Y%m%d%H%M%S")

        # Capture all answer items and their number of points and add the items ids as keys and the weights as values
        all_answer_items = re.findall(r'(?P<nb_points>\d{1,2}.?\d{0,2}|-nc-)\s\[(?P<item_id>\d{1,2}.\d{1,2}.\D)\]', raw)
        for item in all_answer_items:
            nb_points = 0 if item[0] == '-nc-' else item[0]
            dict[item[1]] = str(nb_points)  # We need the values as string for the import in the platform

    # Generate the .json file of the assessment
    json_filename = f'processed_files/assessment-{assessment_version}_scoring-{scoring_version}_{str_now}.json'
    with open(json_filename, 'w', encoding="utf-8") as fp:
        json.dump(dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)


if __name__ == '__main__':
    main()
