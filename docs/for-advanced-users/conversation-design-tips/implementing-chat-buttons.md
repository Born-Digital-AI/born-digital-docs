# Implementing chat buttons

Button navigation in chatbots provides users with a straightforward and efficient way to interact with the system. By presenting predefined options, buttons simplify the decision-making process and streamline the user experience. However, while buttons offer clarity and ease of use, they can also limit flexibility and require careful design to accommodate various scenarios. Understanding when and how to leverage button navigation can enhance the usability and effectiveness of your chatbot.

**Advantages ****:**

- User-Friendliness: Button navigation provides users with a straightforward and intuitive method of interacting with the chatbot. It requires only a single click on a selected button rather than composing complex sentences.
- Clear Choices: Buttons enable precise definitions of the options available to users, thus eliminating confusion and misunderstandings.

**Disadvantages ****:**

- Limited Flexibility: Button navigation may have limitations compared to free-text input, potentially restricting users' options and leading to frustration.
- Space Constraints: Utilizing buttons may impose constraints on the available space for content, which could be problematic when presenting extensive options or information.

# How chat buttons work

![]()

Buttons within chatbot interfaces serve as simplified means for users to provide input and interact with the system. Here's an overview of their functionality:

Buttons are configured with specific labels in the chatbot interface, representing the available options for users. When a user clicks on a button, the text displayed on the button (label) is sent to the system as an utterance, simulating user input in the input field.

Essentially, buttons act as a simplified pathway for obtaining user input and facilitating interaction with the chatbot. Configuring intent recognition in the Answer (ANS) node is necessary, so the Digital Agnet can progress further in the flow scenario along the defined path.

**The utterance obtained from the button must undergo intent recognition, similar to other inputs, either through keywords, Generative AI-based recognition, or a custom classification model trained on a specific training set. For a detailed explanation of intent recognition configuration, see **

> **INFO:** **Note! **
Users can select only one button within a single menu, as clicking immediately submits the corresponding utterance. For scenarios requiring multiple selections, implementing [widgets](../digital-agent/advanced-functions/widgets.md) such as [checkboxes]() rather than buttons is preferable.

Within the ANS node, you can configure whether to display both button options and a free-text input field simultaneously or hide the free-text input field to prompt users to choose from predefined options. See  for step-by-step tutorial.



## Implementation Methods for Button Configuration

**Method 1: Configuring each button alongside one intent in ANS node**

Within the Answer (ANS) node, buttons can be set up in conjunction with intents. When incorporating an intent, you have the option to designate it as a button. 

- Each intent can be associated with only one button.
- However, not every intent needs to have a corresponding button set within the ANS node. For instance, in case of open-ended questions, we might set buttons for the three most common topics (e.g., "New Product," "Complaints," "Need Assistance") while still allowing for free-text input, thereby recognizing multiple additional topics.

**Method 2: Configuring all buttons from a single variable**

Another approach involves setting buttons from a variable. Prior to the ANS node, define a variable in a preceding node, such as buttons_options variable, and assign an array as its value, e.g., ["New Product", "Complaints", "Need Assistance"].  Then, configuring a button and setting this variable as a source of the whole buttons menu is needed only alongside one of the intents in ANS node. The buttons will then be displayed based on the individual elements within the array, appearing in the order they are listed.

---

# Method #1: Implementing buttons alongside individual intents

![]()

****

When configuring a button for the chatbot, you must define the button label. Optionally, add an icon or image URL for visual enhancement, and select the button's theme (primary or secondary). Once configured, save the settings and configure associated intent settings, such as intent recognition and prompts.

![]()

Once the button label and associated text to be sent upon clicking are configured, the next step involves setting up intent recognition. Each type of intent (training set, keyword, Generative AI) has its own specific requirements and considerations for accurate recognition based on user interaction.

**Training Set:**

- The text displayed on the button (label) must precisely match one of the training sentences defined for the intent.
For example, if the button label is "Need Assistance," there must be a training sentence within the intent's training set that exactly matches this phrase.
- Since training set intents rely on predefined examples, it's crucial to ensure that all potential button labels are included in the training data. This is one of the requirements for project validation before training.

**Keywords:**

