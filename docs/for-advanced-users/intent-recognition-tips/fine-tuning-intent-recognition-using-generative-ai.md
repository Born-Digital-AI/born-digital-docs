# Fine-Tuning Intent Recognition using Generative AI

This guide provides you with step-by-step instructions on harnessing the power of generative AI within our low-code platform to optimize the prompt for intent recognition.

Discover the ins and outs of refining prompts, allowing you to create more intelligent and context-aware conversational experiences for your users. Dive into the details and unleash the full potential of generative AI for precise and accurate intent recognition.

# **Understanding Basics of Generative AI for Intent Recognition**

Generative AI plays a pivotal role in intent recognition, offering a dynamic approach to understanding user input in conversational agents. Unlike rule-based methods, generative AI allows the system to generate responses based on learned patterns and context, providing a more flexible and context-aware interaction.

![]()

****

> **INFO:** While Generative AI is trained on a diverse range of general language data, recognizing specific intents may require some fine-tuning to align with your unique use case and domain. This is particularly important to ensure that the conversational agent accurately interprets and responds to user input in the context of your application.



In our low-code platform, you have two powerful options for fine-tuning Generative AI intent recognition, allowing you to tailor the model to better suit your specific needs:



Fill in the intent description to provide additional context for the Generative AI model. [This option]() allows you to offer a concise but informative description of the intent, aiding the model in better understanding the nuances and specifics associated with each intent. 


When crafting these descriptions, be mindful of token usage, ensuring that they effectively communicate the intent without exceeding any limitations. 




Customize the default super prompt used behind the scenes to add dynamic context for enhanced intent recognition. [This option]() empowers you to inject specific details or context relevant to your application directly into the model's training prompt. 
By modifying the super prompt, you can guide the model to focus on certain aspects or nuances, refining its ability to accurately recognize and respond to user intents.

---

# **Method #1: Intent description: Enhancing intent understanding**

Crafting meaningful intent descriptions can significantly enhance the model's understanding of user queries. Discover valuable tips and examples on effectively filling in intent descriptions, ultimately leading to more precise and context-aware interactions with your conversational agents. Let's delve into the art of providing descriptive context to elevate your intent recognition capabilities.

![]()

****

****

****

****

****

****

---

# Method #2: Edit default super prompt: Adding context of a conversation

Behind the scenes, all Generative AI intent inputs provided through the GUI are amalgamated into a comprehensive super prompt that empowers the ANS node. This unified prompt serves as a directive for the model during intent recognition, ensuring a seamless and efficient process. To facilitate this, a standardized prompt is generated for the ANS node, instructing the model on how to handle incoming utterances.

The template for this system message is as follows:

```
You are a useful assistant used for intent recognition. You are given a list of intents with its name, meaning and description. Please classify the sent utterance and respond only intent name from the list as a JSON object only. Carefully read all the instructions.
```

```
Classify the utterance that you receive as the next message into one of these categories by selecting the most dominant topic from this list below:- friendly name of intent 1: meaning of intent 1 [description of intent 1]- friendly name of intent 2: meaning of intent 2 [description of intent 2][...]If the requested values cannot be found, you should return "NOT_FOUND". Always respond with a valid JSON object in the format { 'recognized_intent': string }. Do not return anything other than JSON.
```



When fine-tuning your Generative AI intents, you have the option to customize the default super prompt, which serves as a crucial directive for the model during intent recognition. 

**To access the super prompt editing window you need:**

- Have at least one existing Generative AI intent set and saved.
- Navigate to the Intents sections in the ANS node and click on the pencil icon.
- Next, you can customize the super prompt system message and instructions.

![]()

- Edit instructions or add more context in the prompt. Furthermore, you can add placeholders of existing variables to fill in the prompt in a personalised, dynamically changing way. The current value of the variable will be filled into the prompt.
- Use this feature to your advantage. Enhance the understanding of the situation, previous interactions or knowing personal info about the user to handle the Digital agent - user communication gracefully and to master intent recognition with contextual awareness.

![]()

> **WARNING:** While this customization allows you to add context and refine prompt, we strongly recommend limiting edits to the system message only. Especially don't temper with the "Text after list of intents" section of a prompt. This is essential for maintaining the integrity of backend processes and ensuring seamless interactions between the user and the conversational agent.


Customizing the system message within the default super prompt offers a powerful avenue to introduce context for more nuanced and accurate intent recognition. It's crucial to note, however, that digital agents lack inherent knowledge of the preceding user interactions unless explicitly provided in the prompt. Additionally, without supplementary contextual information, there may be a decrease in intent recognition precision.

**Here are some customization tips:**

****

****

****

****

****

---
