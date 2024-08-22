Python quickstart 

bookmark_border
Quickstarts explain how to set up and run an app that calls a Google Workspace API.

Google Workspace quickstarts use the API client libraries to handle some details of the authentication and authorization flow. We recommend that you use the client libraries for your own apps. This quickstart uses a simplified authentication approach that is appropriate for a testing environment. For a production environment, we recommend learning about authentication and authorization before choosing the access credentials that are appropriate for your app.

Create a Python command-line application that makes requests to the Google Sheets API.

Objectives
Set up your environment.
Install the client library.
Set up the sample.
Run the sample.
Prerequisites
To run this quickstart, you need the following prerequisites:

Python 3.10.7 or greater
The pip package management tool
A Google Cloud project.
A Google Account.
Set up your environment
To complete this quickstart, set up your environment.

Enable the API
Before using Google APIs, you need to turn them on in a Google Cloud project. You can turn on one or more APIs in a single Google Cloud project.
In the Google Cloud console, enable the Google Sheets API.

Enable the API

Configure the OAuth consent screen
If you're using a new Google Cloud project to complete this quickstart, configure the OAuth consent screen and add yourself as a test user. If you've already completed this step for your Cloud project, skip to the next section.

In the Google Cloud console, go to Menu menu > APIs & Services > OAuth consent screen.
Go to OAuth consent screen

For User type select Internal, then click Create.
Complete the app registration form, then click Save and Continue.
For now, you can skip adding scopes and click Save and Continue. In the future, when you create an app for use outside of your Google Workspace organization, you must change the User type to External, and then, add the authorization scopes that your app requires.

Review your app registration summary. To make changes, click Edit. If the app registration looks OK, click Back to Dashboard.
Authorize credentials for a desktop application
To authenticate end users and access user data in your app, you need to create one or more OAuth 2.0 Client IDs. A client ID is used to identify a single app to Google's OAuth servers. If your app runs on multiple platforms, you must create a separate client ID for each platform.
In the Google Cloud console, go to Menu menu > APIs & Services > Credentials.
Go to Credentials

Click Create Credentials > OAuth client ID.
Click Application type > Desktop app.
In the Name field, type a name for the credential. This name is only shown in the Google Cloud console.
Click Create. The OAuth client created screen appears, showing your new Client ID and Client secret.
Click OK. The newly created credential appears under OAuth 2.0 Client IDs.
Save the downloaded JSON file as credentials.json, and move the file to your working directory.
Install the Google client library
Install the Google client library for Python:


pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib