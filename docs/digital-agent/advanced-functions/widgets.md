# Widgets

Widget enhances the interactivity of chat with your Digital agent by allowing users to engage with dynamic components directly within the conversation flow.

![]()

****

**Widget Behavior:**

- Interaction: When the chatbot encounters an ANS node functioning as a widget, it displays the widget within the chatbot bubble, allowing users to interact with it directly.
- Submission: The chatbot pauses its flow and waits for the user to fill out and submit the widget. Once the user submits the widget, the chatbot continues its flow according to the defined path in the diagram.

**Data Handling:**

- Variable Storage: Values collected from the widget, such as user responses or selections, are stored in backend variables for further processing and analysis.

> **WARNING:** Widgets are designed for use within chat-based Digital agents only and are not compatible with voicebots.

> **INFO:** Widget graphic elements, including colours, fonts, and overall chatbot bubble appearance, can be customized to match the client's branding and style. Contact the [Born Digital team]() to explore customization options.

---

# Star rating

The Star rating is a widget designed to gather user feedback through a star rating system. It allows users to rate their satisfaction on a scale of stars and optionally provide additional comments.

![]()

```javascript
'1':  WIDGET: Chatbot_Rating  DATA:    widget:      Question: 'Please rate our conversation.'      Submit_Button_Message: Submit      Feedback_Message: Thanks!      Star_Labels:        - Horrible        - Bad        - Standard        - Good        - Great      Additional_Fields:        - visible_on: '[true,true,true,true,true]'          title: 'Could you give us a feedback?'          placeholder: Type here...
```

**Configuration Parameters:**

1. Question: The prompt displayed to users, asking for their feedback.

- Data Type: String
- `Example: "Please rate our conversation. How easy was it for you to resolve the issue with the information we provided?"`
2. Submit_Button_Message: The text displayed on the submit button.

- Data Type: String
- `Example: "Submit"`
3. Feedback_Message: The message displayed to users after they submit their feedback.

- Data Type: String
- `Example: "Thank you for your response."`
4. Star_Labels: Labels for the star rating scale, indicating user satisfaction levels. The number of stars is based on the number of elements listed in the array. Additional stars can be added to provide more granularity in the rating scale. 
The strings in the array will be displayed on hover above the corresponding number of stars. The string meaning should start from the lowest rating and progress upwards (e.g., the worst to the best, the lowest to the highest) to maintain consistency within the scale. Ensure that each label reflects a corresponding level of satisfaction and fits within the scale progression.

- Data Type: Array of Strings
- **Example:**

```javascript
[...]Star_Labels: - Very Dissatisfied - Dissatisfied - Neither Satisfied nor Dissatisfied - Satisfied - Very Satisfied[...]
```
5. Additional_Fields: Additional input fields that can be displayed alongside the star rating widget. The additional field is optional and does not need to be shown for all ratings. The visibility of the additional field can be customized using the visible_on parameter, where the number of elements in the array corresponds to the number of stars.

- Data Type: Array of Objects
- **Example:**

```javascript
[...]Additional_Fields:  - visible_on: '[true,true,true,true,true]'    title: 'We would appreciate it if you could provide reasons for your rating:'    placeholder: Your response
```

- The visible_on array determines when the additional field should be displayed. 
For example:
[true, true, true, true, true]: The additional field is displayed for all ratings.
[false, false, false, false, false]: The additional field is not displayed for any rating.[true, true, false, false, false]: The additional field is displayed only if the user selects one of the two lowest ratings
- The title parameter specifies the text to be displayed above the textarea for feedback. It's recommended to provide instructions and a request for feedback in this field.
- The placeholder parameter specifies the text to be displayed inside the textarea where users can provide feedback. For example, "Write here". If no placeholder text is desired, an empty string "" can be used.



---

# NPS

The NPS_Rating widget is designed to collect feedback using the Net Promoter Score (NPS) methodology. Users are prompted to rate their likelihood of recommending a product or service, typically on a scale from 0 to 10.

![]()

```javascript
'1':  WIDGET: NPS_Rating  DATA:    widget:      Question: How likely is it you recommend our services to your family and friends?      Submit_Button_Message: Submit      Feedback_Message: Thank you!      MinScale: 0      MaxScale: 10      Scale_Min_Text: Most unlikely      Scale_Max_Text: Most likely
```

**Configuration Parameters:**

1. Question: The prompt displayed to users, instructing them to provide their response on a given scale, where the highest score represents "most likely" and the lowest represents "definitely not likely."

