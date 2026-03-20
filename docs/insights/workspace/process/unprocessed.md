# Unprocessed

This module serves to display the status of processing files after their manipulation, ie, data upload, copy, rerun, etc.

![]()

On-screen elements:

- Refresh: button
- Table options:

- Columns: button with a dropdown menu with options to display or hide columns in the table, as per the selection
- Filters: button for displaying a floating window with options below for creating filtering conditions:

- Columns: dropdown menu displaying all available columns
- Operator: dropdown menu displaying all possible operators
- Value: input field for specifying a value based on which to filter
- Density: button with a dropdown menu with text size display options of the rows from smallest to biggest: "Compact", "Standard", "Comfortable"

****

- Table columns:

- Id: column displaying file id
- Created At: column displaying the date and time of the file addition to the queue
- Updated At: column displaying the date and time of the file update
- Rerun: column displaying info whether the cron job is of rerun type or not (True or False)
- Status: column displaying whether the status is "Waiting" or "Processing" state
- Name: column displaying the name of the file that is being processed
- Type: column displaying the name of the codec used for processing the audio file
- STT provider: column displaying the name of the [STT provider]() used for the file processing
- Step: column displaying the pipeline stage, like ingestion, transcription, enrichment
- Rows per page: dropdown with options 10, 25, 100 for displaying the corresponding number of rows in the table
- 0-0 of 0: Number of ítems displaying on a page. E.g., "1-8 of 8"
- < + >: buttons