- Keywords must match the text displayed on the button. It's advisable to input exact matches or include partial matches if necessary.
For instance, if the button label is "Need Assistance," you can set the keyword as "Need Assistance" or include variations like "Assistance."
- Consider the sensitivity of keyword matching, as it determines how closely the input text needs to match the specified keywords for successful recognition. Remember, keyword intent recognition also supports regular expressions.
- If the field for user input is also allowed, consider keywords or strings for matching possible free-text utterances.

**Generative AI:**

- Describe the intent topic and provide example sentences in the prompt field to guide the Generative AI model in understanding user input. Include various phrases and expressions related to the intent topic to improve the model's ability to recognize user intent accurately.
- Offer a range of example utterances that users might input related to the intent topic. See also  and  tips!



## Buttons and free-text input simultaneously

Look at combining configurated buttons for streamlined navigation with free user input from a text field. By offering both structured options and open-ended communication, this approach accommodates diverse user preferences and interaction styles, creating engaging conversational experiences.

![]()

Here's how it works:

- Incorporate intents into ANS node: Integrate intents into the Answer (ANS) node within the chatbot flow.
- Configure buttons: For selected intents to be displayed as buttons, enable the "Use also as a chat button" option. Configure button label, image and theme and save.
- Configure intent recognition: Establish standard conversation design paths by defining possible intents, their recognition methods, and their target state.
- Standard conversation design: Outline fallback scenarios: set fallback counter and message. Optionally, configure [advanced settings.]()

**Considerations for Button Usage:**

- When implementing buttons, consider that the same intent may be suitable for both button-clicked utterances and user-input utterances, which might use different wording.

### Example use case

Let's say the Digital agent asked for product type to return a specific claim form. Three of the most common product types are Computers, Phones and White goods, so we want to streamline the choice of these options and offer them as buttons. Additionally, we need to recognise other types of products as well.

Take a look at the example configuration of ANS node

![]()

  In Advanced settings, Hide chat input field is disabled, so the user is allowed to send free text.

 Intents are configured (this time, using Generative AI as a method for intent recognition).

 Three intents (Phones, Computers, White goods) have also a chat button configured alongside them.

 Other intents (TV, power tolls, other appliances) are configured as well, but without a dedicated button.

 A fallback scenario is also implemented, in case intent recognition fails.

> **INFO:** **Pro-tip!**

- Especially when utilizing keyword-based intent recognition, account for variations in user input that may not directly match the button text.
- For instance, if categorizing product types for complaints, such as "White goods," "Phones," and "Computers," users may provide responses that align with these categories but use different terms. Thus, the keyword for "White goods" should include additional relevant terms like "refrigerator," "freezer," "dishwasher," "washing machine," etc., to accurately capture user intent.
- If we define the "White goods" intent in this way and a user clicks on the button, the input utterance will be the same as what is written on the button. Similarly, if a user types "White goods" in the chat, the same outcome will occur. However, if a user inputs something slightly different like "it's a minifridge model XY" in the chat, well-defined keywords will allow us to assign it to the correct intent as well.

Check it out for yourself. Download the example project below and import it to your project in Digital Studio!

## Buttons-only navigation

Consider a use case, where only button selection is permitted, and the free text field is hidden. In this scenario, users are prompted to choose from predefined options, requiring selection to submit an utterance based on the button label as input for the chatbot. This approach ensures that users engage with the chatbot within the structured flow and progress further based on their selections.

![]()

To implement button-only selection with a hidden free text field, follow these steps:

Hide Chat Input Field in ANS Node: In the Advanced settings of the Answer (ANS) node, select the option to hide the chat input field.

![]()

Configure Intents and Buttons: Set up intents as usual, and for each intent, configure a corresponding button.

![]()

Keyword Matching for Button Labels: Don't waste your time with training set or Generative AI intents. Since users must select a button, the possible utterances are predetermined. Match the button labels by setting keywords to be the same as the button labels. This is the most effective way to ensure intent recognition for this use case.

Fallback Target Node:
To ensure a valid and trainable configuration, define a target node for fallback scenarios. This target node can be set to any valid target for intents since if a user only selects from predefined options, the fallback scenario cannot ever occur.

> **INFO:** **Pro-tip!**

It's essential to be cautious when using button labels that are substrings of each other, such as "Back" and "Back to the main menu." The order of keyword intents matters; if "Back" is the first keyword intent in ANS node configuration, it will match the utterance sent from clicking on "Back to the main menu" a redirect the flow to incorrect target node. 

