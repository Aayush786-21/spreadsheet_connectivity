import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1HCJO08fPbWYWwgte7kKe4DBJpAFzyl5GbQmOKUUWopA"

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("secrets.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheets = service.spreadsheets()
        
        for row in range(2, 8):
            task1_result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!A{row}").execute().get("values")
            task2_result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!B{row}").execute().get("values")
            
            if task1_result and task2_result:
                task1 = int(task1_result[0][0])
                task2 = int(task2_result[0][0])
                calculated_result = task1 + task2
                print(f"processing {task1} + {task2}")

                sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!C{row}", valueInputOption="USER_ENTERED", body={"values": [[f"{calculated_result}"]]}).execute()
                sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!D{row}", valueInputOption="USER_ENTERED", body={"values": [["Done"]]}).execute()
            else:
                print(f"Row {row}: Data is missing in one or both of the cells.")
        
    except HttpError as error:
        print(error)
    
if __name__ == "__main__":
    main()
