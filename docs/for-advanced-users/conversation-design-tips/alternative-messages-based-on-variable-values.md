# Alternative messages based on variable values

In this guide, we will demonstrate how to create a conversational design in the Digital Studio flow editor that enables a chatbot or voicebot to deliver variable messages based on the value of a specific variable. This approach is similar to utilizing a randomization method (see ), but instead, it will be driven by a different variable, commonly a string.

 Implementing a variable-based conversational design in your chatbot or voicebot brings several advantages:

- Tailored Responses: By using variables, the bot can provide personalized responses based on user data, such as their name, preferences, or past interactions. This makes the conversation feel more human and engaging.
- Enhanced User Experience: Personalized interactions make users feel valued and understood, improving their overall experience with your service.
- Positive Brand Perception: A bot that remembers user preferences and adapts its responses accordingly can significantly enhance the perception of your brand as being attentive and customer-focused.
- Leveraging User Data: By integrating with your CRM or other data sources, the bot can leverage user data to provide contextually relevant responses, improving the relevance and accuracy of the information provided.
- Adaptability: The design can be easily adapted for different languages, regions, or user demographics, allowing for a more inclusive approach to customer interaction.

---

# Method #1: Fork the path for the next MSG node 

By following this guide, you can create a dynamic conversational experience in the Digital Studio flow editor where the chatbot or voicebot delivers tailored messages based on the value of a specific variable.

![]()

## Step 1: Define the variable

Before you can create decision points based on a variable, you need to define and populate the variable that will be used.

1. Define the Variable:

- Ensure that the variable you intend to use (e.g., my_variable) is defined within your system or flow context. This can typically be done in the Variables/Entities section in one of the previous nodes in the flow.
2. Populate the Variable:

- Make sure that the variable is assigned an appropriate value at some point before the decision node is reached. This can be done through user input, an API call, or predefined logic within the flow.

![]()

## **Step 2: Define the point of decision with DEC node**

Next, we need to create a decision point that evaluates the variable's value and routes the conversation accordingly.

1. Add a Decision Node: Drag and drop the DECISION node onto the canvas.
2. Configure the Decision Node:

- Name: Give the decision node a meaningful name, such as DEC_CHECK_VARIABLE_VALUE.
- Conditions: Define the condition based on your variable. For example, if your variable is named my_variable and you want to check for three possible values ("aaa", "bbb", "ccc"), your conditions would be:

- `my_variable == "aaa"`
- `my_variable == "bbb"`
- `my_variable == "ccc"
`

![]()

## **Step 3: Create message variants**

Now, define the messages that will be delivered based on the variable's value.

1. Add Message Nodes: Create separate message nodes with messages corresponding to scenario for each of the possible values, eg. MSG_VARIANT_A, MSG_VARIANT_B, and MSG_VARIANT_C.
2. Link Conditions to Messages:

- For the condition my_variable == "aaa", draw a connection from the DEC_CHECK_VARIABLE_VALUE node to the MSG_VARIANT_A node.
- For the condition my_variable == "bbb", draw a connection from the DEC_CHECK_VARIABLE_VALUE node to the MSG_VARIANT_B node.
- For the condition  my_variable == "ccc", draw a connection from the DEC_CHECK_VARIABLE_VALUE node to the MSG_VARIANT_C node.
- Don't forget to set a fallback target in Other to ensure flow will have a path to continue in case the variable value is missing or the variable is populated with an unexpected value.

![]()

---

# Method #2: Set the Message Content with Variables

This method involves configuring the content of message nodes as variables. The content is set based on the value of a variable, typically a string. This method simplifies the flow by reducing the number of nodes but requires more advanced configuration.

![]()

## **Step 1: Define and populate the variable**

1. Define the Variable:

- Similar to the first method, ensure that the variable you want to use (e.g., my_variable) is defined within your system.
2. Populate the Variable:

- Assign a value to the variable based on your logic (e.g., user input, API response, hard-coded value etc.).

## **Step 2: Set a new variable for the message content**

![]()

1. Create a New Variable:

- In the message node, create a new variable to store the message content. Name it message_content.
2. Assign Conditional Content:

- Use conditional statements to set the value of message_content based on my_variable. For example:

```python
"This is variant A" if my_variable == "aaa" else "This is variant B" if my_variable == "bbb" else "This is variant C"
```

## **Step 3: Use the variable in the Message node**

![]()

1. Set the Message Content:

- Use the message_content variable as the input for the message node. This allows the message content to be dynamically populated based on the variable value.
2. Assign the Variable to the Node:

- In the message node configuration, set the content to the message_content variable. Use variable placeholder in the field for text output.

## Step 4: Repeat the process to set separate variable for Speech channel

When designing conversational flows, it's important to distinguish between content intended for text chat and content intended for speech synthesis. Using a single variable to handle both text and speech can lead to displaying SSML tags in the chat interface, which can be visually unappealing and hinder readability. To avoid this, it is recommended to use separate variables for chat and speech content.

![]()

1. Define Variables for Chat and Speech:

- Create two variables, one for chat content and one for speech content.
- `Example: message_content, speech_content`
2. Set the Value for Chat Content:

- Define the message content for the chat interface, ensuring it is free of SSML tags.
- Example:

```python
"This is variant A" if my_variable == "aaa" else "This is variant B" if my_variable == "bbb" else "This is variant C"
```
3. Set the Value for Speech Content:

- Define the message content for speech synthesis, including necessary SSML tags.
- Example:

```python
"This is variant A <break time=\"10ms\"/>" if my_variable == "aaa" else "This is variant B <break time=\"10ms\"/>" if my_variable == "bbb" else "This is variant C <break time=\"10ms\"/>"
```

**Step 3: Use Variables in Appropriate Nodes**

1. Assign Chat Content to Text field i:

- Use the message_content variable placeholder in text message nodes intended for the chat interface.
2. Assign Speech Content to Speech field:

- Use the speech_content variable placeholder in speech message nodes intended for voice synthesis.

> **WARNING:** **Note! **
When utilizing SSML ([Speech Synthesis Markup Language]()) tags to modify speech synthesis in your voicebot or digital human, it's crucial to pay attention to the syntax of conditional statements. SSML tags, such as <break time="10ms"/>, contain double quotes. These double quotes can conflict with the double quotes used to delimit strings in your conditional statements for setting variable values.

`**To avoid this conflict, you need to escape the double quotes within the SSML tags. Here’s the corrected version of the example:
"This is variant A <break time=\"10ms\"/>" if my_variable == "aaa" else "This is variant B <break time=\"10ms\"/>" if my_variable == "bbb" else "This is variant C <break time=\"10ms\"/>"**`



### Step-by-Step Correction

1. Identify SSML Tags: Locate the SSML tags within your conditional statements.
2. Escape Double Quotes: Add a backslash (\) before each double quote within the SSML tags.
3. Ensure Consistency: Verify that all SSML tags within your conditional statements follow this format.

### Example

Here’s a step-by-step example:

1. Original Statement with Conflict:

```python
"This is variant A <break time = "10ms"/>" if my_variable == "aaa" else "This is variant B <break time = "10ms"/>" if my_variable == "bbb" else "This is variant C <break time = "10ms"/>"
```
2. Corrected Statement:

```python
"This is variant A <break time=\"10ms\"/>" if my_variable == "aaa" else "This is variant B <break time=\"10ms\"/>" if my_variable == "bbb" else "This is variant C <break time=\"10ms\"/>"
```

---

# Use-cases ideas

****

****

****
