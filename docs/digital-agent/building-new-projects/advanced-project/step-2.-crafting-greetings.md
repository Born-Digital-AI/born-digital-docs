# Step 2. - Crafting Greetings

Following the completion of Step 1, it's time to initiate a more personalized interaction by asking the customer for their name

To extract and utilize this information effectively, the 'Answer' node will leverage the 'smart extractor' function. This function will be created within the entities panel, named "Namex" and configured as a smart function aimed at extracting the Full_name from the user's response.

Now, let's proceed to customize our message nodes by leveraging the properties extracted using "Namex":

- {Namex}: Displays all properties along with their extracted values.
- {Namex["name"]}: Reveals only the customer's Name.
- {Namex["name"]} {Namex["surname"]}: Shows both the Name and Surname of the customer.

You have the flexibility to choose the level of personalization you prefer. Remember to set our previously created 'Function' node as the target node to establish a loop within the flow.

![]()

By integrating additional function nodes and connecting them to backend operations, we can develop a more robust user authorization flow based on the principles outlined in this guide.

****

> **WARNING:** Ensure to check and adjust the language settings in your project within the Project Settings. The extractor supports names predominantly from the domestic language group. For instance, certain names like "Radovan" might not be recognized as valid names in English language settings.

> **INFO:** Entities within the 'Answer' node function similarly to variables in other nodes. They serve the purpose of extracting specific information tailored to your use case.
