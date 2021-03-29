# Processing scripts for the RTDS assessment

## Introduction

This library provides several scripts enabling to:

- Parse the raw version of the French and English assessment and create a single structured object capturing all its properties
- Generate a scoring template easy-to-read and easy-to-fill-in
- Parse the scoring template once completed and create a structure scoring object
- Leverage the upgrade table and the scoring to compute summaries of:
  - the total max score configured per section
  - the evaluation elements conditional to others
  - the evaluation elements having a dedicated non-concerned answer item
  
## Instructions

### Standard use - Complete processing

1. Fetch the remote version of the repository with `git fetch origin` and `git pull origin master` if needed, and checkout to a new branch (for example `git checkout -b process-new-assessment-version`)

1. Prepare the new assessments (both French version and English version) you would like to process and place in folder `input_files`:

   - the raw assessments. They are expected to be `.md` files (although any text file format should probably work)
   - add the language code suffix (`-fr` and `-en`) to the raw assessments. ex: `assessment-0.63-fr.md`, `assessment-0.63-en.md`
   - its upgrade table. It is expected to be a `.json` file following a strict structure (see already existing ones)

1. Determine a previous version of the assessment and of its associated scoring you wish to use to pre-fill your scoring template for the new assessment you want to process.

1. Check and complete or amend the parameters of the processing in `main.py`. You have to specify both the English name and the French name.

   ```python
   ASSESSMENT_MD_VERSION_FILENAME_FR = 'assessment-0.61-fr.md'
   ASSESSMENT_MD_VERSION_FILENAME_EN = 'assessment-0.61-en.md'
   ASSESSMENT_VERSION = '0.61'
   ASSESSMENT_NAME_FR = 'Evaluation Data Science Responsable et de Confiance'
   ASSESSMENT_NAME_EN = 'Responsible and Trustworthy Data Science Assessment'
   OLD_VERSION_TO_CHECK = '0.6'  # previous version of the assessment
   OLD_SCORING_FILENAME = 'assessment-0.6_scoring-1.json'  # scoring reference of the previous version 
   ```

   Then execute the corresponding cell of `main.py`.

1. Execute the first cell of `main.py`. It will create:

   - the `.json` version of the assessment in folder `/processed_files`
   - the `.txt` scoring template in folder `/intermediary_files`

1. Fill-in the scoring template. If you configured previous versions correctly your template should be pre-filled, and only answer items which are new in the assessment are prefixed with `....` so that you can identify them quickly.

   > Note: **Make sure you save your file**.

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

### Processing only a new scoring template

If you only need to update the scoring template for an assessment already processed, proceed as follow:

1. Update the scoring template and be very careful to increment the scoring version (second line of the scoring template)

1. Then execute partially `main.py` as follow:

   1. Run the preliminary cell and the instantiation of the `Assessment` object:

      ```python
      new_assessment = assessment.Assessment(...)
      ```

   1. Then run the second cell:

      ```python
      new_assessment.process_scoring_template_to_json()
      new_assessment.enrich_assessment_with_scoring_recap()
      new_assessment.enrich_assessment_with_non_concerned_recap()
      ```

1. You should be good to go. Don't forget to commit your new scoring and updated structured assessment, and push them to the remote.