Pay attention to button label design to avoid ambiguity or carefully order buttons to prevent unintended matches.

Check it out for yourself. Download the example project below and import it to your project in Digital Studio!

## Primary and secondary buttons

This section explores the use of primary and secondary buttons within a chat interface. It recommends setting primary buttons for main topics and secondary buttons for auxiliary navigation functions (e.g., "Back"). This conversational design approach involves configuring the button theme within the button configuration. It can be applied to scenarios with or without a free text field, providing a structured and intuitive user experience.

![]()

Follow these steps to configure primary and secondary buttons within the chat interface:

- Define Intents: Start by setting up the intents that correspond to the main topics and navigation functions of your chatbot.
- Configure Buttons within Intents: Within each intent, configure the buttons by selecting either primary or secondary themes. The default graphics will be applied. For custom bubbles with personalized graphics, reach out to the Born Digital team.

![]()

- Set Intent Recognition: Configure intent recognition settings to ensure accurate interpretation of user inputs corresponding to the buttons.
- Configure Fallback Scenarios and Advanced Settings: Set up fallback scenarios and any additional advanced settings as needed to manage unexpected user inputs and ensure smooth operation of the chatbot.

### Example use case

Let's say a Digital agent asks users for their favourite treats. If the answer is ice cream, the user is tasked to pick a flavour within button options "Chocolate", "Strawberry" and "Vanilla". Secondary-themed button "Back" is implemented too, in case the user doesn't choose from predetermined options and wants to return to the previous step in the flow.

Take a look at the example configuration of ANS node:

![]()

> **INFO:** **Pro-tip!**

When keeping the user input field visible, it's essential to consider whether the utterance for a secondary button may also appear as a substring within free text input. Therefore, careful consideration must be given to the intent recognition method and rules applied.

For instance, in free-form input, simply using the keyword "Back" for the "Back" button may not suffice if "back" could be part of a valid input for another topic, such as "I want my money back" for a refund intent.

Fortunately, keywords support regular expressions, allowing for more complex matching rules. For example, specifying that "Back" must match the entire string (i.e., "^Back$") clarifies its role as a command to return to the previous step, ensuring that occurrences within longer strings are unlikely to be relevant.

By leveraging such advanced matching rules, you can enhance the accuracy of intent recognition and ensure smooth user interactions within the chatbot interface.

Check it out for yourself. Download the example project below and import it to your project in Digital Studio!

## Buttons for breaking generative AI loops

Explore leveraging buttons within chatbot conversation design as a means to exit generative AI loops. In scenarios where the conversation follows a loop pattern, transitioning out of the loop at the appropriate moment can be challenging.

Usually, intent recognition within the Answer (ANS) node attempts to identify cues indicating the user's desire to exit the loop, such as explicit statements like "Thank you, that's all." However, recognizing these cues can be complex due to the evolving nature of discussions. 

To address this challenge elegantly, buttons can be utilized to provide users with a clear pathway to exit the loop or return to a previous or move to the next step within the conversation flow.

![]()

**This conversational design aims to gracefully exit generative AI loops by utilizing buttons within the chat interface. Here are the key steps of this design flow:**

- User Input in ANS Node: The interaction starts when the user provides an utterance in the Answer (ANS) node. In conversation flow, a MSG node with general instruction usually precedes.
- Generative AI Processing: The user's input is passed to the generative AI, which generates a response based on prompts or prompts combined with a knowledge base.
- Returning to Previous Step: After generating the response, the conversation loops back to the previous ANS node, allowing the user to react and provide a new utterance.
- Continued Looping: This looping process continues as the conversation iterates between user input, generative AI processing, and returning to the ANS node for further interaction.
- Recognizing Exit Cues: Intent recognition configuration within the ANS node attempts to identify cues indicating the user's desire to exit the loop, such as explicit statements like "Thank you, that's all." However, recognizing these cues can be complex due to the evolving nature of discussions.
- Utilizing Buttons for Exit: To address this challenge, buttons are strategically configured within the ANS node to serve as an exit pathway from the loop. By setting specific exit intent recognition for utterances obtained based on clicking on these buttons, users can smoothly transition out of the loop and continue with the conversation flow.
- Fallback Handling: Allowing only the configured exit intents to be recognized intentionally directs all other inputs to the fallback scenario. This ensures that in cases where exit cues are not explicitly stated, the conversation can progress effectively by generating responses through the AI and returning to the loop.

