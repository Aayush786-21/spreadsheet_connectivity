# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# # Set up the Google Sheets API client
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('your-key-file.json', scope)
# client = gspread.authorize(creds)

# # Open the spreadsheet
# sheet = client.open('Your Spreadsheet Name').sheet1


# Get all the tasks, conditions, and user inputs
tasks = sheet.col_values(1)  # Column A
conditions = sheet.col_values(2)  # Column B
user_inputs = sheet.col_values(3)  # Column C

# Process each task and write the output to column D
for i in range(1, len(tasks)):  # Starting from 1 to skip the header
    task = tasks[i]
    condition = conditions[i]
    user_input = user_inputs[i]
    
    if condition == "yes" and user_input == "yes":
        output = "okay on it"
    elif condition == "yes" and user_input == "no":
        output = "data is ignored"
    else:
        output = "data is ignored"

    # Write the output to column D
    sheet.update_cell(i+1, 4, output)  # D column is the 4th column

print("Processing complete!")
