# Customizing smart functions output

In the realm of developing digital agents, the ability to tailor the output of smart functions is paramount. 

These [smart functions]()**, akin to miniature scripts, excel in extracting pertinent information from user utterances, be it named entities or other relevant data. However, the challenge lies in the diverse formats of these outputs, ranging from arrays and dictionaries to simple strings or integers.**

The crux of the matter arises when integrating these extracted entities into the Digital agents's dialogue or synthesized speech, where naturalness and seamlessness are imperative. Thus, leveraging Python syntax, we adeptly mold the outputs from smart functions into variables, ensuring a fluid and natural conversation flow.

**Scenarios Requiring Presentation or Vocalization of Extracted Entities:**

1. **Confirmation Queries:**

- "Did I understand correctly that your order number is {order_id}?"
- "Am I correct in assuming your interest lies in the opening hours of the branch in {city}?"
- "Have I correctly noted that your name is {full_name}?"
2. **Composing Email/SMS Texts for User Dispatch:**

- "Confirming that your order with number {order_id} will be dispatched to the address provided at {address}, under the name {full_name}."
3. **Initiating Ticket Creation for Back Office Requests.**



# Address

When dealing with a smart function for address extraction, the output manifests in the form of a dictionary, with key-value pairs representing various address components such as city, street, etc. 

Let's say we extracted the address from the user's utterance Send me the copy of the contract to Main Street 123 in Prague and stored it in a variable named extracted_address.

![]()

```
{"city": "Prague", "street": "Main Street 123"}
```

To effectively utilize this data in textual contexts, we employ simple Python syntax to parse and store these values into separate variables.

To access individual components of the address, we utilize the following syntax:

- `New variable name: street_to_read
New variable value:  extracted_address["street"]`
- `New variable name: city_to_read
New variable value: extracted_address["city"]`

Subsequently, we integrate these variables into our text, ensuring a coherent and natural flow:

*"I've noted that you reside in {city_to_read}, specifically on {street_to_read}. Is that correct?"*

![]()

**Notes:**

- If extraction of address fails, no output will be stored in extracted_address. Therefore, individual variables street_to_read and city_to_read won't be filled with values as well. Make sure MSG node, where entities are meant be be displayed/read back to user, is entered only under the condition that the address was extracted from user's utterance.
- With languages that use declination, be mindful when crafting message texts, since values in smart function output are always nomitative.
 
       Rozuměl jsem správně, že bydlíte v {city_to_read}? 
       Rozuměl jsem správně, že bydlíte v Praha? 
       Rozuměl jsem správně obec {city_to_read}? 
       Tozuměl jsem správně obec Hradec nad Moravicí? 
       Bydlíte v obci {city_to_read}? 
       Bydlíte v obci Kunčice?

---

# Advanced number

The smart function advanced_number  excels in consolidating and extracting numbers, typically returning the output as a string by default.

![]()

For a chatbot, no customization is necessary. We can seamlessly integrate the extracted number variable into the dialogue text. For example:


```
TextYour order ID is {extracted_order_id}. Is that correct?
```

![]()

However, for a voicebot, it's prudent to ensure that the number is dictated in a comprehensible manner. Dictating each digit individually and slowly allows the user ample time to verify the information.

To achieve this, we can split the order number into individual digits:

![]()

```python
", ".join(extracted_order_id)
```

This transforms "123456789" into "1, 2, 3, 4, 5, 6, 7, 8, 9.

```
Speech input:Your order ID is {order_id_digit_by_digit}. Is that correct?Speech output:Your order ID is 1, 2, 3, 4, 5, 6, 7, 8, 9. Is that correct?
```

We then utilize this variable in the speech channel to ensure that the synthetic voice reads it slowly and distinctly, enhancing user comprehension.

![]()

> **INFO:** Pro-tip!
Additionally, [SSML]() tags can be incorporated to further customize the reading speed and other aspects of the speech output.

```ssml
Your order ID is<prosody rate="-5.00%"><say-as interpret-as="spell-out"> {order_id_digit_by_digit}</say-as>.</prosody> Is that correct?
```

---

# Full name

Similar to address extraction, the output from the smart function for extracting full_name manifests as a dictionary, comprising key-value pairs representing the name and surname components.

Consider the scenario where the output from the smart function is stored in a variable named extracted_name. 

![]()

Output would look like this:

```
{"name": "John", "surname": "Doe"}
```

To access individual components of the full name, we utilize the following syntax:

- `New variable name: name_to_read
New variable value: extracted_name["name"]`
- `New variable name: surname_to_read
New variable value: extracted_name["surname"]`

![]()

Subsequently, we seamlessly integrate these variables into our text to ensure a cohesive and natural flow:

"I've noted your name as {name_to_read} {surname_to_read}. Is that correct?"


![]()

**Notes:**

- If extraction of full_name fails, no output will be stored in extracted_name. Therefore, individual variables name_to_read and surname_to_read won't be filled with values as well. Make sure MSG node, where entities are meant be be displayed/read back to user, is entered only under the condition that the full_name was extracted from user's utterance.
- With languages that use declination, be mindful when crafting message texts, since values in smart function output are always nomitative.
 Hovořím s {name_to_read} {surname_to_read}? Hovořím s Anna Nováková? 
      Jste prosím {name_to_read} {surname_to_read}? Jste prosím Petr Novotný?

---

# Phone

The smart function phone for extracting phone numbers operates by adhering to the language settings configured within the project. It returns an array containing the extracted phone number with the appropriate prefix added, based on the language setting. For instance, for utterances in Czech, Polish, German, and other languages, the format may vary accordingly.

Let's assume the output array for the utterance "Moje telefonní číslo je 123 456 789" in Czech language configuration is as follows:

![]()

```python
['+421123456789']
```

To integrate this phone number into text, we extract it from the array and store it in a separate variable:

- `New variable name: phone_to_read
New variable value: extracted_phone[0]`

![]()

Next, we use the phone_to_read variable in message text to be displayed in chat bubble or read aloud with speech synthesis.


![]()

> **INFO:** Pro-tip! 
When developing a voicebot, it's essential to utilize SSML ([Speech Synthesis Markup Language]()) tags to ensure accurate pronunciation and appropriate pacing. This is particularly crucial for reading out phone numbers, where each digit should be pronounced individually rather than as a single number (e.g., "one two three four five six seven eight nine").

Additionally, incorporating SSML tags to slow down the speech rate can enhance clarity, especially for dictation purposes.

```ssml
I have noted <prosody rate="-10.00%"><say-as interpret-as="spell-out">{phone_to_read}</say-as></prosody> as your phone number. Is that correct?
```

Notes:

- If extraction of phone fails, no output will be stored in extracted_phone. Therefore, variable phone_to_read won't be filled with a value as well. Make sure MSG node, where entities are meant to be displayed/read back to the user, is entered only under the condition that the phone was extracted from user's utterance.
- For voice channel, take your time and c[ustomize speech output]() with SSML to achieve the best result.