- Data Type: String
- Example: "Please rate your response on a scale of 0 to 10, with ten representing very likely and zero representing definitely not likely."
2. Submit_Button_Message: The text displayed on the submit button.

- Data Type: String
- `Example: "Submit"`
3. Feedback_Message: The message displayed to users after they submit their response.

- Data Type: String
- `Example: "Thank you for your response."`
4. MinScale:The minimum value on the rating scale.

- Data Type: Integer
- `Example: 0`
5. MaxScale:The maximum value on the rating scale.

- Data Type: Integer
- `Example: 10`
6. Scale_Min_Text:The text corresponding to the minimum value on the rating scale (e.g., "Definitely not likely").

- Data Type: String
- `Example: "Definitely not likely"`
7. Scale_Max_Text: The text corresponding to the maximum value on the rating scale (e.g., "Very likely").

- Data Type: String
- `Example: "Very likely"`

---

# Like or Dislike rating

The Like Dislike Rating widget provides users with the option to express their preference regarding a chat session by indicating whether they liked or disliked it. Users can also provide specific feedback about what they liked or what could be improved.

![]()

```javascript
'1':  WIDGET: Like_Dislike_Rating  DATA:    widget:      description: Did you like our chat?      isChatInputHidden: true      submit: Send      likeForm:        - enabledOnSelected: true        - placeholder: Let me know what you liked the most.      dislikeForm:        - enabledOnSelected: true        - placeholder: Let me know what to improve.
```

**Configuration Parameters:**

1. description: A brief description of the purpose, prompting users to indicate whether they liked the chat session, service, information provided etc.

- Data Type: String
- `Example: "Did you like our chat?"`
2. isChatInputHidden: Determines whether the chat input field is hidden during the rating process.

- Data Type: Boolean
- `Example: true`
3. submit: The text displayed on the submit button.

- Data Type: String
- `Example: "Send"`
4. likeForm: Configuration for the form fro users to fill out if they liked the chat.

- Data Type: Array of Objects
- **Example:**

```javascript
[...]likeForm:  - enabledOnSelected: true  - placeholder: "Let me know what you liked the most."[...]
```
- Sub-Parameters:

- enabledOnSelected: Determines whether the form is enabled when the "like" option is selected. Set true if you want to show feedback form after the user selected thumb's up , otherwise set false.
- placeholder: The placeholder text displayed inside the input field for users to provide feedback on what they liked.
5. dislikeForm:Configuration for the form users can fill out if they disliked the chat.

- Data Type: Array of Objects
- **Example:**

```javascript
[...]dislikeForm:  - enabledOnSelected: true  - placeholder: "Let me know what to improve."
```
- **Sub-Parameters:**

- enabledOnSelected: Determines whether the form is enabled when the "dislike" option is selected. Set true if you want to show feedback form after the user selected thumb's down , otherwise set false.
- placeholder: The placeholder text displayed inside the input field for users to provide feedback on what could be improved.

**Output Variables:**

After the user submitted result to Like or Dislike rating widget, output is always stored in three variables named  Like_Dislike_Rating_Widget_Result, Dislike_Rating_Widget_Dislike_Form and Like_Dislike_Rating_Widget_Like_Form.

- Like_Dislike_Rating_Widget_Result: Stores the overall rating result chosen by the user ('Like' or 'Dislike').

- Data Type: String
- `Example: "like"`
- Like_Dislike_Rating_Widget_Dislike_Form: Stores the feedback provided by the user in the dislike form.

- Data Type: String
- `Example: "The response time was too slow."`
- Like_Dislike_Rating_Widget_Like_Form: Stores the feedback provided by the user in the like form.

- Data Type: String
- `Example: "I liked the helpful responses."`

---

# Checkbox

The Checkbox widget provides users with the ability to select a single choice or multiple options from a list using checkboxes. This widget is suitable for collecting responses to single-choice or multiple-choice questions or gathering feedback on various options.

![]()

```javascript
'1':  WIDGET: Checkbox  DATA:    widget:      checkboxSingleCheck: false      description: Choose your favourite ice cream flavours.      checkbox:        - name: icecream_vanilla          text: Vanilla        - name: icecream_chocolate          text: Chocolate          textIfChecked: Chocolate is the best!        - name: icecream_strawberry          text: Strawberry        - name: icecream_lemon          text: Lemon        - name: icecream_caramel          text: Salted caramel      buttons:        - button_name_1: Submit          text: Submit          clickable_if: ''
```

