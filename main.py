# -*- coding: utf-8 -*-
"""
Editable script to process the raw .md versions of the assessment
"""

import assessment

ASSESSMENT_MD_VERSION_FILENAME = 'assessment-0.61.md'
ASSESSMENT_VERSION = '0.61'
ASSESSMENT_NAME = 'DSRC Assessment'
OLD_VERSION_TO_CHECK = '0.6'
OLD_SCORING_FILENAME = 'assessment-0.6_scoring-1_20201027161214.json'

# --------------------------------------------------------------------------------------
#%% First cell - Instantiate assessment, process it to .json and create scoring template
# --------------------------------------------------------------------------------------

# Instantiate a new assessment object
new_assessment = assessment.Assessment(ASSESSMENT_MD_VERSION_FILENAME,
                                       ASSESSMENT_VERSION,
                                       ASSESSMENT_NAME,
                                       OLD_VERSION_TO_CHECK,
                                       OLD_SCORING_FILENAME,
                                       )

# Create the .json file for the new assessment
new_assessment.dump_to_json_file()

# Create its scoring template (pre-filled with scoring config from a previous version)
new_assessment.create_scoring_template()

# --------------------------------------------------------------------
#%% Second cell - Process scoring template (launch it when filled in!)
# --------------------------------------------------------------------

new_assessment.process_scoring_template_to_json()
new_assessment.enrich_assessment_with_scoring_recap()
new_assessment.enrich_assessment_with_non_concerned_recap()
