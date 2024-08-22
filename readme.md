# Google Sheets Task Processor

This project reads data from a Google Spreadsheet, performs simple calculations, and updates the spreadsheet with the results. It is built using Python and the Google Sheets API.

## Features

- Read data from specified cells in a Google Spreadsheet.
- Perform arithmetic operations (e.g., addition) on the data.
- Update the spreadsheet with the calculated results.
- Mark tasks as "Done" once processed.

## Prerequisites

- Python 3.x
- Google API credentials (OAuth 2.0 client credentials)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/sudip_dai.git
    cd sudip_dai
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv environment
    source environment/bin/activate  # On Windows use `environment\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Google API credentials:**

    - Obtain OAuth 2.0 client credentials from the [Google Cloud Console](https://console.cloud.google.com/).
    - Download the `secrets.json` file and place it in the project directory.

## Usage

1. **Run the script:**

    ```bash
    python reading.py
    ```

2. **Authorize the application:**

    - The first time you run the script, you will be prompted to authorize the application via your Google account.
    - Follow the provided URL, sign in with your Google account, and allow access to your Google Sheets.

3. **View results:**

    - The script will read data from the specified Google Spreadsheet, perform calculations, and update the spreadsheet with the results.
    - Updated cells will show the calculated result and a "Done" status.

## Project Structure

sudip_dai/
├── reading.py # Main script that processes the spreadsheet data
├── requirements.txt # Python dependencies
├── secrets.json # Google API credentials (not included in the repository)
├── token.json # Stored access and refresh tokens (auto-generated)
└── README.md # Project documentation

