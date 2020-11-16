# Processing scripts for the RTDS assessment

## Introduction

This library provides several scripts enabling to:

- Parse the raw version of the assessment and create a structured object capturing all its properties
- Generate a scoring template easy-to-read and easy-to-fill-in
- Parse the scoring template once completed and create a structure scoring object
- Leverage the upgrade table and the scoring to compute summaries of:
  - the total max score configured per section
  - the evaluation elements conditional to others
  - the evaluation elements having a dedicated non-concerned answer item
  
## Instructions

1. Fetch the remote version of the repository with `git fetch origin` and `git pull origin master` if needed, and checkout to a new branch (for example `git checkout -b process-new-assessment-version`)

1. Prepare the new assessment you would like to process and place in folder `/input_files`:
   - the raw assessment. It is expected to be a `.md` file (although any text file format should probably work)
   - its upgrade table. It is expected to be a `.json` file following a strict structure (see already existing ones)

1. Determine a previous version of the assessment and of its associated scoring you wish to use to pre-fill your scoring template for the new assessment you want to process.

1. Check and complete or amend the parameters of the processing in `main.py`
    ```python
    ASSESSMENT_MD_VERSION_FILENAME = 'assessment-0.61.md'
    ASSESSMENT_VERSION = '0.61'
    ASSESSMENT_NAME = 'DSRC Assessment'
    OLD_VERSION_TO_CHECK = '0.6'  # previous version of the assessment
    OLD_SCORING_FILENAME = 'assessment-0.6_scoring-1.json'  # scoring reference of the previous version 
    ```
   Then execute the corresponding cell of `main.py`.

1. Execute the first cell of `main.py`. It will create:
   - the `.json` version of the assessment in folder `/processed_files`
   - the `.txt` scoring template in folder `/intermediary_files`
   
1. Fill-in the scoring template. If you configured previous versions correctly your template should be pre-filled, and only answer items which are new in the assessment are prefixed with `....` so that you can identify them quickly.

    Note: **Make sure you save your file**. 

1. Execute the second cell of `main.py`. It will:
   - create the `.json` version of the scoring
   - update the `.json` version of the assessment with the summaries
   
1. Check the summaries at the end of the `.json` version of the assessment, and verify if it is coherent.

1. Commit the newly processed files and push them to the remote:
   ```bash
   git add .
   git commit -m "Process version XX of the assessment"
   git push origin process-new-assessment
   ```
