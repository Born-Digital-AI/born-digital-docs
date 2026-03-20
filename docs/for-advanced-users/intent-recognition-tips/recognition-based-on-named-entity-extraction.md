# Recognition based on named entity extraction

In conversational design, named entity extraction is typically utilized in scenarios where specific information needs to be obtained, such as numbers (age, amount, order number), special codes (ID numbers, license plate numbers), addresses, names (of individuals, cities, streets), and similar entities.

### **Understanding Named Entities**

Named entities, often referred to as entities, are specific objects, individuals, dates, quantities, or other types of information that are recognizable and distinct within a given context. In the realm of conversational AI, named entities serve as key components for understanding user input and providing relevant responses. 

These entities can range from simple entities like dates and numbers to more complex ones such as addresses, names, and custom-defined entities tailored to specific use cases. The extraction of named entities from user utterances enables the system to comprehend the user's intent more accurately, facilitating smoother interactions and personalized responses.

- When designing a flow that involves entity extraction, it's crucial to ensure that the extraction process is properly set up. See
- Additionally, actions need to be defined based on the output of the extraction for further flow control. This includes determining what should happen if an entity is successfully extracted from the user's utterance, as well as handling cases where extraction fails or requires validation. See
- Furthermore, it's essential to anticipate and prepare for various user responses, such as if the user claims not to know or remember the requested information or requests additional time to provide it. Therefore, the design must include intent recognition and processes to address these potential objections and handle user interactions smoothly.



## Set Named Entity Extraction with Smart Functions

On our platform, named entity extraction is facilitated by what smart functions. These functions take user utterances as input (unless otherwise specified) and utilize language models or regex-based rules to identify and extract entities within the utterance. Upon successful extraction, the smart function returns an object containing the extracted entity in a predefined format.

![]()

****

> **INFO:** In this documentation section, we won't cover the details of individual smart functions and their parameters. For specifics, please refer to the dedicated documentation on smart functions.



# Configure flow based on extraction output

After setting up a smart function and storing its output in a variable, the next step is to configure actions within the ANS node based on the extraction results.

## Single extraction get condition

A common and straightforward application is to check whether an entity has been successfully extracted and proceed to the next step accordingly in the flow.

To achieve this, we can utilize intent definition using conditions within the ANS node. In the condition field, we specify conditions using the get method, for a variable name we set for storing smart function output in the previous step, and set the target destination to move the flow if the condition is met.

![]()

****

```python
get("extracted_entity")# Replace "extracted_entity" with the name of your variable for storing smart function output# If fulfilled, entity was extracted and flow continues to target state set alongside this condition
```

If the condition is not met, the system proceeds to check other conditions in the configuration. If no other conditions apply, it moves to intent recognition.

This setup allows for flexible and dynamic flow control based on the results of entity extraction, ensuring smooth interaction within the conversational flow.

## Multiple extractions getconditions

In scenarios where multiple entities need to be extracted, such as extracting both a name and a phone number within one node, it's essential to configure multiple variables to store the extraction results separately.

For example, let's set up two variables: extracted_phone to store the result from the phone smart function and extracted_fullname to store the result from the full_name extractor.

![]()

Within the conversational design, we need to set up at least three conditions:

1. get("extracted_phone") and get("extracted_fullname"): Define a target destination to move the flow if both entities are extracted successfully.
2. get("extracted_phone") and not get("extracted_fullname"): Define a target destination to move the flow if only the phone number is extracted, but not the name. For example, direct the flow to a sub-scenario where only the name is asked.
3. get("extracted_fullname") and not get("extracted_phone"): Define a target destination to move the flow if only the name is extracted, but not the phone number. For example, direct the flow to a sub-scenario where only the phone number is asked.

If none of these conditions are met, it indicates that neither entity was extracted, likely because they were not present in the utterance. In such cases, the system should proceed to intent recognition, and it's necessary to prepare intents for expected scenarios.

