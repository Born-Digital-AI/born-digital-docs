# Step 5. - Finalizing the Project

Our last step involves defining the concluding logic for the successful Virtual Assistant we've built.

Let's establish a simple TRUE/FALSE logic based on the customer's response to showcase a basic logic example in your application:

- "YES" intent loops back to the generative AI node.
- "NO" intent leads to ending the conversation.

> **WARNING:** Make sure you have properly setup the hangup (when the user is still on the call) and fallback (backing scenario)

![]()

****

> **INFO:** You can create an infinite loop by arranging 'yes/no' questions to return to the same node (avoiding the call end).