**Configuration Parameters:**

1. checkboxSingleCheck: Determines whether only one option can be selected at a time (true for single selection, false for multiple selections).

- Data Type: Boolean
- Example: false (Multiple selections allowed)
2. description: Provides additional context or instructions for users regarding the purpose of the checkbox widget.

- Data Type: String
- `Example: "Please selected your favourite ice cream flavours from the checkbox below. Multiple options can be selected."`
3. checkbox: Defines the list of options available for selection using checkboxes. Each option is defined by one object in the array. Define as many checkbox options as you want.

- Data Type: Array of Objects
- **Example:**

```javascript
[...]checkbox:  - name: variable_option_1    text: Option 1  - name: variable_option_2    text: Option 2    textIfChecked: "This is the text which appears if Option 2 is checked"  - name: variable_option_3    text: Option 3[...]
```
- Sub-Parameters:

- name: The variable name where the selection status (true/false) of the checkbox will be stored.
- text: The text displayed next to the checkbox option.
- textIfChecked (Optional): Additional text that appears when the checkbox is checked.
4. buttons: Defines the button associated with the widget, such as a submit button.

- Data Type: Array of Objects
- **Example:**

```yaml
buttons:  - button_name_1: Submit    text: Submit    clickable_if: ''
```
- Sub-Parameters:

- text: The text displayed on the button. Customize it to your liking.
- clickable_if (Optional): Condition for button clickability. Leave empty for unconditional clickability.

> **INFO:** Additionally, the name parameter within the Checkbox widget defines the variable name where the selection status (true/false) of each checkbox option will be stored. This variable can be utilized to drive subsequent scenarios within the chatbot's flow based on the user's selections.

---

# Geolocation

The Geolocation widget is a feature designed to enable users to share their precise location or localise precise points/addresses within the chat interface.

![]()

```javascript
'1':  WIDGET: Geolocation  DATA:    widget:      name: location      title: Your location      description: "Please allow GPS localisation in your browser."      submit_button_text: Find my location      enableSkipButton:        enabled: false        text: Skip      enableComment:        enabled: false        variableName: GeolocationComment        label: Leave a comment        placeholder: Type here..      enable_map_visualization: true      map_visualization_text: Check the location on map      map_visualization_submit_button_text: Confirm      enable_address_retrieval: true
```

**Configuration Parameters:**

1. name : Defines the variable name where the location data will be stored.

- `Example: location`
2. title: Displayed at the top of the widget, providing context to users.

- Data type: String
- `Example: Your location`
3. description: A brief instruction guiding users on how to enable GPS localization. Show below the Title of the widget.

- Data type: String
- `Example: Please allow GPS localization in your browser.`
4. submit_button_text: Text displayed on the button to initiate location retrieval.

- Data type: String
- `Example: Find my location`
5. enableSkipButton:Allows users to skip sharing their location if preferred.

- `Enabled: true/false`
- `Text: Text displayed on the button, eg. "Skip"`
6. enableComment: Permits users to leave additional comments or notes along with their location.

- `enabled: true/false`
- `variableName: name of the variable where the comment string will be stored, eg. GeolocationComment`
- `label: Label displayed above the comment box, data type: string, eg.:Leave a note`
- `placeholder: Text displayed in the comment box until the user starts typing, data type: string, eg. Type here...`
7. enable_map_visualization: Option to visualize the location on a map interface for enhanced user experience.

- Data type: Boolean
- `Example: true`
8. map_visualization_text: Displayed above the map interface to prompt users to explore their location visually.

- Data type: String
- `Example: Check the location on map`
9. map_visualization_submit_button_text: Text on the button to confirm the selected location on the map.

- Data type: String
- `Example: Confirm`
10. enable_address_retrieval:Option to retrieve the address corresponding to the selected location, enriching the data collected.

- Data type: Boolean
- `Example: true`

---

# Carousel search

The Carousel Search widget presents a carousel of items with images, allowing users to browse through the options and select individual items. This widget enhances user engagement by providing a visually appealing interface for exploring various choices.

Clicking on an item within the carousel sends its name as an utterance to the chatbot, indicating the user's selection.

When enabled, users can filter carousel items by name, facilitating quicker access to specific items. Users can search for items by typing in keywords or starting letters, allowing for efficient navigation through the carousel.

![]()

