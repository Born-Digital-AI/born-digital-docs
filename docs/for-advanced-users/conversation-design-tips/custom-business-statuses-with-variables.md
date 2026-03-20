# Custom business statuses with variables

Custom string variables can serve as valuable tools for reporting within Digital agent's conversations. By strategically integrating string variables to represent various points or states within the conversation scenario, you can easily track and analyze user interactions and obtain insightful reporting.

## Setting a status variable

To set a string variable in a Digital agent scenario, you need to define the variable and assign a value to it. Variables store data that can be accessed, manipulated, and updated throughout the conversation flow. Here's how it works:

1. **Define the Variable:**

Choose a descriptive name for the variable that reflects its purpose or the type of data it will store. For example, you could name a variable "topic" to represent the current conversation topic.

![]()

1. Assign a Value to the Variable:
Once the variable is defined, assign an initial value to it.
When you enclose a value in double quotes, it explicitly indicates that said value is a string. If you omit the double quotes, it implies that the value refers to another variable.

![]()

## Variable status lifecycle

In the flow editor, variables are initialized the first time a node is entered where a variable of a given name is set with an initial value. This initialization occurs within the configuration settings of Variables/Entities in the respective node. Once initialized, the variable retains its value throughout the conversation flow, unless explicitly updated or reset in subsequent nodes. Here's how it works:

1. **Variable Initialization:**

- When entering a node in the flow editor, variables can be initialized and assigned initial values within that node's configuration settings.
- These initial values serve as the starting point for the variable's lifecycle within the conversation flow.
2. **Variable Updates:**

- Each time a user interacts with the Digital agent and enters a node where the variable is present, its value can be updated.
- For example, we want to track the last message displayed/read to the user. In each MSG node, we set a variable named last_message. In the first MSG node, we set the value of this variable to be"introduction", then, in a subsequent MSG node, we set a variable of the same name with a value "open question". Going through flow, variable value will be updated from "introduction" to "open question".
3. **Variable Retention:**

- Once updated, the variable's value is retained for the remainder of the conversation unless explicitly modified/updated or reset in subsequent nodes.
4. **Node Resets and Variable Persistence:**

- In some cases, nodes may contain variable reset, effectively clearing any previous values.
- However, unless explicitly reset, variables typically maintain their values across multiple node interactions, providing continuity and context throughout the conversation flow.

> **INFO:** Setting custom variable enabled in:
 START node , MSG node, ANS node, FNC node, DEC node, END node

 AI node

Applicable for:
 chatbots, voicebots, digital human

---

---

# Applied use-cases

## Tracking last message

One applied use case of setting statuses with variables is to track the depth of the conversation and identify potential turning points where users may disengage.

**Use-Case: Tracking Conversation Depth**

- Objective: Measure user engagement and identify potential drop-off points in the conversation flow.

![]()

- **Implementation:**

- Set a string variable, such as last_message, to track the depth of the conversation by updating its value with each new message or interaction.
- In each MSG node, set a custom value to last_message, eg. "greeting" in the initial MSG node, "second question" in subsequent MSG node, ..., "goodbye" in the last MSG of the conversation etc.
- Every time a MSG node is entered, its output message is shown/read to a user as well as the last_message variable value is updated based on the setting in said node.
- Monitor the value of the last_message variable at various points in the conversation flow to determine how far users progress before potentially disengaging.
- Analyze the data collected from the variable to identify patterns and pinpoint specific questions or prompts that correlate with user drop-off rates.

**Example Insights:**

- Conversation Abandonment Rate: By analyzing the last_message variable across multiple conversations, analysts can calculate the percentage of users who abandon the conversation at different stages.
- Turning Points: Identify specific questions or prompts in the conversation flow where user engagement tends to decline, indicating potential areas for improvement or optimization.
- Optimization Opportunities: Use insights from variable tracking to refine conversation designs, adjust messaging strategies, or introduce interventions aimed at maintaining user interest and prolonging engagement.

---

## Business status based on intent recognition

Utilizing variables to assign status labels to different categories of utterances streamlines the reporting process. One such use case involves categorizing user responses to specific questions or prompts and aggregating them for reporting purposes.

**Use-Case: Grouping User Utterances**

- Objective: Categorize user responses to specific questions or prompts and aggregate them for reporting purposes.

![]()

**Implementation:**

- Set an ANS node and define intents for intent recognition. As a next step, prepare nodes for statuses and their values to be set, for example, a FNC node.
- In both FNC nodes, set a string variable, such as business_status to track the user's interest level. Set the variable value as "interested" in of the FNC nodes and as "not intersted" in the other.
- Utilize intent recognition in ANS node to identify different categories of user utterances. Group the intents by setting their target accordingly to desired status.
- `Direct user utterances corresponding to the "interested" category to a common target node where the business_status variable is set to the value "interested."`
- `Direct user utterances corresponding to the "not interested" category to the other common target node where the variable business_status is set to the value "not interested."`

**Example Insights:**

- Interest Level Analysis: By aggregating user responses categorized as "interested" or "not interested" for the product or service, calculate the percentage of users expressing interest and identify trends over time.
- Effectiveness of Messaging: Analyze the effectiveness of messaging strategies by comparing the conversion rates of users categorized as "interested" versus "not interested" and adjusting marketing tactics accordingly.
- Product Development: Use insights from user interest levels to inform product development decisions, such as prioritizing features or launching targeted promotions to capitalize on areas of high interest.