Here are some conversation design use case ideas to inspire you:

****

****

****

****

****

### Example use case

Consider a scenario where we have a chatbot that initiates a generative AI loop when a user expresses their love for pizza . Within this loop, users can engage in conversations about pizza with the chatbot. To simplify the identification of when the user wishes to exit the pizza conversation loop, we implement two buttons:

1. "Back to Main Menu" Button: This button aims to redirect the user back to the main menu, serving as an exit point from the current conversation loop.
2. "Ok, That's Enough!" Button: This button is designed to lead the user out of the loop, allowing them to continue with the main conversation flow.

Within the ANS node, we define two intents corresponding to these buttons. Clicking on either button sends the exact text displayed on the button as an utterance.

![]()

For intent recognition, utilizing keywords corresponding to the button texts is recommended. Using regular expressions, such as "^Ok, that's enough!$", ensures that only these predefined utterances trigger the exit from the loop.

All other user inputs are directed to the fallback, where the fallback counter is set to 0, and the target node is set to the AI node responsible for generating responses. This approach assumes that if the intent recognition does not match the predefined button utterances, the user intends to continue conversing with the AI within the loop.

Check it out for yourself. Download the example project below and import it to your project in Digital studio!

> **INFO:** **Pro-tip!**

Not familiar with regular expressions? Our linguists and conversational designers recommend this [tutorial](). Master regexes in one afternoon!

Familiar, but not confident? Use [this handy tool]()to check whether your regex is matching the desired string properly.



---

# Method #2: Setting all buttons from a single variable

This method allows for the dynamic creation of chat buttons based on variable values. By storing button options in a variable, you can easily manage and update button labels within the conversation flow. This approach offers flexibility and scalability, enabling the chatbot to adapt to changing requirements and user interactions seamlessly. However, we recommend this method to advanced designers, as basic Python syntax or working with variables is necessary.



- Set variable for buttons: In this approach, we need to set a variable in any step in the flow preceding ANS node. Let's name the variable button_options. 

- As its value, we assign an array. For example,  ["Fist topic", "Second topic", "Go back button"], or ["Vanilla", "Chocolate", "Strawberry"] Double quotes are necessary to indicate that these are strings.
- The number of objects in the array corresponds to the number of buttons to be displayed.
- These objects serve as the labels for the buttons, and their order determines the sequence of buttons displayed.

![]()
- Implement button menu to ANS node: To implement button options from a variable in an ANS node, follow these steps:

- Select an intent within the ANS node configuration.
- Enable the option "Use also as a chat button" for the selected intent. In the modal that appears, choose the "Configure button from a variable." In the dialogue window, select or enter the name of the variable where the button options are stored. Save the configuration.
- Complete the configuration for the intent (recognition, target node, etc.) and save it.
- For buttons from a variable, it only needs to be implemented in one of the intents.
- If you want to set up separate buttons using the conventional method in another intent, they will not be added alongside the buttons from the variable or appear on the frontend in the chat. Buttons from the variable apply to the entire ANS node.

![]()

- Configure intent recognition for all intents: After setting up the buttons from the variable, the next step is to configure intent recognition. 

- Even though the variable containing all the button options is within one intent, you need to set up intent recognition and their targets for further flow direction for all the button options.
- Various types of [intent recognition]() can be used for this purpose, ranging from custom training sets and keywords to generative AI and custom conditions.

![]()
- Configure the rest of ANS node: The next step is to configure the remaining settings within the ANS node, such as [advanced settings]() and [fallback]() scenarios, according to the specific requirements of the project.

## Buttons from the variable with pre-set string values

`In this scenario, we prepare simple buttons and store them in a variable. If these buttons are predetermined and their values remain constant, we can list them as an array of strings. For instance, ["Vanilla", "Chocolate", "Strawberry"].`

Because the button values are known in advance, we can customize intent recognition to suit our requirements. This customization can be achieved through various methods, such as using a custom training set, relying on generative AI with defined prompts or keywords, or employing a combination of these approaches.

Check it out for yourself. Download the example project below and import it to your project in Digital Studio!