```python
# Both extracted:get("extracted_entity_A") and get("extracted_entity_B")# If fulfilled, both named entities were extracted and flow continues to the target state set alongside this condition# Only one extracted:get("extracted_entity_A") and not get("extracted_entity_B")# If fulfilled, one entity_A was extracted, but the entity_B is missing and flow continues to the target state set alongside this condition# None extracted:not get("extracted_entity_A") and not get("extracted_entity_B")#If fulfilled, none of entities was extracted and the flow continues to the target state set alongside this condition
```

## Conditions based on extracted values

In some cases, controlling the flow based solely on whether an entity was extracted might not suffice. We may also need to consider specific properties or values of the extracted entity. Let's illustrate this with examples:

### Conditions based on extracted integer values

Suppose we're asking for the age and extracting a number. We need to verify that we've extracted a number and that its value makes sense (not unreasonably high or low). Additionally, we want to have different conversation paths for minors, adults, and seniors.

Let's say we extract the age using the simple number smart function and store the result in the variable extracted_age. Here are the conditions:

![]()

1. **Condition for Minors:**

- `get("extracted_age") and int(extracted_age) < 18`
- If the extracted number represents a minor's age, redirect to a sub-scenario prepared for minors.
2. **Condition for Unlikely Age Values:**

- `get("extracted_age") and int(extracted_age) > 100`
- If the extracted age is unusually high (over 100), redirect to a sub-scenario addressing this situation.
3. **Condition for Seniors:**

- `get("extracted_age") and int(extracted_age) > 64`
- If the extracted age is 65 or older, redirect to a sub-scenario for seniors. This condition covers ages from 65 to 100, inclusive.
4. **Condition for Adults:**

- `get("extracted_age") and extracted_age > 17 and extracted_age < 65`
- If the extracted age is between 18 and 64, redirect to the next node in the adult sub-scenario.

If none of these conditions are met, it indicates that the age was not extracted, likely because it wasn't present in the user's utterance. In such cases, the process proceeds to intent recognition to understand the user's input, or it may fall back to a default response.

```python
# Int value is equal:get("extracted_entity") and int(extracted_entity) == 10 # or another value# Int value is greater or equal:get("extracted_entity") and int(extracted_entity) >= 10 # or another value# Int value is greater:get("extracted_entity") and int(extracted_entity) > 10 # or another value# Int value is lesser or equal:get("extracted_entity") and int(extracted_entity) <= 10 # or another value# Int value is lesser:get("extracted_entity") and int(extracted_entity) < 10 # or another value# Int value within open intervalget("extracted_entity") and int(extracted_entity) > 0 and int(extracted_entity) < 10 # or other values# Int value within closed intervalget("extracted_entity") and int(extracted_entity) >= 0 and int(extracted_entity) <= 10 # or other values
```

### Conditions based on extracted string length

Similarly, we can apply conditional logic based on the properties of numeric strings, where the focus is on the string's value rather than its integer interpretation. Let's consider an example where we use the advance number smart function to extract an order number, and we store the result in the variable extracted_order_id.

Let's say that in our example case, valid order numbers typically range from 8 to 12 digits. We've configured the smart function to extract numbers with a length of at least 8 and at most 12 digits. 

![]()

Let's say that the length of the order ID string determines the type of customer (corporate or personal) and eventually a product (fridges, washing machines and smartphones). For further flow control, we need to distinguish whether we've extracted a numeric string with a valid length and, if so, what type of order it represents.

![]()

Here are the conditions:

1. **Condition for Corporate Orders (8 or 9 digits):**

- `get("extracted_order_id") and len(extracted_order_id) < 10`
- Redirect to a sub-scenario for corporate orders.
2. **Condition for Personal Orders (10 digits):**

- `get("extracted_order_id") and len(extracted_order_id) == 10`
- Redirect to a sub-scenario for personal orders, such as those for refrigerators.
3. **Condition for Personal Orders (11 digits, e.g., Washing Machines):**

- `get("extracted_order_id") and len(extracted_order_id) == 11`
- Redirect to a sub-scenario for personal orders, such as those for washing machines.
4. **Condition for Personal Orders (12 digits, e.g., Phones):**

- `get("extracted_order_id") and len(extracted_order_id) == 12`
- Redirect to a sub-scenario for personal orders, such as those for phones.