```javascript
'1':  WIDGET: CarouselSearch  DATA:    widget:      items:        pikachu: 'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png'        bulbasaur: 'https://upload.wikimedia.org/wikipedia/en/2/28/Pok%C3%A9mon_Bulbasaur_art.png'        charizard: 'https://upload.wikimedia.org/wikipedia/en/1/1f/Pok%C3%A9mon_Charizard_art.png'        squirtle: 'https://upload.wikimedia.org/wikipedia/en/5/59/Pok%C3%A9mon_Squirtle_art.png'        jigglypuff: 'https://upload.wikimedia.org/wikipedia/en/thumb/2/22/Pok%C3%A9mon_Jigglypuff_art.png/225px-Pok%C3%A9mon_Jigglypuff_art.png'        psyduck: 'https://upload.wikimedia.org/wikipedia/en/2/2d/Pok%C3%A9mon_Psyduck_art.png'      search: true
```

**Configuration Parameters:**

1. items: Defines the list of items to be displayed in the carousel, each consisting of a name and an image URL.

- Data Type: Object
- **Example:**

```javascript
[...]items:  pikachu: 'https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png'  bulbasaur: 'https://upload.wikimedia.org/wikipedia/en/2/28/Pok%C3%A9mon_Bulbasaur_art.png'[...]
```
2. search: Enables or disables the search functionality, allowing users to filter carousel items by name.

- Data Type: Boolean
- Example: true (Search functionality enabled)

---

# Calendar

The Calendar widget provides users with the capability to select a date and time conveniently within the chatbot interface.

## Single date selection

![]()

![]()

```javascript
'1':  WIDGET: Calendar  DATA:    widget:      heading: "Choose day and time"      submitButtonMessage: Submit       chooseTime: true       date:         name: callback_date        type: singleDate      time:         name: callback_time        minTime: "8:00"        maxTime: "20:00"
```

**Configuration Parameters:**

1. heading:Specifies the heading or title displayed above the calendar interface, guiding users to choose a day and time.

- Data Type: String
- Example: "Choose day and time"
2. submitButtonMessage: Defines the text displayed on the submit button, allowing users to confirm their date and time selection.

- Data Type: String
- Example: "Submit"
3. chooseTime:Determines whether users can select a specific time in addition to the date.

- Data Type: Boolean
- Example: true (Time selection enabled)
4. date: Configures the date selection settings, including the variable name to store the chosen date and the type of date selection.

- Sub-Parameters:

- name: The variable name where the selected date will be stored.
- type: Specifies the type of date selection, such as singleDate (single-day selection) or rangeDate (date range selection).
5. time: Configures the time selection settings, including the variable name to store the chosen time, minimum and maximum time limits.

- Sub-Parameters:

- name: The variable name where the selected time will be stored.
- minTime: Specifies the earliest selectable time.
- maxTime: Specifies the latest selectable time.



## Date range selection

The Calendar widget, configured for date range selection, allows users to specify a range of dates conveniently within the chatbot interface.

```javascript
'1':  WIDGET: Calendar  DATA:    widget:      heading: "Choose range"      submitButtonMessage: Submit       chooseTime: false      date:         name: callback_date        type: range        minDate: 2024-01-01        maxDate: 2025-12-31        startDateText: "Start of the range"        endDateText: "End of the range"
```

**Configuration Parameters:**

1. heading:Specifies the heading or title displayed above the calendar interface, guiding users to choose a date range.

- Data Type: String
- Example: "Choose range"
2. submitButtonMessage:Defines the text displayed on the submit button, allowing users to confirm their date range selection.

- Data Type: String
- Example: "Submit"
3. chooseTime:Determines whether users can select a specific time in addition to the date. In this configuration, time selection is disabled.

- Data Type: Boolean
- Example: false (Time selection disabled)
4. date: Configures the date range selection settings, including the variable name to store the chosen date range, the type of date selection, minimum and maximum date limits, and custom text for the start and end dates.

- Sub-Parameters:

- name: The variable name where the selected date range will be stored.
- type: Specifies the type of date selection, in this case, "range" for date range selection.
- minDate: Specifies the earliest selectable date. YYYY-MM-DD format required.
- maxDate: Specifies the latest selectable date. YYYY-MM-DD format required.
- startDateText: Custom text displayed for the start date selection.
- endDateText: Custom text displayed for the end date selection.

## Multiple date selection

The Calendar widget, configured for multiple date selection, presents users with a predefined list of dates as checkboxes, allowing them to choose multiple dates simultaneously within the chatbot interface.

```javascript
'1':  WIDGET: Calendar  DATA:    widget:      heading: "Pick a date"      submitButtonMessage: Submit       chooseTime: false      date:         name: callback_date        type: multipleDate        multipleDateValues:         - 2024-04-01         - 2024-05-01         - 2024-06-01         - 2024-07-01         - 2024-08-01
```

**Configuration Parameters:**

1. heading:Specifies the heading or title displayed above the calendar interface, guiding users to pick a date.

- Data Type: String
- Example: "Pick a date"
2. submitButtonMessage: Defines the text displayed on the submit button, allowing users to confirm their date selection.

- Data Type: String
- Example: "Submit"
3. chooseTime: Determines whether users can select a specific time in addition to the date. In this configuration, time selection is disabled.

- Data Type: Boolean
- Example: false (Time selection disabled)
4. date:Configures the multiple date selection settings, including the variable name to store the chosen dates, the type of date selection, and a predefined list of selectable dates.

- Sub-Parameters:

- name: The variable name where the selected dates will be stored.
- type: Specifies the type of date selection, in this case, "multipleDate" for selecting multiple dates.
- multipleDateValues: Predefined list of dates that users can choose from.

---

# Generic form

The Generic Form widget offers flexible customization options to create a dynamic form within the chatbot interface, which includes various field types such as text input, dropdown selection, and checkboxes, allowing users to input diverse types of information efficiently.

**Parameter configuration:**

1. description: This parameter allows you to define a textual description that will be displayed above the form. It can be used to explain the purpose of the form or provide instructions to the user.

- Data Type: String
- Example: "This is a description text, which can be also longer to explain what is happening"
2. submit: This parameter determines the text displayed on the submit button of the form. Users, by clicking on this button, confirm their inputs and submit the form.

- Data Type: String
- Example: "Submit"

```javascript
1:  WIDGET: Generic_Form  DATA:    widget:      description: This is a description text, which can be also longer to explain what is happening      submit: Submit      field: [...]
```

Let's explain the field parameter, which contains individual fields of the widget. Each field represents an input or selection element in the form, and the name of each field also serves as a variable where the value entered by the user will be stored after the form submission, eg. order_id_field, name_field, surname_field.

### Field Configuration:

```javascript
1:     [...]      field:         order_id_field:           visible: 'true'          label: "Field label, eg. Order ID"          placeholder: "Type order ID here"          validForSelections:                - 1          type: text          validation:            pattern:              value: ^71[2-9][3-9][0-9]{6}$              error_message: "Wrong format. Order ID starts with 71 and has 10 digits."            minlength:              value: '10'              error_message: Order ID is too short. Must have exactly $value digits.            maxlength:              value: '10'              error_message: Order ID is too logn. Must have exactly $value digits...        name_field: [...]        surname_field: [...]        phone_number_field: [...]        email_field: [...]        message_field: [...]
```

1. order: Specifies the order in which the field appears within the form. Lower values appear first.

- Data Type: Integer
- `Example: "order": '1'`
2. visible: Determines whether the field is visible to the user.

- Data Type: Boolean (true/false)
- `Example: "visible": true`
3. label: Defines the label or prompt displayed alongside the input field, providing instructions or information about the expected input.

- Data Type: String
- `Example: "label": "Order ID"`
4. placeholder: Specifies a placeholder text that appears inside the input field when it is empty, giving users a hint about the expected input.

- Data Type: String
- `Example: "placeholder": "Start typing..."`
5. type: Determines the type of input or selection element for the field.

- Data Type: String
- Possible Values: "text", "textarea", "tel", "dropdown", etc.
- `Example: "type": "text"`
6. validation: Defines validation rules for the field to ensure that the user input meets specific criteria.

- Data Type: Object
- Subparameters: Can include rules such as required, pattern, minlength, maxlength, etc.
7. values (for dropdown type): Specifies the list of options available for selection in a dropdown field.

- Data Type: Array of strings
- **Example:**

```json
"values": [  "the fist option",  "the second option",  "the third option",  "None of above"]
```

> **INFO:** For detailed configuration and (sub)parameters of different field types, check-out:

## Selection buttons filter

The selection parameter in the Generic Form widget allows users to present initial choices or options to the form respondents. These selections act as a gateway to determine which subsequent fields will be displayed based on the user's choice.

When configuring the selection parameter, users define a set of options along with their corresponding labels. Upon rendering the form, these options are presented to the users as buttons.

