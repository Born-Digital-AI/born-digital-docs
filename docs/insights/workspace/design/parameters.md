# Parameters

This module is used for creating and managing parameters that are later used by prompts.

## Types and configuration fields

### Custom

Their purpose is to obtain data of interest as their variables from the files of the selected [Data sources](). They are later combined and used by [Prompts](). 

![]()

On-screen elements:

- Type: drop-down field with values "[Custom]()" and "[Flow connector]()" for the change of the parameters type
- Bin icon: button for the deletion of the parameter
- **Details:**

- Name: input field of the parameter
- Language: drop-down field, for selecting parameter processing language. If "Universal" is selected, the model decides for itself, using the language in the instructions.
- Global: switch, if enabled, the parameter can be used in the other projects within the organisation
- Definition: input field for a parameter instruction that is later passed as a prompt to obtain a value
- Output format: buttons for choosing the right output format of "String" (text), "Number", or "Boolean" (true or false) type
- **Settings:**

- Fallback value: input field for providing a filled-in output value in case there is an error in the evaluation of the "Definition", and none of the values from the "List of values" are chosen
- Enforce: switch for enforcing fallback value. It can be turned on only if there is a value in the "List of values" field.
- List of values: input field for defining values that should be used as an output of the "Definition" evaluation. Values are input individually (use enter for input).
- Custom categories: drop-down field for selecting the user-defined categories of a [custom type and AI category suggestions](). After the selection, the result of the parameter will then fall into the category.
- Constraint: input field for describing the format validation of the output
- ⚙️ Multi prompt behaviour: drop-down field with processing strategies for aggregating results from multiple prompts, since some of the prompts used to be parsed and sent to bypass context window limits.
- ⚙️ Weighted table: drop-down field. It is enabled once "WEIGHTED_VALUE" is chosen as a value in the "Multi prompt behavior" field. It displays options for how to process multi-prompt aggregation using a weighted table strategy.

****

> **INFO:** Multi prompt setups are used to decompose a single complex task into smaller prompt segments because language models have limited context windows. Dividing input text or audio transcriptions into several prompts allows handling large documents or recordings without truncation. Each prompt processes part of the content, and the system later aggregates the partial outputs into a unified response.

This is relevant only for very long audio/text inputs (ie >1h recording).

- Normalization: of the parameter`s output

- Letter case conversation: radio buttons for changing the output to be Lowercased, Uppercased, or Capitalized, or none of these, based on the selected value
- Remove diacritics: radio buttons for removing diacritics from the output value if "Yes"
- Apply underscore: radio buttons for applying underscore from the output value if "Yes"
- Save: floating button for saving the settings to the parameter

### Flow connector

These parameters are used for the connection with the [flows]() defined in the [Digital Agent]() project type. Once connected, you can pass insight data to flow for further processing and then retrieve it. 

![]()

On-screen elements:

- Type: drop-down field with values "[Custom]()" and "[Flow connector]()" for the change of the parameters type
- Bin icon: button for the deletion of the parameter
- Details:

- Select project to connect: drop-down field for a selection of the "Digital agent" flow project
- Select trained version: drop-down field for a selection of a version of the selected project
- Name: input field of the flow connector
- Global: switch, if enabled, the parameter can be used in the other projects within the organisation
- Definition (auto-generated): field displaying the hash ID of the selected Digital agent project and version (each version has unique hash ID)
- Output variables: input field for defining what the output variables of this parameter will be. Once defined, only these variables will be pulled out of the connected flow. Input the variables individualy exactly as defined in Flow, escape with enter.

> **SUCCESS:** Pro Tip:
Send relevant data from Digital Agent back to Insights -> you can them use them in your Dashboards easily.

- Send results from previous prompts to the flow: switch

- If disabled (default state), only transcription (of audio files) or parsed emails will be passed to the flow

- Transcriptions or emails are then sent one by one into the flow`s "current_utterance" variable
- If enabled, along with the data, it also publishes all previous prompts and their values/results listed above the prompt containing this flow connector parameter. 

- The previous prompt's value/result can then be accessed in the flow using the name convention <previous_prompt>_<parameter>
- Should process email attachments: switch to enable processing email attachments in the flow
- Save: floating button for saving the settings to the parameter

> **WARNING:** Consider creating and selecting a proxy project in the "Select project to connect" field, so you do not need to re-select the target flow project after each (re)training. Please see more [here]().

## Management

![]()

On-screen elements:

- Upper part:

- Search parameters: bar for searching parameters based on their name
- Filters (below search bar):

- All: button for displaying all parameters

- Global: button for displaying only the global parameters of both flow or custom types
- Custom: button for displaying only custom parameters (not global)
- Flow: button for displaying only flow parameters
- Select: button for selecting multiple parameters in their list at once, and then for following self-describing actions like "Duplicate" and "Delete"
- *List of parameters:
(Elements are listed from the left)*

- **Parameter name**
- Pencil: icon button for editing the parameter
- Language: displaying selected language for the parameter processing
- Parameter type: displaying either "Custom" or "Flow connector" value
- Prompt preview: displaying a value of the parameters "Definition" field
- Floating buttons:

- Export: for exporting all parameters in a JSON-formatted file
- Import: for importing parameters in a JSON-formatted file