---

## **Topics status in open question based on intent recognition**

This approach proves particularly valuable in scenarios where open-ended questions yield a diverse range of intent categories that can be consolidated into broader topics.

**Use-Case: Categorizing User Requests into Topics**

- Objective: Group user requests into topics to streamline reporting, identify common themes, and drive process improvements.

![]()

- **Implementation:**

- Define a set of topics representing overarching themes or categories relevant to user requests. For example, topics could include "invoice," "product info," "reclamation", "other" etc.
- *Utilize intent recognition to identify specific user intents within the broader question, How can I help you?*
- Group and map each identified intent to its corresponding topic.
- Insert to variable status to the target node of each intent, or create a designed node just for setting the status variable before continuing to the next step.
- Set a string variable, such as topic, to track the topic of each user request by updating its value based on the recognized intent category and flow path.
- Set the value of the variable accordingly. For example, if all intents concerning invoices lead to MSG_INVOICE_INFO, set a value "invoice" to the variable topic there. Don't forget to prepare a node with variable topic and value "other" for fallbacks.
- Aggregate user requests by topic for reporting and analysis purposes, allowing businesses to identify the most requested topics and prioritize areas for improvement or automation.

**Example Insights:**

- Top-Requested Topics: Analyze the distribution of user requests across different topics to identify the most commonly sought-after assistance areas.
- Process Improvement Opportunities: Use insights from topic-based reporting to streamline processes, allocate resources effectively, and address recurring issues or pain points.
- Automation Potential: Identify topics with high request volumes that lend themselves to automation, enabling businesses to automate responses or tasks to improve efficiency and enhance the user experience.

---

## Counter of AI generated answers in looping conversation flows

In looping conversation flows, where interactions follow a repetitive pattern, it is often handly to know the number of completed loops. One such use-case involves using a smart function counter to track the number of completed cycles in a looping conversation flow and derive insights for conversational design optimization.

**Use-Case: Tracking Conversation Cycles with a Counter Function**

- Objective: Monitor the number of completed cycles in a looping conversation flow to gauge user engagement and identify potential disengagement points.

![]()

- **Implementation:**

- Integrate a counter function into the flow diagram to dynamically track the number of completed cycles.
- Place the counter function in a FNC node positioned after the completion of each interaction cycle in the conversation flow, right after the AI node, where the answer to the user's query is generated.

![]()

- The smart function counter increments its value by +1 each time the node with the counter function is entered, indicating the completion of an interaction cycle.
- Store the counter's value in a variable, such as generated_answers_counter, allowing for easy access and reporting of cycle counts throughout the conversation.

**Example Insights:**

- Engagement Metrics: Analyze the number of completed conversation cycles to assess overall user engagement levels and interaction frequency.
- Disengagement Points: Identify trends or patterns in cycle counts to pinpoint potential disengagement points where users may lose interest or abandon the conversation.
- Conversational Design Optimization: Utilize insights from cycle tracking to inform conversational design decisions, such as adjusting messaging strategies, introducing new prompts, or offering channel switches after a certain number of cycles.

---

## **Status for Customer hanging-up in voice conversations**

By setting custom statuses to differentiate between user-initiated hang-ups and scenario-completion events, gather valuable insights for reporting and analysis. This use-case is particularly relevant for voicebot interactions where users may terminate the call abruptly, signaling the need to distinguish between voluntary and involuntary conversation endings.

Scenario: During a voice call with a voicebot, users may choose to end the conversation voluntarily by hanging up the phone, or the call may terminate unexpectedly due to external factors, such as signal loss or technical issues. Distinguishing between these scenarios allows businesses to track hang-up rates accurately and gain insights into user engagement levels.

**Use-Case: Setting Custom Statuses for Hang-Up Events**

- Objective: Differentiate between user-initiated hang-ups and scenario-completion events in voicebot conversations for reporting and analysis purposes.

![]()

- **Implementation:**

- Create a dedicated FNC node to serve as the endpoint for hang-up events in the conversation flow and another FNC node dedicated to saving status for scenario completion ending.
- Set a string variable, such as business_status, within the FNC node to capture the reason for the conversation ending.
- Use hang up routing target routing from ANS nodes to direct all hang-up events in the conversation flow to the designated FNC node for hangups, ensuring that the custom status is set before ending the flow.
- Assign different values to the business_status variable in different nodes based on the reason for the hang-up, such as "user hang-up" for voluntary terminations and "scenario completion" for successful scenario fulfillments.

**Example Insights:**

- Hang-Up Rate Statistics: Analyze the distribution of hang-up events and track hang-up rates over time to assess user engagement and identify potential pain points in the conversation flow.
- Scenario Success Metrics: Differentiate between scenario-completion events and user-initiated hang-ups to measure the success rate of conversation scenarios and identify areas for improvement.
- User Engagement Patterns: Use insights from hang-up events to understand user engagement patterns, such as the point at which users are most likely to disengage from the conversation.

> **INFO:** Hang-up statuses applicable for:
voicebots
digital human
chatbots

Hang-up signalling feature is exclusively relevant for voice-based interactions, including voicebots and digital humans, where hang-up events serve as significant indicators of conversation conclusion from the user's part.
