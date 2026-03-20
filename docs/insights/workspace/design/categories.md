# Categories

This module is for creating and managing categories that are then used for the categorisation of the processed text or audio from data sources.

## Types, configuration, and management of the fields

### Custom

It is a basic type that needs to be defined manually. These custom categories are then selectable in [parameters]() settings and serve for categorisation of audio or text files. 

![]()

On-screen elements:

- Type switch: in the upper part of the screen, with options "Custom" and "AI category suggestions" for switching the creation category type
- "+": button for creating a new category, fields below are displayed after clicking:

- Name: input field of a new category is displayed only after using the "+" button

- Bin icon: for deleting the category
- + Add subcategory: button for creating a new subcategory
- Sub-category 1: name input field is displayed only after using "+ Add subcategory" 

- Bin icon: for deleting the sub-category
- Save: floating button for saving the settings to the category

### AI category suggestions

This feature uses [prompts]() as its input and, based on them, suggests categories. 

![]()

On-screen elements:

- Type switch: in the upper part of the screen, with options "Custom" and "AI category suggestions"
- Input: drop-down field containing [prompts]() displayed in combination with their individual parameters.
ie, <prompt1>_<parameter1>, <prompt1>_<parameter2>, ... <prompt1>_<parameterx> 
ie, “basic_summary”, which, after the selection, will categorize processed text or audio based on the summary
- Category count: input field for defining the number of categories that should be suggested. You can specify multiple values, for example, 5, 10, 15 at once.
- Version: dropdown field with values representing versions of [reruns]() on which the AI category suggestions will be applied
- From (UTC) + To (UTC): date fields for delimiting the timeframe of text or audio records used for categorisation
- Instructions: input field for additional prompt specifics. E.g., output file type, processing specifics, structure requirement, etc. It is mainly used in some specific cases to fine-tune the output.
- Check: button for validating how many text or audio record results will be categorized after using the "Suggest" button. The number will be displayed below the button.

![]()

> **WARNING:** Use "Check" to check how many results (interactions, recordings, emails...) will be used for suggesting categories - if the number is too small (<10), the results might not represent the sample well. If the number is too big (>500), the suggestion will take some time. For the best results, we recommend using a sample of around 100.

- Suggest: button for running the AI category suggestions. Suggested categories are displayed on the right side. If not, use a "Refresh" button.
- Refresh: button for displaying the suggested categories after using the "Suggest" button
- Save: floating button for saving the settings to the AI category suggestor
