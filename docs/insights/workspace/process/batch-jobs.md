# Batch jobs

This module is used for displaying all batch jobs, ie, using prompts (suggesting topics, etc.) and reruns.

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
- Table columns:

- Id: column displaying batch job id
- Created At: column displaying the date and time of the batch job addition to the queue
- Updated At: column displaying the date and time of the batch job update
- Operation: column displaying the name of the batch job operation, like "rerun_call"
- Status: column displaying whether the status is "New", "Processing", "Error", or "Done" state
- Triggered by: column displaying an email address of the initiator of the operation
- Processed: column displaying the number of audio records that are processed
- Total: column displaying the total number of audio records that are to be processed (queued)
- Progress: column displaying the current progress of the cron job in percentages (Done / Total)
- Configuration: column displaying an icon button opening a window with a text editor displaying the configuration in JSON format

![]()
