# Basics

For large language models (LLMs), prompting serves as a critical interface. It allows developers to provide these sophisticated AI systems with tailored instructions, enabling them to generate narratives, answer queries, and perform a wide range of linguistic tasks.

The accuracy of a large language model's output is highly dependent on the quality of the prompt provided. Well-designed prompts act as clear instructions that define the desired content. A concise and effective prompt goes beyond simply conveying instructions; it serves as a strategic roadmap, guiding the model to generate results that meet specific stylistic, tonal, and contextual requirements.

Mastering the art of prompting is a game-changer, allowing developers to fine-tune responsiveness, creativity, and task relevance.

# What is a prompt

> In the context of language models, a "prompt" serves as the input or instruction given to the model to generate a specific output. It acts as the catalyst for the model's response, guiding it toward producing text that aligns with the user's expectations.

A prompt can take various forms, ranging from a simple sentence to a detailed set of instructions. It is the user's means of conveying the desired task or information to the language model. A well-crafted prompt is crucial for achieving accurate and contextually relevant results.

In the Flow Editor, you can leverage the [**AI Node**](../digital-agent/conversation-flow/nodes-explained.md) to harness the power of generative language models. Within the modal, you can customize the behaviour of the generative model by providing specific instructions or prompts. These custom instructions guide the model in generating content tailored to your requirements.

![]()

---

# Crafting effective prompts

In the realm of prompting, the art lies in constructing instructions that yield precise and relevant model outputs. This section explores key principles for crafting effective prompts, ensuring developers can harness the full potential of language models.

Here are some general guidelines:

****

****

****

****

****

****

---

# Prompt template for beginners

Start small and simple.

```
You are a {role/persona}. Your role is/you are tasked with {general task}. I need you to {needs to fullfill}. Be brief in your answers. Always respond in {language/format}.
```

```
Here is some additional information:- {context}- {knowledge}- {specific details}Here's what you gonna do: - {task's steps, details}, eg. {example}Please DON'T {forbidden steps}.In case you {cannot fullfil the task}, respond with "This is a fallback message".Otherwise, respond with {output format}.
```

```
This is user's input: {input_variable}
```

---

# Veteran prompter field notes

- DO NOT use "be helpful" in your prompt for chatbot behaviour, since it often leads to jailbreaks, as the virtual assistant engages in off-topic conversations in order to comply.
- `When defining desired output, it is better to use the verb "respond" than "answer", since the latter leads to lengthy, wordy output.
Respond with two or three sentences maximum.
Respond with "Sorry, I cannot provide a relevant answer".
Respond just with a whole number.`
