# Step 4. - Managing Flow Scenarios

Let´s create a simple Flow scenario!

In this tutorial, we'll create a straightforward answer node equipped with two intents, presented as selectable options via buttons:

- YES: Represents a positive response; the customer seeks additional information or has another query.
- NO: Indicates the call will conclude immediately.

![]()

While using keywords is helpful, leveraging generative AI based on meaning can often yield better outcomes and simplify processes.

****

> **WARNING:** The sequence of intents, variables, and entities within nodes is critical. Visualize this as an SQL case function where the system progresses through ordered parameters until no matches are met. This functions as a fallback action or, in SQL terms, an "else" statement.

> **INFO:** Determine the priority flow by assigning primary colors to intents for primary objectives and secondary colors for alternate objectives.