If none of these conditions are met, it indicates that we didn't extract a numeric string with a valid length, likely because it wasn't present in the user's utterance. In such cases, the process proceeds to intent recognition, where intents should be prepared to handle predictable scenarios (e.g., the customer doesn't remember the order number, is unfamiliar with it, or has lost it).

```python
# Length equals to:get("extracted_entity") and len(str(extracted_entity)) == 10 #or other value# Length is greater or equal to:get("extracted_entity") and len(str(extracted_entity)) >= 10 #or other value# Length is greater than:get("extracted_entity") and len(str(extracted_entity)) > 10 #or other value# Length is lower or equal to:get("extracted_entity") and len(str(extracted_entity)) <= 10 #or other value# Length is lower than:get("extracted_entity") and len(str(extracted_entity)) < 10 #or other value# Length is within open interval:get("extracted_entity") and len(str(extracted_entity)) > 1 and len(str(extracted_entity)) < 10 #or other values# Length is within closed interval:get("extracted_entity") and len(str(extracted_entity)) >= 1 and len(str(extracted_entity)) <= 10 #or other values# Length is equal either to A or B:get("extracted_entity") and (len(str(extracted_entity)) == 1 or len(str(extracted_entity)) == 10) #or other values
```

### Conditions based on string values

Conditional logic can also be applied based on the extracted strings. Let's consider a scenario where we ask customers for their full name, and we want to implement special logic for customers named "Patrick" in celebration of St. Patrick's Day.

`First, we use smart function full_name to extract name and surname from user's input utterance and name the variable for storing smart function's output extracted_fullname.`

![]()

1. **Condition for Customers Named "Patrick":**

- `get("extracted_fullname") and extracted_fullname["name"] == "Patrick"`
- Redirect to a branch for St. Patrick's Day specials.
2. **Condition for Extracted Full Name:**

- `get("extracted_fullname")`
- Redirect to the branch where the flow continues upon successfully obtaining the name.

If neither of these conditions is met, it indicates that the smart function failed to extract the full name. In such cases, the process proceeds to intent recognition, where it's beneficial to have intents prepared to handle predictable scenarios. Alternatively, it may end in a fallback.

> **INFO:** It's worth noting that outputs from smart functions can be various types of objects (pure [strings](), integers, [dictionaries](), or [arrays]()). Handling the extraction of specific values from these objects is covered in another section of the documentation. See

```python
# Value is a given stringget("extracted_entity") and str(extracted_entity) == "Example string"# Value is not a give stringget("extracted_entity") and str(extracted_entity) != "Example string"
```

# Handling Various User Responses with Intent recognition

**When designing conversational interactions, it's vital to anticipate and effectively manage a wide range of user responses. **

**This encompasses various scenarios of utterances without the desired named entity present at the first place, such as users claiming unfamiliarity with or inability to recall the requested information, requesting additional time to respond, or providing ambiguous or unclear replies. **

Therefore, the design strategy must incorporate robust intent recognition capabilities and procedural frameworks to navigate through these potential challenges seamlessly. By doing so, we ensure a smoother and more user-friendly conversational experience that accommodates diverse user interactions.

![]()

For basic 101 explanations and tutorials on setting intents for intent recognition, visit  page. 

Check out the  tips and tricks page for advice on fine-tuning intent recognition prompt.

> **INFO:** Pro-tip!
Before you take off to brainstorm the variety of input you might get from your users, take time to familiarize yourself with hierarchy in the processing of different intent types during the intent recognition process.

**Order of Intent Evaluation:**

- **Conditions, Keywords, and Generative AI:**

- These are evaluated in the order they're configured in the ANS node. Ensure that conditions for directing further steps based on entity extraction are prioritized first, followed by keyword detection and Generative AI intent recognition.
- **Intent Recognition using Training Set:**

- This is evaluated last in the sequence and is reached only if previous conditions aren't met, keywords aren't captured, and Generative AI fails to recognize the intent. For further details on custom training set intent recognition, see
- **Fallbacks:**

- If none of the above conditions are satisfied, the process falls back to fallback logic as configured in ANS node. For further detail, see

**Common scenarios to cover with intents:**

****

****

****

****

****