> **INFO:** Note!
Unfortunately, when setting buttons from a variable, it's currently not possible to define an icon/image or a theme for the buttons. Therefore, it might be more practical to directly define buttons for each intent instead of using a variable.



**Pro-tip!**

The only scenario where using buttons with predetermined labels from a variable might be preferable is when the order of intents in the ANS node configuration needs to differ from the order desired for the buttons.



## Dynamic buttons from variable

In this case, we require the values on the buttons to change dynamically. Within the array for button variables, values can be strings or other variables whose values are strings. 

For example:

- ["cat", "dog", "goldfish"] - Simple strings representing button labels.

![]()

- [ animal_1, animal_2, animal_3] - Values are dynamically populated based on the contents of variables such as animal_1, animal_2, and so on. These variables must be stored in the flow before setting the array variable for buttons.

![]()

- [ animal_1, animal_2, animal_3, "Skip"] - It's also possible to combine fixed values with variables. For instance, for skipping questions or returning to the previous step.

![]()

In this scenario, the dynamic aspect involves the names that appear on the buttons, with the number of buttons determined by the number of objects in the array. As the variables' values change during the conversation flow, the button labels automatically update accordingly. 

> **INFO:** Note! Ensure that variables in the array are not empty to avoid issues with rendering the button menu in the chat bubble frontend!


After setting up the dynamic button values and integrating them into the ANS node, the next step is to ensure proper intent recognition. This is crucial for processing the user's input and advancing the conversation flow. Here's how to approach it:

### Predefined Button Values intent recognition:

If the possible button values are known in advance, such as in the case of displaying recent purchases or product options, set up intents and routing for each potential option.

- For example, if a chatbot offers 30 different products and wants to display the user's last three purchases as buttons, create intent recognition for all 30 products.
- Choose the appropriate method for intent recognition based on the chatbot's requirements and capabilities. Define keywords associated with each intent, or train the chatbot with a custom training set tailored to recognize user intents accurately, or utilize generative AI to prompt the chatbot to understand user intents.

### Unknown dynamic button values intent recognition

When the button values are not known beforehand, and we cannot predefine intent recognition, conditional recognition based on the button options becomes necessary. Here's how to implement it:

- If the button values are stored in variables like option_1, option_2, option_3, which are then stored in an array variable button_options, clicking on a button sends the text displayed on the button as the user utterance.
- Conditional Intent Recognition:

- For Hidden Text Field: If only the button menu is visible, users must click a button, and their utterance will match exactly what's on the clicked button. Set up conditions like current_utterance == option_1 to match the user's input with the button text. Define target nodes accordingly to continue the flow based on the button clicked.

```python
current_utterance == option_1
```

****

- For Enabled Text Field: If users can input text freely, consider the possibility of their input matching a button option. Use conditions like option_1 in current_utterance to check if the text on a button is present in the user's input. Define target nodes based on these conditions to guide the user's flow after clicking a button or providing input.

```python
option_1 in current_utterance
```

- However, the user's input may not exactly match the text on the buttons. Here's how to save the situation. By leveraging generative AI prompts and using variable placeholders, the chatbot can dynamically recognize user intents.
- Prepare generative AI intents and their prompts. Create a concise description indicating the user's query relates to a specific button option. For example, "User's query pertains to option 1."
- Within the ANS node, [edit the generative AI superprompt]() to provide context and include a variable representing the button options.

****



## Buttons from a variable with dynamic values from API 

Explore a dynamic approach where the content of the button menu is fetched in real time from an external data source via an API.

By integrating APIs into the configuration of button menus, chatbots can offer more dynamic and personalized experiences to users. This method allows for real-time updates of available options, ensuring that users have access to the most relevant and up-to-date information within the conversation interface.

Here's how the implementation process works:

1. API Call Integration: Begin by integrating API calls using fetch-url or similar methods. The API call retrieves relevant data that you want to display as button options in your chatbot interface. This data can include product recommendations, recent order history, subscription plans, or any other information relevant to your use case.
2. Data Processing and Storage: Once you receive the output from the API call, process the data and extract the values that you want to display as button options. Store these values in a variable such as button_options, as an array. Additionally, if needed, you can store individual objects in separate variables for later use for intent recognition.
3. Configuration of Button Menu in ANS Node: Next, configure the button menu in the ANS node of your chatbot. Select the option to use buttons from a variable and specify the variable (button_options) that contains the array of button options.
4. Intent Recognition Configuration: Configure intent recognition to handle user interactions with the button menu effectively. Choose an appropriate method for intent recognition based on the nature of your project. If the button options are known in advance, you can set up intent recognition accordingly. However, if the options are dynamic or if you allow free-text input alongside buttons, adjust the intent recognition method accordingly.

### Example project

The objective of this model project is to create an interactive chatbot that allows users to select their Hogwarts house from a list of options retrieved via an API call. Upon selecting their house, users will proceed through a tailored conversation flow based on their choice.

![]()

Implementation steps:

- **API Integration:**

- Integrate an API call to retrieve the names of Hogwarts houses.
- Upon receiving the API response, extract the house names and store them as an array in button_options.

![]()

- The configuration of the fetch_url function will vary for each API depending on its specific endpoints and the expected output format. For this example, we utilized the publicly available [Wizard Words API](). When integrating different APIs into your chatbot project, ensure that the fetch_url function is tailored to the API's requirements and response structure to retrieve the desired data effectively.
- Based on the API call output, set the button_options variable to store the array or our button menu options. Store individual individual options in separate variables as well.

![]()
- **Button Menu Implementation:**

- Implement the button menu functionality in the ANS node.
- Create an intent, and select Use also as a chat button. Select Set buttons from a variable, and select button_options (or the name variable where you store your prepared array).
- **Intent Recognition:**

- Set up intent recognition to identify the user's selection from the button menu.
- In the example project, we used conditions to compare input utterance and button option variable value.




![]()
- **Chatbot Flow Configuration:**

- Configure the flow of the chatbot to handle user interactions after house selection.
- Upon the user selecting a house, store the chosen house as a variable for further use in the conversation flow.
- Design a tailored conversation flow based on the user's chosen house, providing personalized responses and prompts.
- **Generative AI Interaction:**

- Integrate generative AI capabilities to engage users in conversation based on their selected house.
- Utilize prompts and instructions within the conversation flow to guide the user through interactive dialogues with the chatbot.

![]()

Check it out for yourself. Download the example project below and import it to your project in Digital studio!

Here are some ideas for more use cases for API-driven button menus:

1. Personalized Product Recommendations: Showcasing personalized product recommendations based on user preferences, browsing history, or past purchases.
2. Recent Order History: Providing users with quick access to their recent order history, allowing them to easily reorder items or track their deliveries.
3. Subscription Management: Allowing users to manage their subscriptions by presenting options to upgrade, downgrade, or modify their subscription plans directly from the chat interface.
4. Service Selection: Offering users a selection of available services or features tailored to their account type or subscription level.
5. Tariff Selection: Presenting users with a choice of tariffs or pricing plans based on their usage patterns, geographic location, or other relevant factors.
6. Location-Based Services: Enabling users to select delivery addresses, pickup locations, or service areas based on their current location or saved preferences.



## Buttons from a variable with AI-generated values

In this approach, we leverage the generative AI within the [AI node](../digital-agent/conversation-flow/nodes-explained/ai-node.md) to dynamically generate button labels based on user input. The generative AI can generate button labels autonomously, either solely based on the [prompt](../for-advanced-users/prompting-cookbook.md) or with the assistance of a [knowledge base](../digital-agent/advanced-functions/knowledge-base.md). The output generated by the AI is processed in the background, and a variable containing the generated buttons is prepared.

Subsequently, we implement these dynamically generated buttons into the ANS node (Answer node), where they are displayed to the user. From there, we proceed according to the conversational design tailored to our project, including intent recognition, handling various flow scenarios, and more.


**Generating button options with AI (and knowledge base)**

- In the AI node, craft a prompt with instructions for generating the buttons. Within the prompt, instruct the AI to generate a response in the form of a dictionary. Predefine the structure and keys, indicating to the AI that it only needs to populate the values.

```
You're are a smart assistant. Based on user's input, your task is to find exactly 3 most similar topics in ask_knowledge base function. Provide only topics name in form of a string. Respond with a dict and only fill in the blank values to the predetermined keys. Output must look like this:{    "1": "",    "2": "",    "3": ""}
```

**Processing AI output into button variable**

