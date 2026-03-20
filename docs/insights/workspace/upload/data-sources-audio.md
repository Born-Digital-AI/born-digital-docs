# Data sources (Audio)

This section is used for data sourcing using the manual upload option or integration with other data sources.

![]()

On-screen elements:

## Sourcing from Azure

- Sourcing from Azure: switch for enabling sourcing from Born Digital's Azure bucket, also called blob storage.
- Provider: drop-down field with values "Azure", "Azure Premium", "ElevenLabs" for processing of audio files described below

****

- Display type: drop-down field with values "lexical", "display", "itn", "maskedITN" described below

****

---

## **Upload audio files**

feature is suitable for uploading a smaller batch of recordings (ca up to 50), rather for testing or POC cases.

- Upload: button for manual upload of data files for processing in formats .wav, .mp3, .ogg, .flac
- Metadata: switch for displaying a JSON metadata editor underneath it. Once activated, the editor's value applies exclusively to a single audio file for upload.

> **INFO:** Metadata accompanies uploaded audio files, resulting in improved visibility and extending filter options in dashboards; its data can also be utilized in [parameter conditions]() and [Digital Agent flows]().

---

## **Copy data from another project**

> **SUCCESS:** Use this feature to fine-tune your parameters or prompts without interfering with your main project!

- Project: drop-down field for a selection of the "Insight" → "Audio" project if the current project is of the "Audio" type
- Version: drop-down field for selecting a version of the selected project
- From (UTC) + To (UTC): date fields for delimiting the timeframe of audio records that are to be copied from the selected project
- **Floating buttons:**

- Check: button for validating how many emails will be copied after using the "Copy" button. The number will be displayed below the "From (UTC) + To (UTC)" date fields.


![]()
- Copy: button for initiation of copying audio records from the selected project
- Save: button for saving the settings

> **WARNING:** Make sure you have access to the project of interest; otherwise, you will not be able to copy any files.