Based on the option selected by the user, only the fields associated with that particular selection will be displayed, while the rest remain hidden. This mechanism enables the creation of more interactive and context-sensitive forms tailored to the user's choices and preferences.

![]()

![]()

In the provided example, the selection parameter offers two options: "Ice cream" and "Steak." Depending on the user's selection, either the field for specifying the favorite ice cream flavor or the field for describing steak preferences will be shown, while the other field remains hidden. 

To specify which fields are shown for each selection, the validForSelections parameter is used within each field.

```javascript
1:  WIDGET: Generic_Form  DATA:    widget:      description: "Please fill in your personal info, than click on Submit."      submit: Submit      selection:        visible: true        label: Please select. You rather enjoy...        values:          - Ice cream          - Steak      field:        icecream_flavour:          order: '1'          visible: 'true'          label: What's your favourite ice cream flavour?          validForSelections:            - 1          placeholder: Type here          type: text          validation:            required:              error_message: "Please fill this field."            pattern:              value: ^.+$              error_message: "Please fill this field."        steak:          order: '2'          visible: 'true'          label: How do you prefer your steak?          validForSelections:            - 2          placeholder: Type here          type: text          validation:            required:              error_message: Field must be filled            pattern:              value: ^.+$              error_message: Field must be filled.        drink:          order: '3'          visible: 'true'          label: What's your drink of choice?          validForSelections:            - 1             - 2          placeholder: Type here          type: text          validation:            required:              error_message: Field must be filled            pattern:              value: ^.+$              error_message: Field must be filled.
```

**Parameters configuration:**

- description:  Provides a brief description or instruction to users about the purpose of the form.

- Data Type: String
- `Example Value: "Please fill in your personal info, then click on Submit."`
- submit: Specifies the text displayed on the submit button.

- Data Type: String
- `Example Value: "Submit"`
- selection: Defines the selection options presented to users at the beginning of the form.

- Data Type: Object
- **Subparameters:**

- visible: Determines whether the selection options are visible to users.

- Data Type: Boolean
- `Example Value: true`
- label: Provides a label or prompt for the selection options.

- Data Type: String
- `Example Value: "Please select. You rather enjoy..."`
- values: Specifies the options users can choose from.

- Data Type: Array of Strings
- `Example Value: ["Ice cream", "Steak"]`
- field : Contains individual fields of the widget. Each field represents an input or selection element in the form

- Data type: Object
- Subparametres:

- order: Specifies the order in which the field appears in the form.

- Data Type: String or Number
- `Example Value: "1"`
- visible:Determines whether the field is visible to users.

- Data Type: Boolean
- `Example Value: "true"`
- label: Provides a label or prompt for the field.

- Data Type: String
- `Example Value: "What's your favourite ice cream flavour?"`

> **INFO:** The selection parameter offers initial choices to users, determining which fields appear next. When a user makes a selection, only the fields relevant to that choice are displayed, optimizing the form-filling experience.

Field ordering, denoted by the order parameter within each field, influences the sequence in which fields are displayed. Lower numerical values indicate earlier display positions. Ensure that fields crucial for initial selections have lower order values to appear first and guide users efficiently through the form.

## Text field

The field type text allows users to create customizable forms with various input fields to collect specific information.

![]()

```javascript
1:  WIDGET: Generic_Form  DATA:    widget:      description: "Please fill in your personal info, than click on Submit."      submit: Submit      field:        person_name:              order: '1'              visible: 'true'              label: Your name.              validForSelections:                - 1                - 2              placeholder: Type here              type: text              validation:                required:                  error_message: Name must be filled.                pattern:                  value: ^[a-zA-Zá-žÁ-Ž][a-zA-Zá-žÁ-Ž\s-]*$                  error_message: Cannot use digits or special characters.        person_surname:          order: '2'          visible: 'true'          label: Your surname.          validForSelections:            - 1            - 2          placeholder: Type here          type: text          validation:            required:              error_message: Surname must be filled            pattern:              value: ^[a-zA-Zá-žÁ-Ž][a-zA-Zá-žÁ-Ž\s-]*$              error_message: Cannot use digits or special characters.
```

**Parameters Configuration:**

- description: Provides a brief description or instruction to users about the purpose of the form.

- Data Type: String
- `Example Value: "Please fill in your personal info, then click on Submit."`
- submit: Specifies the text displayed on the submit button.

- Data Type: String
- `Example Value: "Submit"`
- field:Contains individual fields of the widget. Each field represents an input or selection element in the form.

