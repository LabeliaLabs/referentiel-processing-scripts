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

    # Open and read the text file
    # Current directory, where the assessment and the script should be both present
    directory = os.path.dirname(sys.argv[0])
    filepath = directory + glob.glob("scoring_template.txt")[0]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath, "r", encoding="utf-8") as fp:
        raw = fp.read()

        # Capture and fill the version numbers
        assessment_version = re.search(r'Assessment\sversion\s:\s\[(?P<version_nb>.+)\]', raw)
        scoring_version = re.search(r'Scoring\sversion\s:\s\[(?P<version_nb>.+)\]', raw)
        dict["assessment_version"] = assessment_version.group("version_nb")
        dict["scoring_version"] = scoring_version.group("version_nb")

        # Initialize with timestamp and empty dict for answer items
        now = datetime.now()
        dict["timestamp"] = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        dict["answer_items"] = {}

        # Capture all answer items and their number of points
        all_answer_items = re.findall(r'(?P<nb_points>\d{1,2}.?\d{0,2})\s\[(?P<item_id>\d{1,2}.\d{1,2}.\D)\]', raw)
        for item in all_answer_items:
            dict["answer_items"][item[1]] = float(item[0])

    # Generate the .json file of the assessment
    json_filename = f'assessment-{dict["assessment_version"]}_scoring-{dict["scoring_version"]}.json'
    with open(json_filename, 'w', encoding="utf-8") as fp:
        json.dump(dict, fp, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=False)


if __name__ == '__main__':
    main()
