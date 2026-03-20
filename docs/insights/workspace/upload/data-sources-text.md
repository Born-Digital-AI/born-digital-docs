# Data sources (Text)

This section is used for data sourcing using the manual upload option or integration with other data sources.

![]()

On-screen elements:

## Custom mailbox

- Configure O365: feature for connecting with an Office 365 mailbox account. You can use  "Client secret", “Refresh token”, “Certificate”, or "Azure Connect" as per your needs.

- 1) Client details: for "Client secret", “Refresh token”, “Certificate” authentications:

- Client ID: input field. Fill in a value as per: 
Azure Portal → Microsoft Entra ID (Azure AD) → App registrations → Application details
- Tenant ID: inout field. Fill in a value as per: 
Azure Portal → Microsoft Entra ID → Overview or organization properties
- Client secret or Refresh token or Thumbprint (Certificate): input field

- Client secret: fill in a value as per: 
Azure Portal → Microsoft Entra ID → App registrations → Certificates & secrets → “New client secret”
- Refresh token: fill in a value as per:
After an OAuth2 login using grant_type: authorization_code flow, retrieved via your app or a tool like Postman
- Thumbprint (certificate): Generate a certificate and then upload it using the button below. 
Azure Portal → Microsoft Entra ID → App registrations → Certificates & secrets → Upload or generate a certificate

- Upload: button for Certificate option to upload the certificate
- Mailboxes: section for the specification of the email address(es) from the connected email group (via Client ID and Tenant ID) that are to be connected and used as an email source for further analysis 

- +: button for the addition of a new email address. 

- Email: input field for an email address
- Folder ID: input field for additional specification of an email source, this is for choosing a folder of the email address mentioned above.
- Schedule sourcing:

- From (UTC) + To (UTC): date fields for delimiting the timeframe of emails that are to be copied from the defined mailboxes
- Minutes for sourcing: numbers input field for telling the worker how often new emails should be fetched from the defined mailboxes
- Should download unread e-mails only: checkbox for defining whether only unread emails are to be downloaded from the defined mailboxes
- 2) Client details: for "Azure Connect"

- Connect: button for connecting a mailbox via Microsoft email authentication

> **DANGER:** Make sure that you have chosen the correct mailbox; if none is selected, all emails (to which the Client has access) from the mail server are fetched!

---

## Default mailbox

- Default mailbox: 

- Is active: switch for activating the possibility to send an email from your email client to your project email address (always in a format of analytics-project_id@analytics.borndigital.ai)
- Use attachments: switch for processing the attachments. Attachments are then downloaded and usable in the Digital Agent flow project.

- Max attachments: input field for capping the number of attachments that can be downloaded
- Max size in bytes: input field for capping the size of one attachment.
- Max pages: input field for capping the number of pages of one attachment.

---

## Upload

A feature for uploading email files for analysis.

- Upload: button for manual uploading of CSV data files for processing. Once uploaded, a "Content preview" window is displayed.
- Content preview: window displaying parsing and analysing options

![]()



- Statistics:

- Total Rows: number representing rows identified in the uploaded file
- Preview Rows: number representing rows currently displayed
- Column to analyse: dropdown menu for selection of a column that is to be analysed
- ⚙️ Quotechar: input field with default value " " " used to enclose text containing special characters like semicolon, ensuring that the semicolon within the text is not read as a column separator "Delimiter".

- Example: “New York; NY” will be intact and not parsed into columns even though it contains a semicolon = ;
- ⚙️ Delimiter: input field with default value ";" that is used for parsing of the CSV file into columns
- ⚙️ Encoding: input field with default value "utf-8-sig" used for text encoding of the uploaded CSV file
- Preview table: displays parsed file as per settings above
- Import: button for importing the file for the analysis

---

## Send text

Feature alternating CSV "Upload" feature with direct email sending from the Digital Studio platform. It is mainly used for testing or demo purposes. 

![]()

- Send text as an email for analysis: 

- Email address: to which any of the emails can be sent using directly the Digital Studio UI. Email is unique for each project in a format analytics-project_id@analytics.borndigital.ai.
- Type email text for analysis:

- Email text: input field for simulation of the email body
- ⚙️ Advanced options: switch enabling additional features listed below

- Attachments: feature for the addition of attachments to an email that is to be sent

- Supported document types: pdf, word dosc, csv, txt, png, jpg, webp, tiff
- Upload: button for uploading attachments

- Metadata (JSON): editor for accompanying the "Email text" with additional metadata, like a subject, in JSON format
- Send: button for sending the email

> **WARNING:** Make sure to toggle the "Is active" switch of the "Default mailbox" type if you want to send an email from your email client. For sending directly with "Type email for analysis" button, you do not need the switch to be turned on.

---

## Copy data from another project

> **SUCCESS:** Use this feature to fine-tune your parameters or prompts without interfering with your main project!

- Project: drop-down field for a selection of the "Insight" → "Text" project if the current project is of the "Text" type
- Version: drop-down field for selecting a version of the selected project
- From (UTC) + To (UTC): date fields for delimiting the timeframe of emails that are to be copied from the selected project
- **Floating buttons:**

- Check: button for validating how many emails will be copied after using the "Copy" button. The number will be displayed below the "From (UTC) + To (UTC)" date fields.

![]()
- Copy: button for initiation of copying emails from the selected project
- Save: button for saving the settings

> **WARNING:** Make sure you have access to the project of interest; otherwise, you will not be able to copy any files.