- Subparametres:

- order: Specifies the order in which the field appears in the form.

- Data Type: String or Number
- `Example Value: "1"`
- visible: Determines whether the field is visible to users.

- Data Type: Boolean
- `Example Value: "true"`
- label: Provides a label or prompt for the field.

- Data Type: String
- `Example Value: "Your name."`
- validForSelections: Specifies the selections for which the field is valid.

- Data Type: Array of Numbers
- `Example Value: [1, 2]`
- placeholder: Displays a placeholder text within the input field.

- Data Type: String
- `Example Value: "Type here"`
- type:Defines the type of input field (e.g., text, tel, dropdown).

- Data Type: String
- `Example Value: "text"`
- validation:Defines validation rules for the input field.

- Data Type: Object
- Subparametres:

- required:Specifies whether the field is required.

- Data Type: Object
- **Example Value:**

```json
"required":   "error_message": "Name must be filled."
```
- pattern: Defines a regular expression pattern for validating the input value.

- Data Type: Object
- **Example Value:**

```json
"pattern":   "value": "^[a-zA-Zá-žÁ-Ž][a-zA-Zá-žÁ-Ž\s-]*$",  "error_message": "Cannot use digits or special characters."
```

## Textarea field

Unlike a single-line text field, a textarea  field type provides a larger space for users to input longer free-form text, suitable for messages, event descriptions, notes, and more.

![]()

```javascript
"1":  WIDGET: Generic_Form  DATA:    widget:      description: Leave your message here.      submit: Send      field:        message_field:          order: "1"          visible: "true"          label: Message          placeholder: Type here          type: textarea          rows: 5          validation:            required:              error_message: Please fill in your message. Max. lenght is 3000 characters.            minlength:              value: "10"              error_message: Min. $value characters!            maxlength:              value: "3000"              error_message: Max. $value characters!
```

**Parameters configuration:**

- description: A brief instruction or description guiding users on what to input in the form.

- Data Type: String
- `Example: "Leave your message here."`
- submit: The text displayed on the form's submit button.

- Data Type: String
- `Example: "Send"`
- `**field **`

- Contains individual fields of the widget. Each field represents an input or selection element in the form. Field are defined by subparametres.
- order: Specifies the order in which the field appears within the form.

- Data Type: Integer
- `Example: "1"`
- visible: Determines whether the field is visible to users.

- Data Type: Boolean (true/false)
- `Example: "true"`
- label: The label displayed above the text area field, indicating its purpose.

- Data Type: String
- `Example: "Message"`
- placeholder: A temporary text displayed within the text area field, providing a hint or example of the expected input.

- Data Type: String
- `Example: "Type here"`
- type: Specifies the type of field, in this case, a text area.

- Data Type: String
- Example: "textarea"
- rows: Determines the number of visible lines (rows) in the text area field.

- Data Type: Integer
- `Example: 5`
- **validation:**

- error_message: The message displayed to users when validation conditions are not met.
- Data Type: String
- `Example: "Please fill in your message. Max. length is 3000 characters."`

## Phone number field

The field type tel in the Generic Form widget allows users to input their phone numbers.

![]()

```javascript
1:  WIDGET: Generic_Form  DATA:    widget:      description: Fill in your phone number, than click on Submit.      submit: Submit      field:        person_phone:              order: '1'              visible: 'true'              label: Phone number              validForSelections:                - 1                - 2              placeholder: Type here              type: tel              data:                prefix: '+420'                editable: 'True'                validation:                  required:                    error_message: Make sure prefix is filled too.                  pattern:                    value: ^\+[0-9]*$                    error_message: Wrong format of prefix.                  minlength:                    value: '3'                    error_message: "Too short. Prefix must be +01, or +012"                  maxlength:                    value: '4'                    error_message: Too long. Prefix must be max. 4 characters.              validation:                required:                  error_message: Phone number has to be filled.                pattern:                  value: ^[0-9]*$                  error_message: Wrong format.                minlength:                  value: '8'                  error_message: Too short. Phone number must be at least $value digits.                maxlength:                  value: '12'                  error_message: Too long. Phone number must be max. $value digits.
```

**Parameters Configuration:**

- description: Provides a brief description or instruction to users about the purpose of the form.

- Data Type: String
- `Example Value: "Fill in your phone number, then click on Submit."`
- submit: Specifies the text displayed on the submit button.

- Data Type: String
- `Example Value: "Submit"`
- field: An object containing all the widget fields. The sub-object /field name, eg. phone_number , is also a variable where the entered value from the form will be stored.

