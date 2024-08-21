
# Google Sheets Task Processor

Google Sheets Task Processor is a Python-based application that interacts with a Google Spreadsheet to automate the processing of tasks. The script reads tasks, conditions, and user inputs, processes them according to predefined rules, and writes the results back into the spreadsheet.

## Features

- Connect to Google Sheets using the Google Sheets API
- Read tasks, conditions, and user inputs from a Google Spreadsheet
- Process each task based on user-defined conditions
- Write the output back to the Google Spreadsheet
- Modular design for easy expansion and maintenance

## Prerequisites

- Python 3.x
- Google Cloud Project with Sheets API and Drive API enabled
- `gspread` library
- `oauth2client` library
- Service account credentials JSON file

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Aayush786-21/sudip_dai.git
cd google-sheets-task-processor

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
```bash
pip install gspread oauth2client

4. Set up Google API credentials:
Go to the Google Cloud Console.
Create a new project and enable the Google Sheets API and Google Drive API.
Create a service account and download the credentials JSON file.
Share your Google Spreadsheet with the service account email found in the JSON file.

5. Update the script with your credentials:
Replace 'your-key-file.json' in the code with the path to your service account JSON file.
Replace 'Your Spreadsheet Name' with the name of your Google Spreadsheet.

Usage

Run the script:
python reading.py

Use the application:
The script will process each task based on the conditions and user inputs and update the results in the spreadsheet.

Project Structure
reading.py: Main application file with functions to authenticate, process tasks, and generate outputs.
requirements.txt: List of dependencies required to run the project.
README.md: Project documentation.