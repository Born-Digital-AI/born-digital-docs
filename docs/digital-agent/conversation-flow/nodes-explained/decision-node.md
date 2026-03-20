# DECISION node

The 'Decision' node serves as a valuable feature for creating branching scenarios within your Conversation Flow

In this example overview, prerequisites are established through the ['Function' node](../digital-agent/conversation-flow/nodes-explained/function-node.md) or some variable in the['Answer' node](../digital-agent/conversation-flow/nodes-explained/answer-node.md)before reaching the 'Decision' node. To witness its application, refer to the chapter [Creating Your First Virtual Assistant](../digital-agent/building-new-projects.md):

- County: Tracks the number of times the user crosses the ['Function' node](../digital-agent/conversation-flow/nodes-explained/function-node.md).
- Value: Assuming the value is set to 32, multiple scenarios are crafted based on these values to bifurcate the [Conversation Flow](../digital-agent/conversation-flow.md).

![]()

Precise conditions within the ['Decision' node](../digital-agent/conversation-flow/nodes-explained/decision-node.md) hold utmost significance. Conditions are processed sequentially, moving from the first to the last. When a condition is met, the connected target node is triggered. 

In cases where no conditions match, the ['Decision' node](../digital-agent/conversation-flow/nodes-explained/decision-node.md) resorts to the 'Other' path, similar to a fallback function seen in other nodes. Visualize it as akin to an SQL Case function (when/else logic).

> **INFO:** Consider altering the condition order based on your flow logic and priority for optimal decision-making within your [Conversation Flow](../digital-agent/conversation-flow.md)
