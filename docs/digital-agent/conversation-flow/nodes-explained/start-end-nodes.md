# START / END nodes

Defining the starting and ending points within your conversational flow is crucial for the successful implementation of your project's logic.

Without them, errors may occur in the code editor, hindering the training process.

![]()

- Starting Node: This is the initial node visible when starting a new blank project. Quite straightforward, this node serves as the entry point for conversations with your chatbot or voicebot. Creating a message node after the start automatically generates a target node associated with it.
- End Node: In a brief explanation, the end node functions as a fallback mechanism. For instance, when the customer doesn't respond with a "yes," it triggers the end of the conversation. This example illustrates a simple usage and flow towards the conclusion. Multiple end nodes can be established to conclude conversation logic as needed.

> **INFO:** To create an['End node'](), you can simply drag it from the nodes panel located on the right side of the interface. It's important to note that within a project, there is only one starting node, which acts as the singular point of conversation initiation.