- In your flow, connect the AI node generating buttons to a new FNC node.
- In this FNC node, first, create a variable to store AI node output. Name it for example generated_dict.  Output from generative AI is always in the form of a dict logged on the backend. To store generative AI output as value to your new variable, use this syntax:

```python
gpt_response["response_text"]
```

- Second, let's transform the string saved in generated_dict into JSON object that can be further processed using Python syntax. Create a new variable. Name it, for example json_dict. Use json.loads method with this syntax:

```python
json.loads(generated_buttons)
```

- Now the dict generated with AI is stored as JSON object in json_dict variable. Next, let's store values from the dict into individual variables for each button. Create new variable and name it, for example button_1. Use Python syntax to reference the key which value you want to extract into new variable.

```
json_dict["1"]#From dictionary stored in json_dict, save the value under the key "1" to the button_1 variable.
```

- Similarly, repeat the process to create individual variables for each button of generated dictionary.

```python
json_dict["2"]
```

```python
json_dict["3"]
```

- Finally, let's arrange our button into an array. Create a new variable and name it, for example, button_options. This variable will be used in ANS node to set the button menu. Set an array of individual button variables as it value.

```python
[button_1, button_2, button_3]
```

- Optionally, if you want to add other buttons with statuc values, add them to the array as a string.

```python
[button_1, button_2, button_3, "Back to main menu", "Skip"]
```

### Implementing buttons from the variable into ANS node

- Implement the dynamically generated buttons into the ANS (Answer) node. Create an intent with the chatbot button  configuration enabled and select Configure buttons from variable. Set the button_options variable as a source for your menu options.
- Proceed with the conversational design based on your project's requirements. Configure intent recognition, handle various flow scenarios and ensure seamless interaction with the user.

### Example project

In this project, our chatbot assists trainers who have forgotten the name of a Pokémon but remember its description. The bot uses the trainer's description as input for a generative AI, which generates three suggestions for the Pokémon's identity. We then process the AI's output in the background, storing it in variables. These variables are then implemented as button options, allowing the user to select from the suggested Pokémon.

![]()

Implementation steps:

- User Input: The trainer describes the Pokémon they're trying to identify (ANS node)
- Generative AI Response: Using the trainer's description, the generative AI generates three suggestions for the Pokémon's identity.

```
Be brief in your answers. Help the user identify a pokémon. The user describes to you what the pokémon looks like. Your task is to provide exactly 3 options of pokémon names that fit that description. Respond only with a dict with pokémon names as string values for keys pokemon_1, pokemon_2 and pokemon_3 (fill in the blank values). Output must look like this:{"pokemon"_1: "","pokemon"_2: "","pokemon_3": ""}
```

- Background Processing: We process the AI-generated suggestions in the background, storing them in variables.

- First, we stored the generative AI output into generated_pokemons variable. Then we transformed it into JSON object and stored that into pokemons variable.
- Next, the extracted values from JSON dictionary  in pokemons to individual variables pokemon_1, pokemon_2 and pokemon_3.
- Finally, we created an array of the individual pokemon variables and store them in into button_options variable.




![]()
- Implement as Buttons: The stored suggestions are implemented as button options in the chat interface. The user can now choose from the suggested Pokémon.

![]()

- User Selection: The user selects one of the suggested Pokémon by clicking on the corresponding button.
- Further Interaction: Upon selection, the chatbot proceeds to another node where the generative AI generates detailed information about the selected Pokémon, helping the trainer with their query.

Check it out for yourself. Download the example project below and import it to your project in Digital studio!

## Buttons from a variable generated by AI with varying options count

Dynamic button generation can occur through prompts alone or with the assistance of a knowledge base, potentially resulting in a fluctuating number of buttons. When generating buttons solely from prompts, the count may vary based on the context provided. 

Similarly, leveraging a knowledge base alongside prompts introduces the possibility of returning differing quantities of relevant results. This section delves into managing variable button counts, considering both prompt-based and knowledge base-driven scenarios, and adapting to the evolving context of the conversation.

Generating button options with AI (and knowledge base)
The implementation [process]() remains consistent with generating a fixed number of buttons. We compose a prompt outlining instructions for generating button suggestions.

