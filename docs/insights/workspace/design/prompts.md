# Prompts

This module is for creating and managing Prompts. They pair parameters into wholes that are then used for processing audio (transcriptions) and text inputs.

## Configuration

![]()

On-screen elements:

- Details:

- Name: input field of the prompt
- Language: drop-down field for processing the prompt
- Prompt state: dropdown field for changing the state to one of these: "Enabled", "Disabled for all" (completely disabled), or "Disabled for rerun" (disabled only for any of the following reruns) states
- Multi-segment analysis (input longer than 110k tokens, ie >10 hours of speech or 40k words in an email): radio buttons for choosing which part of a long, multi-chunk record this prompt should read: use "Each" chunk (for sentiment analysis), only the "First" chunk (for greetings), or only the last chunk (for farewell).

> **INFO:** ### Why the Multi-segment analysis setting exists

In the past, the LLM models used to have smaller "context" - ie the length of audio or text which we sent for analysis had to be broken into several chunks before processing, analysed in sequence and summarized.

However!

Nowadays models have no problem with long context. The chunking is only applied in these situations:

- recordings longer than cca 10 hours
- emails longer than 30-50k words (depends on the content, images, email structure)
- texts longer than 80k-90k words

In case you are using such long inputs, the Multi-segment analysis control gives you a say in how a prompt reacts to that split: it lets you decide whether the prompt should read every chunk, just the opening segment, or only the final one.

- Parameters:

- Predefined parameter group: input field for selecting already predefined hardcoded parameter groups. Once any of them is selected,  its predefined, hardcoded parameters are then listed in the "Parameters" field below.
- Parameters: input field for selection of parameters (custom-made or predefined)

****

- *Previous parameter: input field. If any parameter is selected, then its outcome is used as an input for this prompt. 
Example: summary of the audio record (prompt_summary)*

> **INFO:** You can only select parameters that are used by other prompts. Thus, the naming convention is in this format: <prompt>_<parameter>.

- Instructions: input field for additional prompt specifics. E.g., output file type, processing specifics, structure requirement, etc. It is mainly used in some specific cases to fine-tune the output.
- Conditions: section for specifying cases, based on values of already processed parameters, on which the current prompt should be applied:

- Condition: dropdown field for selection of logical operators "AND" and "OR".
- Add new condition: link displays upon clicking the following fields below. You can add multiple conditions at once. 

- Parameter: dropdown field for selection of parameters from other prompts in the format <prompt>_<parameter>
- Value: input field displaying values based on the selected parameter
- Temperature: input field for changing the creativity of the model output. 
Lower values (closer to 0) make output more deterministic, focused, and consistent (sometimes called “stricter”).
Higher values (such as 0.7 or 1) increase creativity and diversity, making the model more exploratory in its responses.
- ⚙️ Provider: 

![]()

- Create provider: button for opening a form for the selection of LLMs that will be used for processing


- Provider: dropdown menu with options representing LLM providers (Azure OpenAI, Anthropic, Gemini, Groq, or OpenAI)
- API Key: input field
- Model name: input field
- API base: input field for entering URL
- API version: inout field for
- Remove: button
- Create: button for creating the prompt with the latest configuration

> **INFO:** Tip: Use the predefined parameters for inspiration, but add little details for your individual use-case. (Ie exact call script for your agents to introduce to customers, like: The value YES, if the agent greeted, introduced himself and asked "How can I help you?". The value NO otherwise.

vs. the default:

The value YES, if the agent greeted, introduced himself, said the name of the company. The value NO otherwise.

## Management

- The order of prompts defines their running order.

![]()

On-screen elements:

- Upper part:

- Search prompts: bar for searching parameters based on their name
- + Create: button for creating a new prompt
- Select: button for selecting multiple parameters in their list at once, and then for the following actions:

- Prompt state: dropdown field for changing the state to one of these: "Enabled", "Disabled for all" (completely disabled), or "Disabled for rerun" (disabled only for any of the following reruns) states
- Delete: button for deleting the selected prompt(s)
- *List of prompts:
(Elements are listed from the left)*

- Name: of the prompt
- Pencil: icon button for editing the prompt
- Command line: icon indicating the prompt state
- Language: used for processing the prompt
- Prompt provider type: displaying either "Default provider" or any other, as per the provider configuration
- Parameters preview: displaying a preview of the parameters used by the prompt, upon hovering over them, their definition is displayed
- Floating buttons:

- Export: for exporting all prompts in a JSON-formatted file
- Import: for importing prompts in a JSON-formatted file
- Save: for saving prompt changes