- order:Specifies the order in which the field appears in the form.

- Data Type: String or Number
- `Example Value: "1"`
- visible:  Determines whether the field is visible to users.

- Data Type: Boolean
- Example Value: "true".
- label: Provides a label or prompt for the field.

- Data Type: String
- `Example Value: "Your phone number:"`
- validForSelections:Specifies the selections for which the field is valid.

- Data Type: Array of Numbers
- `Example Value: [1, 2]`
- placeholder: Displays a placeholder text within the input field.

- Data Type: String
- `Example Value: "Type here"`
- type: Defines the type of input field (e.g., text, tel, dropdown).

- Data Type: String
- `Example Value: "tel"`
- data: Additional data configuration for specific field types.

- Data Type: Object

- prefix (optional): Specifies a prefix for the input field, such as a country code.

- Data Type: String
- `Example Value: "+420"`
- editable (optional): Determines whether the input field is editable.

- Data Type: Boolean
- `Example Value: true`
- validation: Defines validation rules for the input field.

- Data Type: Object
- required: Specifies whether the field is required.

- Data Type: Object
- Example Value:

- ```javascript
"required":  "error_message": "Phone number has to be filled."
```
- pattern: Defines a regular expression pattern for validating the input value.

- Data Type: Object
- **Example Value:**

```javascript
"pattern":   "value": "^[0-9]*$",  "error_message": "Wrong format."
```
- minlength: Specifies the minimum length of the input value.

- Data Type: Object
- **Example Value:**

```javascript
"minlength":  "value": "8",  "error_message": "Too short. Phone number must be at least 8 digits."
```
- maxlength: Specifies the maximum length of the input value.

- Data Type: Object
- **Example Value:**

```javascript
"maxlength":   "value": "12",  "error_message": "Too long. Phone number must be max. 12 digits."
```

## Dropdown selection field

This example demonstrates the configuration of the Generic Form widget to create a simple dropdown menu.

![]()

```javascript
1:  WIDGET: Generic_Form  DATA:    widget:      description: Enter your adventurous journey with a starter buddy!      submit: Submit      field:        dropdown_value_variable:          order: '1'           visible: 'true'          label: Choose your starter pokémon champion!          placeholder: Click here          type: dropdown          validation:            required:              error_message: You must select a champion          values:            - bulbasaur            - charmander            - squirtle            - pikachu
```

**Configuration Parameters:**

1. description: This parameter defines the descriptive text displayed above the form, guiding users on the widget's purpose or instructions.

- Data Type: String
- `Example Value: "Enter your adventurous journey with a starter buddy!"`
2. submit:  This parameter specifies the text displayed on the submission button within the form, allowing users to submit their selections.

- Data Type: String
- `Example Value: "Submit"`
3. **field:**

- dropdown_value_variable: This is the name of the variable where selected value will be stored. Also, other subparameters under this object must be defined.

- order: This parameter determines the order in which the form field appears within the widget, influencing its position relative to other fields if multiple are present.

- Data Type: Integer
- `Example Value: 1`
- visible: This parameter controls the visibility of the form field, indicating whether it is displayed to users.

- Data Type: Boolean
- `Example Value: true`
- label: This parameter specifies the label or prompt associated with the form field, providing context or instructions for users.

- Data Type: String
- `Example Value: "Choose your starter Pokémon champion!"`
- placeholder: This parameter defines the placeholder text displayed within the form field when it is empty, guiding users on what to input.

- Data Type: String
- `Example Value: "Click here"`
- type: This parameter sets the type of form field to create, such as dropdown, text input, or textarea.

- Data Type: String
- `Example Value: Dropdown`
- `**validation:**`

- required: This parameter specifies whether the form field must be filled out before submission, enforcing user input.

- Data Type: Boolean
- Example Value: true
- values:This parameter provides a list of options for the dropdown menu, allowing users to select from predefined choices.

- Data Type: List of Strings
- Example Value: [bulbasaur, charmander, squirtle, pikachu]

> **INFO:** Pro-tip!
Within one Generic Form widget, you have the flexibility to combine various types of fields according to the needs of your form. 


Each field can be individually tailored, whether it's a single-line text field, a textarea for longer descriptions, an input field for phone numbers, or even a dropdown menu for selecting from predefined options. Thanks to this flexibility, you can create forms that precisely match your requirements and user needs. Your imagination is the only limit!