- What is different, is specifying both the minimum and maximum number of suggestions desired.
- Additionally, we define the output structure and provide an example of how the dictionary should be formatted.
- To facilitate dynamic button counts, we augment the dictionary by including a "result" key with an instruction for the generative AI to populate it with the count of previously filled keys. This count indicates the number of buttons generated, offering flexibility in accommodating varying counts based on the context.

```
You are a smart assistant. Based on the user's input, your task is to find 3  to 5 most similar topics in ask_knowledge base function. Provide only topic names in the form of a string. Respond with a dict and only fill in the blank values to the predetermined keys. You must fill minimum 3, but maximum 5 keys with topics. In case of filling out less that 5, leave "" in the key value. Also, always fill in the "key" result with number of previously filled keys. Output must look like this:{    "1": "",    "2": "",    "3": "",    "4": "",    "5": "",    "result": ""}
```

### Processing AI output into buttons variable

The next step in processing the AI output remains unchanged. We store the output in a variable, convert it into a JSON object, and unpack the individual values from the dictionary in the JSON object into separate variables.

- The key difference lies in introducing a fork in the flow using a DEC node based on the value in the "result" key. This directs the flow to a point where we prepare and store a variable with an array of buttons with the desired count. Eg. variable button_options with array [button_1, button_2, button_3, button_4] if the number of results from generative AI was 4.

![]()

> **INFO:** Note!
It's crucial to ensure that the array in the variable defining the button menu does not contain empty variables or empty strings. Otherwise, the button menu would not render on the front-end of the chat bubble.

**Subsequent steps**

The subsequent steps, such as i[mplementing buttons in the ANS node](), intent recognition, and setting up further flow, remain the same.

**Example project**

In this example project, we leverage generative AI to generate 3-5 Pokémon options based on the user's description. The user's input description is processed by the generative AI to generate 3-5 Pokémon options that match the description. 

![]()

Behind the scenes, we process the AI output and create a fork in the flow based on the number of generated options. We then save separate arrays for 3, 4, or 5 Pokémon options. The chatbot displays 3-5 buttons, each corresponding to a Pokémon option, allowing the user to select their desired Pokémon. Upon clicking a button corresponding to a Pokémon, the generative AI provides information about that Pokémon, offering details or characteristics. 

This project demonstrates how dynamic button generation based on generative AI output can enhance user interaction and provide personalized responses in a chatbot environment.

```
Be brief in your answers. Help the user identify a pokémon. The user describes to you what the pokémon looks like. Your task is to provide 3 to 5 options of pokémon names that fit that description. Respond only with a dict pokémon names as string values for keys pokemon_1, pokemon_2 and pokemon_3, pokemon_4 and pokemon_5. (fill in the blank values).  You must fill at least 3 pokemon keys. If you fill in less than 5, leave the value of the others "". In the key "result" fill in a number of how many pokémon keys you have filled. Output must look like this:{"pokemon"_1: "","pokemon"_2: "","pokemon_3": "","pokemon_4": "", "pokemon_5": "","result": ""}
```

- Background Processing: In subsequent [DEC node](../digital-agent/conversation-flow/nodes-explained/decision-node.md), we process the AI-generated suggestions in the background, storing them in variables.

- First, we stored the generative AI output into generated_pokemons variable. Then we transformed it into JSON object and stored that into pokemons variable.
- `Next, the extracted values from JSON dictionary  in pokemons are stored to individual variables pokemon_1, pokemon_2,pokemon_3,pokemon_4 and pokemon_5`
- Also, a value from the key result is stored into an individual variable of the same name.
- Then, we created a fork in the flow based on the number of generated options.
- ![]()
- `Each branch leads to a FNC node, where button_options is set with the appropriate number of objects in an array [pokémon_1, pokémon_2, pokémon_3], or  [pokémon_1, pokémon_2, pokémon_3, pokémon_4], or [pokémon_1, pokémon_2, pokémon_3, pokémon_4, pokémon_5]`




![]()
- Implement as Buttons: The stored suggestions are implemented as button options in the chat interface. The user can now choose from the suggested Pokémon.

![]()

- User Selection: The user selects one of the suggested Pokémon by clicking on the corresponding button.
- Further Interaction: Upon selection, the chatbot proceeds to another node where the generative AI generates detailed information about the selected Pokémon, helping the trainer with their query.

Check it out for yourself. Download the example project below and import it to your project in Digital studio!
