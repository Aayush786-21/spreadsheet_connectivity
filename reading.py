import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets(json_keyfile, spreadsheet_name):
    # Set up the Google Sheets API client
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
    client = gspread.authorize(creds)
    
    # Open the spreadsheet
    sheet = client.open(spreadsheet_name).sheet1
    return sheet

def process_tasks(sheet):
    # Get all the tasks, conditions, and user inputs
    tasks = sheet.col_values(1)  # Column A
    conditions = sheet.col_values(2)  # Column B
    user_inputs = sheet.col_values(3)  # Column C

    # Process each task and write the output to column D
    for i in range(1, len(tasks)):  # Starting from 1 to skip the header
        task = tasks[i]
        condition = conditions[i]
        user_input = user_inputs[i]
        
        output = generate_output(condition, user_input)
        
        # Write the output to column D
        sheet.update_cell(i+1, 4, output)  # D column is the 4th column

    print("Processing complete!")

def generate_output(condition, user_input):
    if condition == "yes" and user_input == "yes":
        return "okay on it"
    elif condition == "yes" and user_input == "no":
        return "data is ignored"
    else:
        return "data is ignored"

def main():
    # Replace with your actual JSON key file and spreadsheet name
    json_keyfile = 'your-key-file.json'
    spreadsheet_name = 'Your Spreadsheet Name'
    
    sheet = authenticate_google_sheets(json_keyfile, spreadsheet_name)
    process_tasks(sheet)

if __name__ == "__main__":
    main()
