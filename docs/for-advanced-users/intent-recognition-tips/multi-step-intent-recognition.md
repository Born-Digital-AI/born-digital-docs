# Multi-step intent recognition

When dealing with open-ended questions that require categorization into numerous fine-grained intents, it is advisable to adopt a multi-step approach and prepare a recognition tree. 

This method involves creating a tree structure consisting of [Answer nodes](../digital-agent/conversation-flow/nodes-explained/answer-node.md), where utterances are processed and intents are recognized. Due to limitations in prompt space and the complexity of categorization, it is recommended to divide the process into multiple steps.

![]()

## Multi-Step Approach

### Step 1: General Topic Recognition

In the first Answer node, focus on identifying broad topics (e.g., "invoice"). After recognizing the main topic, pass the input to the next "Answer" node. 

![]()

- Add new intent.
- Name the intent, select Generative AI type.
- Fill in the Meaning and Description prompt. For further details and tips on Generative AI intent recognition prompts, visit
- Set a target (another ANS node devoted to the intent's topic)
- Enable the reuse utterance feature within the intent configuration window, so input utterance will be reused in the next step.

### Step 2: Sub-Topic Classification

![]()

In the second "Answer" node, categorize the input into more specific sub-topics (e.g., "invoice not received," "invoice discrepancy," "payment for invoice"). Further, route the input based on the recognized sub-topic.

- Follow similar steps as in the previous ANS node.
- If you wish to add another level of recognition, enable the reuse utterance feature within the intent configuration window.
- If this level of recognition granularity is final and you wish to continue with the flow (to MSG node with answer or next question etc.), disable the reuse utterance feature. Upon encountering the next answer node in the flow, the Digital agent will stop and wait for a new user input.

### Step 3: Fine-Grained Categorization (Optional)

![]()

For even finer categorization, consider adding a third level of classification. For example, within the "change delivery" sub-topic, identify whether the change is delivery time postponement or redirecting delivery to a different address.

**Here's an example project:**

# Perks and Limitations

### Advantages of Multi-Step Approach to Intent Recognition:

1. Enhanced Precision: Breaking down the intent recognition process into multiple steps allows for more precise identification of the user's query, minimizing the risk of misinterpretation.
2. Reduced Complexity: Dealing with complex queries becomes more manageable when the process is divided into individual steps, simplifying the overall recognition task.
3. Improved Conversation Flow Management: Each step in the process is dedicated to a specific phase of the query, facilitating better management of conversation flow and directing users to relevant parts of the chatbot's script.
4. Flexibility and Scalability: The multi-step approach offers flexibility and scalability for future development. It allows for the addition of new categories or expansion of existing sub-topics without significant code complexity.
5. Ease of Debugging and Maintenance: Simplified and systematic intent recognition makes debugging and maintenance of the chatbot system easier, even as the complexity of scenarios increases.
6. Enhanced User Experience: Overall, this approach leads to a better user experience. Users feel that the chatbot can better understand their queries and provide relevant and timely responses.

### Disadvantages of Multi-Step Approach to Intent Recognition:

1. Increased Development Time: Implementing a multi-step approach may require more development time initially due to the need to design and integrate the recognition process into the chatbot system.
2. Potential for Overhead: The multi-step approach may introduce additional processing overhead, especially if the recognition process involves multiple layers of classification or extensive branching logic, leading to increased processing time and latency between obtaining user input and provided Digital agent's output.
3. Risk of Overfitting: Over-segmentation of the recognition process into too many steps could lead to overfitting, where the system becomes overly specialized and less adaptable to variations in user queries.
4. Complexity for Novice Users: Novice users or developers may find it challenging to understand and implement the multi-step approach, especially if they lack experience in natural language processing or chatbot development.
5. Dependency on Training Data: The effectiveness of the multi-step approach relies heavily on the quality and diversity of the training data used to train the intent recognition models at each step.
6. Potential for Error Propagation: Errors or misclassifications in one step of the process may propagate to subsequent steps, leading to inaccurate responses or user frustration.

> **INFO:** **Note!**

The multi-step approach to intent recognition can be effectively utilized for both voicebots and chatbots.

However, when implementing this approach for **voicebots, designers should consider that using Generative AI for intent recognition inherently introduces a latency of approximately half a second to a second per node. Chaining multiple steps in the recognition process can further extend the processing time, potentially impacting the user experience.**

Designers should be mindful of this latency and its potential impact on user satisfaction, especially in voice interactions where users expect immediate responses.
