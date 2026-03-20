# MESSAGE node

Use Message node when you want to tell something to the customer.

This node is a basic element within the [Conversation Flow](../digital-agent/conversation-flow.md), facilitating communication between your digital agent and the customer. It serves various purposes such as:

- posing questions
- providing guidance
- offering information

Within ['Message' nodes](../digital-agent/conversation-flow/nodes-explained/message-node.md), you have the flexibility to add, delete, or edit multiple text or voice blocks. Each block is considered as one "chat bubble" in case of chat conversation.

Incorporate basic text or utilise variables, for dynamic content. Just start typing with curly brackets {} and variable names will be suggested to you. During the actual conversation, content of the variable is read to the customer.

> **INFO:** To enable using various visuals for chat conversations, we support Markdown language. Check out  in Tips & Tricks chapter for a detailed guide to all the formatting wizardry.

> **INFO:** To enable intonations for voice conversations, we support SSML language. You can find more about intonations in  section.

You can use your project as either chat or voice conversation or both. That's why you can define either Text or Speech content within the Message node. In case you define just one of them, other channel use the same content.

![]()

---

## Variables

The variables section can be found in all node types, since it can be used for various purposes based on the goal you need to achieve. Within the Message node, variables are used to track the progress or status of the conversation. To input a string value to the variable, just use "" quotes such as "Invoice explained" as the value of the variable.

---

## Use Announcement Feature: 

With announcements, you can create placeholders within your conversation flow. When an announcement is active (configured on the workspace tab for each project), the designated message will automatically be played at that point in the flow. This can be used for various use cases, such as informing customers about service availability issues, other technical issues, or any other emergency or time specific information. Announcements can be also scheduled. 

> **INFO:** For voice conversations, the announcement message is played to the customer as it is defined in the Announcement settings on the workspace tab.

> **INFO:** For chat conversations, you can set the type of announcement in the Message node, supporting modal type or toast type of announcement.

---

## Advanced Settings: 

The Message node's advanced settings are straightforward:

- Execute after the message is played: This option is intended for voice conversations, allowing moving the conversation to the next target node only after the message is played. This is usually used in specific scenarios such as executing some time consuming back end calls in parallel and using the Message node to bridge this time with information about what is happening and moving to next node only after the time-consuming back-end call is finished. If turned off, the Conversation Flow will continue until next Answer node, where it stops to get the response from the customer.
- Use variable as target: This setting caters to advanced users, enabling dynamic setting of the next target node. If turned on, variable can be used instead of specific node name.
