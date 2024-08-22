import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapi.com/auth/spreadsheets"]

SPREADSHEET_ID = "1HCJO08fPbWYWwgte7kKe4DBJpAFzyl5GbQmOKUUWopA"

def main():
    Credentials = None
    if os.path.exists("token.json"):
        Credentials = Credentials.from_authorized_user_file("token.json",SCOPES)
    if not Credentials or not Credentials.valid:
        if Credentials and Credentials.expired and Credentials.refresh_token:
            Credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("secrets.json", SCOPES)
            Credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(Credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=Credentials)
        sheets = service.spreadsheets()
        
        for row in range(2,8):
            task1 = int(sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!A{row}").execute().get("values")[0][0])
            task2 = int(sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!B{row}").execute().get("values")[0][0])
            calculated_result = task1 + task2
            print(f"processing {task1} + {task2}")

            sheets.values().update(spreadsheetId=SPREADSHEET_ID, range=f"Sheet1!C{row}", valueInputOption="USER_ENTERED", body={"values":[[f"{calculated_result}"]]}).execute()
            sheets.values().update(spreadsheetId= SPREADSHEET_ID, range=f"Sheet1!D{row}", valueInputOption="USER_ENTERED", body={"values": [[f"{Done}"]]}).execute()
        
    except HttpError as error:
        print(error)
    
if __name__ == "__main__":
    main()
