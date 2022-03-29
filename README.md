# drf_excel_processing

An example DRF project on how to upload and process excel files using openpyxl

## Requirements

The requirements.txt/environment.yml lists all Python moduls required. In short:

- Python 3.10
  - Django==4.0.3
  - djangorestframework==3.13.1
  - openpyxl==3.0.9

Note: Project was created under Windows. Installing from requirements.txt under Linux might fail due to possible differences in module versions/version naming

## Install from source

Clone repository or download as zip.
Optional: create a virtualenv / conda env to use an isolated Python environment

Install using pip:

```
pip install -r requirements.txt
```

Install using conda:

```
conda env create -f environment.yml
conda activate drf_excel_processing
```

## Usage

1. Make sure your environment is activated
2. Run the Django development server from the "excel_project" folder using:

```
python .\manage.py runserver
```

3. open your browser and navigate to: http://127.0.0.1:8000/api/v1/
4. Use the provided *example_excel_sheet.xlsx* for upload and processing
5. Use "Raw data" to post columns in the Summary view since DRF does not provide a lists component in the HTML form 

## Notice

- this is just an example project that would need some modifications for production use
- this project uses the DRF Browsable API accessible via browser at http://127.0.0.1:8000/api/v1/ to allow for easier API discoverability
- authentication and authorization was disabled/skipped for ease of use
- as stated in https://docs.djangoproject.com/en/4.0/howto/static-files/ - the way static files are served in this project is not suitable for production use. Follow https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/ in order to serve static files in production.
- the summary endpoint can be accessed either via the summary URL, or via the "Extra Actions" dropdown in a detail view
- since it was just required to create a summary of the provided Excel file, this could have been solved by just implementing one endpoint - however the current approach seems "nicer" overall and allows for easier extensibility
- the current create_summary method assumes that the column names can be found in the first row of the first available sheet

## Improvements

- Compatible/Parsable Excel file/sheet structure should be better defined:

  - What is a column name e.g. column header (A, B, C, AA, AB etc.) or some cell that contains that name as a value
  - Where is a column located e.g. first row or arbitrary location (add parameter with information about the specific row where the column headers can be found)
  - Are duplicated column names allowed? If so, how should they be handled?
  - Excel files use different sheets (tabs at the bottom of the screen) - add parameter to enable sheet selection (via name or index)
  - It might be sensible to also include information about the numbers type, e.g. currency (if any)

- Parse Excel file during initial post to extract columns which could be provided as a general model field and a "MultipleChoiceField" in the summary endpoint

- Better Error handling:

  - ensure loaded file is in fact an Excel file (file extensions do not mean a thing...)
  - return information why data for a specific column was not returned e.g. column not found, TypeError (cannot calculate sum/avg for strings), empty file etc.

- write tests (especially for openpyxl, since I do not a lot of experience with this specific module)
- add comments where needed
