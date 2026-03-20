# Step 1. - Establishing Functions

Let's dive in!

In this initial step, our aim is to create a fundamental function - a counter to track the number of times a user interacts with the function node. Utilizing this information, we'll leverage the decision node to smoothly guide our users through the Conversation Flow.

- When the Chatbot/Voicebot interacts with the user for the first time, the chatbot will initiate a query to identify the user's name.
- Subsequent interactions (beyond the first) will redirect the flow to a generative AI node designed to assist the customer.

This specific use case serves as a foundational example within this guide.

![]()

By incorporating additional function nodes and integrating backend-connected functions, we can create a user authorization flow based on the principles laid out in this simple guide.

****

> **INFO:** Function nodes are incredibly versatile. They can be utilized to track specific use case information or retrieve data from your backend system, such as current date, time, user address, or numerical values.
