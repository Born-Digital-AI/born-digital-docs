# DECISION node

The 'Decision' node serves as a valuable feature for creating branching scenarios within your Conversation Flow

In this example overview, prerequisites are established through the ['Function' node]() or some variable in the['Answer' node]()before reaching the 'Decision' node. To witness its application, refer to the chapter [Creating Your First Virtual Assistant]():

- County: Tracks the number of times the user crosses the ['Function' node]().
- Value: Assuming the value is set to 32, multiple scenarios are crafted based on these values to bifurcate the [Conversation Flow]().

![]()

Precise conditions within the ['Decision' node]() hold utmost significance. Conditions are processed sequentially, moving from the first to the last. When a condition is met, the connected target node is triggered. 

In cases where no conditions match, the ['Decision' node]() resorts to the 'Other' path, similar to a fallback function seen in other nodes. Visualize it as akin to an SQL Case function (when/else logic).

> **INFO:** Consider altering the condition order based on your flow logic and priority for optimal decision-making within your [Conversation Flow]()
