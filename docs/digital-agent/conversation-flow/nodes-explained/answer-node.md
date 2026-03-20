# ANSWER node

Use Answer node when you need a response from the customer and you need to understand the intent from the response and extract some name entities.

The['Answer' node](../digital-agent/conversation-flow/nodes-explained/answer-node.md)essentially waits for and processes customer response, subsequently guiding the Conversation Flow based on these inputs. Let's delve into the foundational logic of the ['Answer' node](../digital-agent/conversation-flow/nodes-explained/answer-node.md)step-by-step.

![]()

# Entities

Entities operate similar to variables, with the purpose of extracting information from user responses. Enable Use Smart Function toggle and choose from available functions to extract entities from customer response. Each smart function may have some configuration elements to further tailor what the extracted entity should look like. 

In general, last utterance is used as an input for entity extraction, meaning that the user's last response to the digital agent is checked, and if the entity is present there, it is stored as a value of that specific variable. Use Custom input field in case you want to use anything else as an input for entity extraction (i.e. content of any other variable).

> **INFO:** Learn more about smart funcitions here -> [https://smart.borndigital.ai/]()

> **WARNING:** We will update the UX/UI of the variable dialog in near future. Stay updated!

Most commonly used entity extraction types are:

- address
- advanced_address
- advanced_number
- birth_number
- birthdate
- city
- date
- fullname
- phone
- registration_plate
- street
- simple_number
- time



---

# Intents

Intent is a meaning of what the customer said in his last utterance and thus intents enable the conversation to move further based on the context. We use 4 types how to build the intent:

****

****

****

****

We can use every intent as separated chat button with some basic configuration. Feel free to learn more in chapter - [Creating Your First Virtual Assistant](../digital-agent/building-new-projects.md)for more informations and basic use case.

> **WARNING:** Every intent has to have a target node, what I want to do with the intent of customer. 

For example: Customer wants to know more about the product, intent is recognized, continue in flow to ask for specific product name.

See the page - [STEP 4.](../digital-agent/building-new-projects/advanced-project/step-4.-managing-flow-scenarios.md) and [STEP 5.](../digital-agent/building-new-projects/advanced-project/step-5.-finalizing-the-project.md)in [Creating Your First Virtual Assitant](../digital-agent/building-new-projects.md) to see the intents in action

---

# Fallbacks

Fallback scenarios are a crucial component of the Answer node setup, as they provide fail-safe mechanisms for instances where the bot encounters challenges in processing user inputs or understanding their intents.

## Fallback triggers

Fallback occurs under the following circumstances:

- Failure to acquire input from speech-to-text (STT) conversion (applicable to voicebots and digital human only).

- NO_INPUT: This signal, pertinent only to voicebots, arises when the STT module detects silence from the user.
- NO_MATCH: Also exclusive to voicebots, this signal occurs when the STT module fails to transcribe the user's audio input into coherent words, such as in cases of background noise.
- SHUT_UP: This signal, applicable solely to voicebots, triggers when the user's speech exceeds a predefined duration, indicating a prolonged input.
- Recognition failure of user intent, resulting in no identified intent.

- NOT_UNDERSTOOD: This signal applies to both voice and chat interactions, signifying that although an utterance was received, the intent recognition process failed to understand or select any options.

Each time a fallback occurs, irrespective of its trigger, the counter increments, recording the frequency of fallbacks encountered within that specific Answer node.

You have the option to chose between the following 2 courses of action, for the situation when a fallback is triggered in the conversation:

1. Transition to another node: you may opt to direct the conversation flow to a different node within the Digital Agent's flow. This action bypasses further interaction within the current node.
2. Custom Fallback message: Alternatively, you can specify a custom fallback message to be delivered to the user. This message prompts the user to retry or rephrase their input. Following the delivery of the custom fallback message, the conversation loops back to the beginning of the Answer node, affording the user a second opportunity to engage effectively. This loop mechanism provides users with a second chance to provide input and Digital agent with a second chance to process user query successfuly.

The behavior of the fallback counter is determined by its configuration:

- Counter Set to 0: In this case, the conversation flow proceeds directly to the target node without considering the presence of a fallback message.


![]()



- Counter Set to 1: Upon the first fallback occurrence, the conversation transitions to the first custom fallback message. Subsequently, upon encountering a second fallback, the flow proceeds to the target node as the maximum fallback count has been reached.

![]()



- Counter Set to 2: The first fallback event directs the conversation to the First custom fallback message. Upon the second fallback, the flow transitions to the Repeated custom fallback message. Finally, upon encountering a third fallback, the conversation progresses to the target node, having exhausted the maximum fallback count.

![]()

- Counter Set to Higher Values: For counters set to values higher than 2, the behavior remains consistent with the previous scenarios. The conversation initially proceeds to the first custom fallback message upon the first fallback occurrence. With each subsequent fallback, the flow transitions to the repeated custom fallback message until the maximum fallback loop count specified in the counter is reached. Upon reaching this limit, the conversation proceeds to the target node.

![]()

Once the fallback repetition count reaches its limit (e.g., if the configured count is 2 and the fallback cycle occurs for the third time in a specific ANS node), the conversation flow progresses to the designated target node. 

> **INFO:** **Note! **
Fallback counter operates locally within Answer nodes. Each time the conversation falls back due to intent recognition failure, a count is incremented within that node, resetting when moving to a new node.

Example: Imagine a scenario with three nodes, each representing a question. If the fallback counter is set to 2 within each node, it means the fallback message can occur up to twice for each question. So, in total, the fallback could happen up to six times throughout the conversation, with two fallbacks per question, before transferring to an operator.

Understanding this local behavior is key for designing a smooth user journey and knowing when to transition to human assistance

> **INFO:** Note! 

If you enable reuse utterance for fallbacks in the advanced settings (for more details see ) the signal (no_input, no_match, shut_up) and empty utterance will be carried over to the next ANS node it encounters in flow and reused as input there!

> **WARNING:** Upcoming Feature: Exciting news! We're working on a feature for global fallback counting. Stay tuned for updates!

## Setting Custom Fallback messages

In ANS node modal, you have the option to customize fallback responses according to specific scenarios triggered by different signals. This customization process involves creating distinct messages for each type of signal, ensuring tailored interactions with users based on their input or lack thereof.

![]()

****

Additionally, you can skip the custom messages and set different target nodes for each type of trigger, directing the conversation flow to the next node right away, based on the nature of the input signal received.

![]()

****

> **WARNING:** **Note! **
Within chatbot flows, configuring custom fallback messages for 'NO_INPUT,' 'NO_MATCH,' and 'SHUT_UP' signals is redundant and unnecessary. These signals are specifically related to the functionality of speech-to-text conversion, which is not utilized in chat channels. Therefore, these signals never occur in a chat-based environment.

**Custom Messages Examples:**

- **NO_INPUT:**

- `First Message: "Apologies, I didn't catch that. Could you please repeat?"`
- `Repeated Message: "Sorry, I still couldn't hear you. Please try again."`
- **NO_MATCH:**

- `First Message: "I'm sorry, I couldn't understand your query. Can you provide more clarity?"`
- `Repeated Message: "It seems I'm still having trouble understanding. Could you rephrase your question?"`
- **SHUT_UP:**

- `First Message: "Could you sum that for me in a one sentence, please?"`
- `Repeated Message: "Remember, shorter queris make our conversation smoother and more effective. Let's keep it brief for better understanding.`
- **NOT_UNDERSTOOD:**

- `First Message: "Apologies, I couldn't understand your request. Could you provide more information?"`
- `Repeated Message: "I'm still having difficulty understanding. Can you try rephrasing your request?"`

---

# Advanced settings

Advanced settings within the 'Answer' node are quite complex. The advanced settings are designed to unlock the full potential of your Digital agent. These settings delve deeper into the intricacies of your bot's functionality, catering to both novice and seasoned users alike.

Advanced settings encompass a diverse range of features, spanning from fine-tuning speech-to-text timeouts to customizing the UI chat bubble appearance and optimizing obtaining  user utterance and intent recognition processes. These settings offer users granular control over various aspects of their bot's behaviour, empowering them to create more sophisticated and tailored conversational experiences.

![]()

****

## Speech-to-text timeouts

Let's break down the speech-to-text timeouts and explain when they're used, what they control, and their default values. It's also important to note that these settings are local to the specific Answer Node and apply only to that node.

### **No Input Timeout**

![]()

- Default Value: 15 seconds.
- This parameter sets the threshold time for detecting no response from the user. After this period, if the system detects no input from the user, it triggers the 'no_input' action signal. Based on this trigger, the system can either progress or activate fallback actions within the conversation flow. See

### **Maximum Listening Time**

![]()

- Default Value: 15 seconds.
- This setting is useful in scenarios where the user speaks for an extended period, and transcription keeps coming. After this period, the system sends a 'shut_up' signal, which can trigger fallback actions or transfer to the next node in the flow, based on the configuration of the Answer Node. See

### **Continuous Transcription**

![]()

- Default Value: Disabled.
- Recommended for open-ended questions, continuous transcription allows the Answer node to wait for extended pauses in speech before processing the information. This setting enhances transcription accuracy by capturing the user's complete utterance, even if they briefly stop to think or catch a breath.

- **End Transcription:**

- Default Value: 1800 milliseconds.
- When Continuous Transcription is enabled, this feature determines the timeout for concluding continuous transcription in specific scenarios. It optimizes resources by stopping transcription when no longer needed, enhancing performance.
- Values are specified in milliseconds. When the user pauses for a second, speech-to-text continues transcription but ends it and sends input when the pause reaches 1800 milliseconds (or the set value).

> **WARNING:** **Note! **
These speech-to-text settings are specifically tailored for voice-based interactions, such as those with voicebots or digital human interfaces. 

For chatbots, configuring these settings is not applicable, as chat interactions do not involve speech-to-text processing. Therefore, signals like 'no_input' or 'shut_up' cannot be triggered within a chat environment. When setting up your conversational assistant, consider the nature of your interaction channels to optimize settings accordingly.



## DTMF settings

DTMF signals are audio tones generated when a user presses keys on a phone keypad or similar input device. These tones are commonly used for interactive voice response (IVR) systems, allowing users to input numerical or menu selections during a phone call.

![]()

### **Expected DTMF Signals Length**

- Default: 0 (must be set to higher value).
- This parameter specifies the expected length of DTMF signal string, eg. 10 for a 10-digits order ID.
- For instance, if we expect the user to press a single digit like "press one," after receiving the first digit, the system won't wait for additional input. However, it's crucial to set the signal length appropriately. For example, on a scale from 0-10 or 1-10, the signal length must be set to 2. Otherwise, after pressing 1, the system won't wait for subsequent input, preventing the user from entering 10.

### **DTMF Timeout**

- Default: 3000 milliseconds (also minimum required, cannot be set to a lower value).
- This setting determines how long the system waits for DTMF input, in milliseconds.
- After this period, if no input is received, the system proceeds according to further configuration in ANS node.

### **Received DTMF Signal Silences Playback**

- When enabled, received DTMF signals silence the playback of the current natural language processing (NLP) response.
- This feature ensures that if the user inputs DTMF signals during a response playback, the system interrupts the playback to process the input promptly.

> **WARNING:** **Note! **
These DTMF (Dual-Tone Multi-Frequency) signal settings are specifically designed for voicebots, as they facilitate interaction via phone keypad inputs during phone calls.

Therefore, configuring DTMF settings is irrelevant for chatbots and digital humans, where users interact via chat, microphone or terminals rather than telephone calls. When setting up your conversational assistant, consider the input methods available to your users to optimize settings accordingly.

## Chat interface settings

Discover advanced settings to customize the chat bubble output in the Answer Node. From hiding the chat input field to enabling file uploads, optimising user interactions and streamlining the conversational experience.

### **Hide Chat Input Field**

- This setting hides or disables the manual input option in the chat field.

![]()

- It's beneficial when your conversational flow relies solely on button selections for intents, streamlining the user experience. For instance, if your chat interface presents users with predefined button options and you prefer they choose from those options rather than inputting free text, enabling this setting ensures users must make a selection, promoting clearer interaction paths.

![]()



### **Use as a Widget**

Engage the Answer node as a [widget](../digital-agent/advanced-functions/widgets.md) for specialized uses. This feature caters to advanced users seeking enhanced functionalities, offering additional customization options and integration capabilities. 

![]()

- When enabled, a code window appears for inserting the widget code. Widgets provide alternative ways of obtaining user input (such as [forms](), [star ratings](), [NPS ratings](), etc.)
- After training the projects, the widget will be rendered in the chat bubble interface upon entering the given ANS node. User input obtained within widgets is logged and processed based on further configuration of ANS node or the rest of the flow.

![]()

- All types of widgets are pre-developed, but customizable.  This feature is intended for advanced users only as it requires coding skills. For detailed documentation on widgets and code examples see .

> **WARNING:** 🔔 Coming Soon: No-Code Widget Builder Stay tuned for an upcoming enhancement to widget functionality! We're planning to revamp widgets and introduce a no-code feature, allowing users to easily create custom widgets using the widget builder



### **Allow File Upload**

![]()

- In summary, enabling Allow File Upload adds a functionality to the chat bubble interface, allowing users to share files. The associated parameters, Upload Timeout and Maximum Uploaded File Size, control the timeout duration for the upload process and set limits on the size of uploaded files, respectively.

- **Upload Timeout**

- Default: 10000
- This parameter specifies the limit, in milliseconds, for the duration the system waits for the file upload process to complete.
- If the upload process exceeds this timeout period, the system may trigger a timeout action or display an error message, depending on the configuration.
- **Maximum Uploaded File Size**

- Default: 10
- This parameter specifies the limit of the file size in megabytes.
- If a user attempts to upload a file that exceeds this size limit, the system may reject the upload or display an error message.

> **WARNING:** **Note! ****
These chat bubble output settings are specifically designed for chat channels, where users interact with the conversational assistant via text-based interfaces. In voice channels, such as phone calls, users utilize voice interfaces to provide input. Therefore, these settings are not applicable to voice channels.**

## Other advanced settings

### **Use Variable as Target**

![]()

- This advanced setting empowers node naming through specific variables, allowing for customized operations. It enhances flexibility and control over how intents are processed and managed.

### **Enable Language Detection**

![]()

- Activating this feature allows the 'Answer' node to analyze provided answers and determine the conversation's language. Useful for multilingual voicebots and digital humans or for directing users to appropriate language-specific flows.
- **Language detection is an advanced speech-to-text feature. As such, it won't detect the language of utterances obtained by a chat interface and does not apply to chatbots.**
- When enabled, the result of language detection is stored in a variable called language_detection. The value represents the two-letter ISO code of the detected language, such as "en" for English, "de" for German, or "pl" for Polish.
- Enabling language detection affects speech-to-text processing because it occurs before transcription begins. This process may take longer to receive the transcription of the user's utterance. Consequently, there will be a delay between when the user stops speaking and when the bot starts responding. This delay is due to several processing steps taking place in between, each taking a few milliseconds to a second.
- Enabling language detection merely stores the ISO language code in the background. If we intend to use language detection to control subsequent flow steps or transfer to another project based on language, we must manually configure this.

- For instance, within an Answer Node, we can set up a condition like language_detection == "de", where the target node is set to [transfer](../digital-agent/conversation-flow/nodes-explained/transfer-node.md) to a German language-specific project (TRAN_DE). This manual configuration ensures that the conversation continues appropriately based on the detected language.

### **Reuse Utterance**

![]()

- Stores unrecognized utterances (failure of intent recognition) obtained in the ANS node where this setting is enabled and reuses the utterance in the next Answer Node in the flow.
- This feature applies only to utterances that fall into the fallback category. If we want to reuse recognized utterances, we must enable reuse within the intent configuration.
- Caution! When this setting is enabled, it means that utterances from the fallback are carried forward until they encounter the next Answer Node in the flow. In the subsequent node, instead of stopping and waiting for new input, it evaluates the utterance remembered from the previous step.
- This behaviour also applies to signals from speech-to-text (no_input, no_match, shut_up). In that case, obtained input is a signal value and empty utterance (e.g. signal 'shut up' and utterance "" is logged in tech logs)  and this input is carried over to the next ANS node and reused as an input there as well.
- This feature is beneficial, for example, when designing a decision tree-like flow with gradual intent recognition. At the first level, we obtain the utterance and recognize only the general topic (e.g., Invoice). Then, we want to reuse this utterance in the next Answer Node, which focuses only on invoices and further categorizes them into specific topics (send invoice, missing invoice, wrong sum, unpaid).
