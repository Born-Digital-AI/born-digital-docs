# Product changelog

What´s new in Digital Agent? Read a quick change log overview

# Release 07.10.2025

_[Table content - see GitBook for full view]_

## AI node 2.0 - Tools

From this release, AI node now support various tools to be used within its execution (and more will be coming). With this, the API on which the AI node runs is now switched to responses API. However, to not loose backward compatibility and possibility to run on chat completions API - switch between New & Old AI node has been also implemented.

### New vs Old AI node

Below are the basic rules how New vs Old is goona work:

- All newly added AI nodes to the flow -> 2.0 version is used -> you can switch back to old AI node by flipping the toggle at the top of the AI node
- All existing AI nodes -> old version is kept -> you can switch to 2.0 version but it is IMPORTANT that

- You test your AI node accordingly
- You check the configuration. If you have been using Knowledge base tool, you need to configure it again

**NEW AI node - toggle is ON**

![]()

![]()

**OLD AI node - toggle is OFF & only KB based tools present**

![]()

### New tools in AI node

These are the new tools in AI node 2.0:

- **Web search**

- Working only for Open AI provider yet
- You can configure Search context size (how much context is retrieved from the web) and Country (refine search based on geography)
- Use Behaviour to set more context how websearch should be used and when
- **IMPORTANT notes**

- With GPT-5, nano model does not support websearch
- Reasoning effort needs to be set to at least Low

![]()

- **Redirect to human**

- Gives AI node an ability to handover the conversation to Human operator
- Tool description gives you an option to explain to the Agent, when this tools should be used - so what are the rules when handover should happen
- You can configure 1..N nodes, where the conversation can be transfered to -> Rationale gives you an option to explain, what conversation should be transfered where (i.e. Invoice topics to node representing transfer to finance skill, tech topics to tech skill etc)
- IMPORTANT -> you should redirect to MSG node ans specify message played to customer

![]()

- **Transfer to Node**

- Similar to Redirect to human
- You can use this tool to transfer the conversation to another specialised Agent (AI node)
- You can define 1..N transfers representing Agents
- **End process**

- In similar fashion, you can define situations, when conversation should be ended

### Attachments support in AI node

Within User input (Configuration section) you can now use attachments. You can do that by choosing a variable, where attachments is stored such as:

- Variable with any naming should contain URL to the attachment. This URL needs to be accessible via Internet
- In case your content can not be exposed to internet

- Use variable with naming binary_XYZ.
- Upload your attachment to the storage, where our platform has access to (i.e. Blob storage)
- Use the URL to this storage within the attachment
- Out platform will take the attachment, convert to base64 and send that for processing to LLM. Base64 is not logged nor stored anywhere
- **Variable type supported is a String or List**
- **Attachment type supported are: **

- PNG (.png) - JPEG (.jpeg and .jpg) - WEBP (.webp) - Non-animated GIF (.gif), PDF, DOC, DOCX are supported
- Up to 50 MB total payload size per request - Up to 500 individual image inputs per request

![]()

### Other configuration updates

Various changes were done in reagrds to GPT 5 * models. These are

- Temperature needs to be set to 1 -> so you will not be able to change that
- Reasoning effort - by default set to Minimal. This directly impacts effect on latency and reasoning tokens, which are more expensive. You can change it to Low/Medium/High for more reasoning type of actions

- For websearch, at least Low needs to be used
- Summary with setting of Auto and Detailed. Reasoning summary is stored with llm response in respective variable - not exposed to customer

Response format - if you use JSON, word json needs to be used in your Behaviour prompt.

![]()

## New Bubble MVP

**New bubble has been deployed on customer test bringing convergence of Text & Speech (avatar coming later). It will appear as 3rd option in the bubble in Digital Studio called "New Chat"**

![]()

Within this release, you are able to:

- Set the voice settings directly in the bubble
- Switch between Speech & Text mode
- Use streaming also for chat conversations
- Markdown language is supported for formatting

IMPORTANT - this is still MVP phase. Lot of more stuff is comming, bugs will appear and your feedback is appreciated. 

**What is in store for new bubble in next releases:**

- Avatar regime
- Bubble customization (colours) direclty in Digital Studio
- Bubble deployment via Deploy button
- js code to use for client web page directly in Digital Studio

**Text mode:**

![]()

**Speech mode**

![]()

## Removed Advanced & Custom parsing in KBI

For Knowledge base processing, options for Advanced and Custom parsing has been removed.

### DEV release notes

- NEW_BUBBLE_URL (typicaly [https://customer-test.borndigital.ai/da-bubble]())  env needs to be added to Builder deployment
- APP_AZURE_VERSION env ('2025-03-01-preview' and later) needs to be added to Llm-connector deployment
- Ingress needs to be updated for DA bubble

# Release 10.09.2025

_[Table content - see GitBook for full view]_

## New AI Node

AI node has been redesigned to bring more clarity to all the settings, you can use and need to configure also splitting them to Essentials (needs to be configured almost always) and Configuration, where the rest of the configuration is placed which doesn't often needs to be even touched.

All other nodes will also follow in this pattern. In the Essential configuration part, you can modify 2 of the most important parts of the AI node, which are:

### Essential

- Behaviour - here your system prompt goes. This is you role-play section, where you needs to define all your expectations from the AI node

![]()

- Tools - here is you place to specify Knowledge base details (at least for now). Very shortly, more tools will be coming here

![]()

### Configuration

In the configuration section you will find all the LLM configuration you are usualy used to tweak. Each section is expandable and should be intuitive to use for LLM users. In more detail:

- Modifying input for AI response - if not changed, whatever user says is send to LLM and is responded to based on the Behaviour you have set. However, you can modify it here to whatever you want. You can even add chain of User/Assistant messages

![]()

- AI provider - choose the LLM provider you want to use here. Models for each providers are updated regularly. With list of models, you can find also information how long (based on benchmark) does that specific model take to generate firs token within its response. This has impact on the final latency.
- Latency graph is showing how long would it take to generate audio response of average sentence using chosen LLM model abd STT/TTS setings used within you project. This assumes, that for longer responses you are using streaming option.

![]()

- Preparing the response - specify the rest of the parameters, which are sent to LLM with your request. If you want to use JSON response format, you need to use word "json" also in your prompt. All other parameters are as you are used to them

![]()

- Handling the response - specify, what you want to do once you get the response from LLM. You can specify to which variable the response is stored, wether it is also stored in LLM conversation history, wether it is shown to the user and wether it is streamed or not.

![]()

- Timeout - lastly, here you can set the timeout for the LLM response. If the response is not returned within specified time, response_text will be empty. You need to prepare for this eventuality in the flow

![]()

## New Message node

Same as of the AI node, Message node has been redesigned. Variables section has been split to Variabled and Tools, Message box has been simplified & new Voice section has been added.

- Message - has been simplified, where only 1 input box is present as default. This will be used for all channels. If you need still to specify different message for Chat or Voice channel, you can do it via Split toggle. Use the X to see the variables, you are using within your flow.

![]()

- Voice - here you can see TTS settings you are using on the project. You can change them and see the impact on the latency. This will be expanded in the following weeks with ability to synthesise that message to hear the final result.

![]()

- Tools - are the former Smart functions. For more details, see in the sections below
- Variables - in this section, you can define new or work with your variables. For more details, see in the sections below

## New Function node

Also FNC node has been redesigned. IN this node, you can work with the Tools (former Smart functions) and Variables. In addition, you can reset your variables here.

![]()

## Tools section

Former Smart functions (special type of Variable) has been significantly redesigned and given it's own section. Screen to work with the tools has been made bigger to bring:

- Tool configuration section on the left side. All the tools configuration parameters are shown here. They are also split to the required ones and the optional ones. You need to define at least the ones, which are required. You may be lucky, as some tools do not require any initial configuration.
- Documentation where each tool will have shown it's documentation on the right hand side. You will find there

- Basic tool description
- Example of User input and what would be the tool output
- Explanation of Required parameters and how to use them
- Explanation of Optional parameters and how to use them

![]()

![]()

## Variables section

Variables has been also significantly expanded giving you space to not just simply assign values or do basic text operations, but also to work with elaborate IF statements or even bring you own simple python 1 liners (they still need to pass an evaluator).

![]()

As remembering syntax is b*tch, we have brought you also the most common operators, which can be dragged into your variable workspace.

![]()

On the right side, you will also fint the copilot - chatbot with basic instructions as system prompt. You can use him to clarify syntax if needed.



In the future, ability to test you work directly here will be coming.

## New Redirect & End node

Redirect and Transfer has been changed as well. Transfer node is truly simple and therefor the author will not spend more time on that. However, redirect node is bringing some sections for you to use and we will validate, if such approach is something we will be bringing more:

- Destination - as redirect node is used for Human transfer, destination parameter is important. It is still a "simple" variable at the end, but we made a special section for that.
- Status - this is also a simple "variable" at the end, but to build dashboards, you usually needs to set at least some statuses within your flow. The idea is to give it this special attention at least at points, where something significant is happenings - which will be Start, Redirect and End node. you can use  variable "status" anywhere in the flow to expand this.

![]()

## Deploy modal

To continue with re-designs, deploy modal has been also taken into action. We again split it to Essential and Extras and brought also latency graph. To give you more details:

### **Essential section**

- General - selection of available phone numbers is here, from which you need to choose. You can also opt to record (and store) the call recording here.
- Voice - STT and TTS setup is made here. From this point, you don't need to specify each language if you are using Multilingual type of TTS here. But if needed, use Split toggle for that

- STT and TTS selection has direct impact on latencies. Latencies graph should be read in a way, that this is the time required for STT to transcribe the utterance and the average length sentence response is synthesised. In case of LLM, this processing needs to be added. In case of static cached response, TTS latency will not occur.
- Repeat question after no answer -> this is old no_input limit. Selected number means, that if the user is not reacting to the bot within the same Answer node for more than this number, call is dropped

> **INFO:** IMPORTANT: Different Voice (or any other) setup for each phone number wil not be possible anymore. This was decided to reduce the complexity of the setup, since majority of the cases the setup was the same. If you need to set different voices for different phone numbers, you can still do that -> just deploy different versions and each version can have its own set of phone numbers and Voice setup.

![]()

### Extras section

Backgroung music, whitelist and blacklist can be specified here.

![]()



# Release 08.04.2025

_[Table content - see GitBook for full view]_

## Product & Organization dropdowns in New tab modal

Now, when you want to open new Tab, you will be able to choose a Product and Organization, from which you want to open new project from

![]()

## New Whisper Cloud variants for TTS

Now, when deploying your project on some Phone number, you will be able to choose Whisper Cloud variants - specifically Whisper Open AI and Whisper Azure. Just few remarks:

- Whisper Open AI -> service is not hosted in European Union. To generate audio from average sentence, it takes around 700ms
- Whisper Azure -> here we have very limited quote on requests for a region in EU which is 3 per minute.  To generate audio from average sentence, it takes around 500ms

## Recently closed tabs

If you want to reopen the Tabs, which you have recently closed - you will be able to from now. Just look for 3 vertical dots in the top right corner

![]()

# Release 06.03.2025

_[Table content - see GitBook for full view]_

## New Workspace = Home

As part of the Digital Studio redesign initiative, we have decided to make significant updates to the Workspace section. Below are the main changes.

### **Organization and Product selection in left menu**

Organization and product selection has now been moved to the left menu, where you can now switch easily  

- between product you want to work with (either Digital Agent or Insights)
- between organisations - please note, that you will be able to see Organizations dropdown only if you are member of multiple organisations

![]()



### **Home section (previously Workspace)**

Previous Workspace section has now expanded to Home, where all activities outside of specific Project will be happening. You will be able to always get back to Home page by selecting Home icon in the top left corner.

![]()

Home menu is now consisting of:

- Projects where all projects, which you can access, are organized
- Organization where Admin can manage their organization and all users can manage Data sources for their projects (Input data mainly for users)
- Help section, where our Documentation is linked and also email to our support team can be generated

Projects section has also expanded providing multiple ways, how you can see your projects. These includes:

- Recent - you can see last 10 projects you have opened or made changes in (for given organization). If you don't see any - don't worry. They will appear there once you open any project
- **Favourites - you can mark any project as your favourite (just use "star" icon on the project detail) - and you will see them all here **
- **Folders - you can create your own folders in which you can then organise your projects. These folders are your own and will not be applied to different users. Each user can use their own folder structure**
- All projects - here you will simply see all the projects you have access to

** **

![Projects section & Recent view]()

![Projects section & Folders view]()

### **Project settings **

We move from the left menu to the main part of the Home page - Projects. In whichever view you choose, you can:

- Open Project settings by single click on your selected Project tile

- Project settings will appear in the bottom right corner
- Open Project as such (flow or configuration) by double click on the Project tile, or by choosing Open in the project settings

![]()

### **Filters & Search**

Now, in all projects section you are quickly able to filter your projects by:

- Live parameter -> all projects, which have been deployed to Phone Number
- Trained parameter -> all projects, which are trained (meaning at least 1 version is trained)

You can also use modified Search bar at the top of the page. you can search by Name, or some tags like Owner & Editor. Important - results of the search will be shown in the modal and you can open projects from there

### **Project in tabs**

Once you open any project, you will be redirected to new tab as shown below. IMPORTANT change here is, that now you will be able to open Multiple projects at the same time and switching between them - even though they are from different organization.

![]()

Left menu within opened project stayed mostly without changes. However, we have included possibility to:

- See that project version is trained or not
- Mark project as favourite
- Open Project settings

As part of the left Project menu

![]()



## Tables - new design

All data grids across the app were redesigned to a new, improved layout. These updates enhance usability and provide additional functionality for better table management.

1. **Resizing Columns**

- Users can now adjust column widths to be larger or smaller as needed
- This functionality is available in all data grids, including those on the Campaigns page
2. **Advanced Filtering**

- A new filtering system has been added to simplify data search.
- Users can define operators and input values to filter specific columns.
- To apply filters:

1. Click the filter icon in the upper right corner.
2. Enter the desired values and press enter
3. **Quick Text Search**

- A simple text-based search field is available for quick filtering.
- Users can enter search terms, press Enter, and instantly see the filtered results.

![]()

![]()



## Knowledge Base updates

### **Index**

Clicking on the index name opens a modal displaying a table of documents.

![]()

### **Documents**

Clicking on a document name opens a modal for editing the document.

![]()

### Indexer upload status

**Within the Knowledge Base tab, while uploading documents there is a modal showing all newly created documents and their upload status. Now, with high number of documents being uploaded, user can scroll through them.**

![]()

## Disable utterance processors

To improve performance, we introduce a new configuration option for projects that do not contain any intents of type Training Set. These projects will automatically bypass all utterance processors (such as transformers, correctors, and stop words processing), as these operations are unnecessary and can negatively impact CPU performance.

**Configuration Details**

- `Parameter Name: disable_utterance_processors`
- Type: Boolean (true/false)
- *Friendly Name: Disable Utterance Processors*
- **Description:**

> If set to true, all utterance processors (i.e., transformers, correctors, stop words) will be disabled.

**Behavior & Default Settings**

- **Default Value:**

- true → If the project does not contain any Training Set intents (other intent types may still be present).
- false → If the project contains at least one Training Set intent.
- **Automatic Adjustment During Training:**

- The flag is evaluated and set during training.
- If an intent of type Training Set is added before training, the flag is set to false.
- If all Training Set intents are removed, the flag is set to true during the next training cycle.
- **Sync Behaviour (Flow Editor & Code Editor):**

- If sync between Flow and Code editors is enabled, the flag is automatically updated based on the project's intents.
- If sync is disabled, the flag follows the Code Editor setting:

- If the flag was not previously set in Code Editor, it defaults to false.
- If the flag is present in Code Editor, it remains unchanged.

**Implementation in Configuration**

The disable_utterance_processors parameter is available in both:

1. **YAML Configuration**
2. **Flow Editor Settings**

![]()

## ANS node - Advanced settings change

### Maximum listening time is now allways higher than noInputTimeout

The noInputTimeout parameter determines the duration the system waits for user input before timing out. 

The maxListeningTime defines the maximum allowable listening period once input starts. 

**In cases, where these times has been set to the same value, shut_up signal would be send to conversation in case this time is reached (so maximum listening time takes precedence). Now, in newly created ANS nodes, Maximum listening time is allways set to higher number than No input time.**



![]()

## ANS node - default intent type

In the Add Intent modal, we have changed the order of options for intent type as follows:

- Generative AI (First)
- **Training Set**
- **Keywords**
- **Condition**

**Updated Default Selection:**

When user is creating a new intent, the default selection is now Generative AI (previously set to Training Set).

These changes ensure a more intuitive workflow by prioritizing Generative AI as the default intent type.

![]()



# Release 14.11.2024

_[Table content - see GitBook for full view]_

## Beta testing of colour scheme of Digital studio

As a test we've come up with a slightly altered - cool toned - variant of green for our Digital Studio. Feel free to share with us your feedback, which variant works better for you.

![]()

![]()

![]()

![]()

![]()



## New multilingual speech to text provider (Whisper) added

![]()

A new Speech-to-Text provider option, Whisper, has been added to the platform, enhancing transcription capabilities for users mainly in the multilingual area. 

Whisper, developed by OpenAI, is renowned for its accuracy and versatility across multiple languages. It excels at recognizing various accents and dialects, making it a powerful tool for diverse, multilingual applications. Whisper’s strengths lie in its robustness and adaptability, offering reliable transcription even in less-than-ideal audio conditions.

Whisper also requires less time for preparing a transcript leading to lower latencies when used.

As Whisper doesn't support continuous recognition - our implementation leverages voice activity detection (VAD) to differentiate speech from silence in an incoming audio stream, sending only the relevant audio chunks to the transcription service. This approach reduces processing demands and improves transcription accuracy and responsiveness.

> **WARNING:** As use of Whisper is still in the trial phase, for production uses of Whisper, discuss with the product team.

****

## Reference node in new design

Reference nodes have been updated to match the appearance of their original nodes. The background colors of the reference nodes are now lighter versions of the original colors, and they have the same shape, making them look more similar.

![]()

## Duplex - Possibility to be able to jump to Voicebot speech

User speaking with voicebot will now be able to interupt the voicebot in his speech. This has been long in the discussion, but with LLMs now also possibly contributing to the success of the call.

> **INFO:** With old NLP based conversation flow, this functionality would almost all the time lead to not understanding and transfer to the human operator.

This feature needs to be TURNED ON, if you want to use it, in the Advanced settings in each Answer node, where you want to use it.

PICTURE

> **WARNING:** IMPORTANT - be careful with this functionality, as any audio input may interrupt the voicebot in their speech.

But its not just that - The Voice Interaction Interruption API now allows external applications (User, Digital Human touchscreen etc) to interrupt the system's voice processes, whether it's speaking back a response or listening to a user. This feature is useful for making real-time adjustments, enabling external signals to take precedence over ongoing tasks.

****

## Project version is shown in project dropdown again

**In header is now next to project name is now again visible information about version. **

When user change the version of project he can see it there and it is not nescessary to go to version history to check wich version of project is In use. 

![]()

## Updated By information in the Version history 

Now, in Version history modal, you will be able to see who made the last changes to the flow. This information is updated automatically wich each save (manual or automatic) of the version. Just a reminder, project version is automatically saved with each Open/Close of the node and all other activities on the conversation flow page.

![]()

## Knowledge base and conversation transfer between muliple logic

We have encountered a bug, when if you had a Transfer node in the project and were using the Knowledge base, in some conversations the knowledge base would not be pulled by the AI node. This was caused by not correct project id used by back-end in that conversation. As a workaround, knowledge base was needed to be uploaded also to the project, where the Transfer node led.

**This bug has been fixed.**



## Pasting text to start of Message node

Bug with pasting text at the beginning of the text box has beed fixed. 

![]()

## ElevenLabs spending has been added to logs

As part of Cognitive services spending log, we have added spending monitoring specifications for the ElevenLabs Text-to-Speech (TTS) service, focusing on tracking characters synthesized and audio duration. These metrics are essential for monitoring usage and performance, similar to the current logging for multilingual TTS.

****

## **Copy of flow elements is working again**

Copying of flow elements has been fixed working now also with all of the node content and also between projects.

![]()

## **Various Design and Functional changes**

- New nice animation when waiting to load the data
- Design fixes after new design system implementation
- New way, how counter is generated in Yaml - leading to quicker BOT responses, especially with long conversations
- Voice-connector has been updated - only user speech part is sent to Voice with STT, reducing completely the situations, where BOT can listen to itself
- Azure multilingual voices has been added
- Support for new out-calls up in Voice-connector, Voice and NLP has been added
- In NLP, fixes has been made to prevent conflicting DB updates in coversation history leading to not correct stated in some cases, where non=blocking fetch_url has been used

# Release 30.09.2024

_[Table content - see GitBook for full view]_



## New LLM Providers integrated with our solution

The AI node now supports integration with various LLM providers including Azure, OpenAI, Anthropic, Gemini, and Grog. This allows business users to choose the best solution based on their business needs, improving flexibility and performance.

### **Provider Descriptions:**

**• Azure: GPT 4o mini for Standard model and GPT 4o for Advanced model. Best for big corporate clients. It excels in handling large-scale deployments with robust security and compliance requirements. It's compliant with GDPR requirements for clients in EU.**

**• OpenAI: GPT models directly from Open AI provider. Newest models available very quickly with much higher limit for maximum token per minute spend. Data may be processed outside of EU.**

• Gemini: Alternative if Open AI models shoyuld not be user. To be used mainly in EN languages, local languages after thorough testing. Flesh and Pro models, where: 

- **Gemini Flesh shows higher speed with comparable quality and price compared to GPT 4o Mini**
- Gemini Pro showing higher quality than GPT 4o with lower price but also speed

• Grog: Optimised for high-speed responses and low-resource environments with high amount of input data. It’s a good choice for lightweight voicebots where speed and efficiency are critical without sacrificing too much on quality. To be used mainly in EN languages, local languages after thorough testing.

- Llama small (3.1 8B): very quick in responses, slightly lower quality and lower price compared to GPT 4o Mini
- Llama big (3.1 70B): comparable quality with 4o Mini, slightly higher price

• Anthropic: Good for logical reasoning. To be used mainly in EN languages, local languages after thorough testing.

- Sonnet (Claude 3.5): best for programming and complicated logic. Slightly more expensive than GPT 4o with higher context window.



### **AI node changes**

UI of our AI node slighlty changes, where Provider and Model name are shown to the user right away. Default is Azure and Standard model, but you can choose you provider now. You need to be sure, if you want to use different than Azure provider in terms of:

- GDPR rules and requirements of your client
- Quality of responses for your context, especially in non EN languages

![]()

### **General technical info:**

New LLM service needs to be deployed to support non Azure LLM providers. In case the service is not deployed, old implementation will be still supported for several releases using Azure Open AI LLM provider only.

### **Environment variables changes needed:**

**Builder-Server**

```
LLM_CONNECTOR_API_URL needs to be added with URL to LLM Service deploymentFor each provider, Friendly names and actual models names needs to be provided in a form: friendly name (i.e. Standard) | model name (i.e. gpt-4o-mini)Such as:LLM_PROVIDER_AZURE_MODELS: Standard|gpt-4o-mini;Advanced|gpt-4oLLM_PROVIDER_OPENAI_MODELS: Standard|gpt-4o-mini;Advanced|gpt-4oLLM_PROVIDER_GEMINI_MODELS: Gemini Pro|gemini-1.5-proLLM_PROVIDER_ANTHROPIC_MODELS: Haiku|claude-3-haiku-20240307LLM_PROVIDER_GROQ_MODELS: Llama small|llama3-8b-8192;Llama big|llama3-70b-8192;Mixtral|mixtral-8x7b-32768
```

**NLP Engine**

```
LLM_CONNECTOR_URL needs to be added with URL to LLM Service deployment
```

## New design system

About 80% of new design system components has been developed and applied to as-is UI of the Digital Studio. The biggest changes can now been seen in buttons, checkboxes, icons, tabs, drop-down and switch options, Avatar menu, navigation panel, textfields, alerts, tooltips, stepper and scroll bars. Just see for yourselves. Now, rest of the components will be developed in parallel with complete workspace redesign and creation of templates.



## Custom parsing documents - Better support for PDF files

In knowledge base section, upload of PDF file now has better support for parsing of the document.

## Call end signals now properly propagated to the flow

Starting now, the system will now transparently log and display how each call ended, both in interaction logs and technical logs. 

This includes detailed reporting on the success or failure of call redirects to human agents. For all SIP transfers (both attended and unattended), the outcome of the transfer—whether successful or not—will be logged, providing greater transparency and control over call handling. 

> **INFO:** **If a transfer is successful (202 Approved for SIP REFER or 200 OK for SIP INVITE), the call will be connected to human operator. In case of failure, information is send back to flow and alternative steps such as API call can be employed to manage the fallback situation.**

Call end information is also now stored in the call_end_type variable, which can be leveraged for reporting and visualisation as part of Kibana dashboards.

Call End type of information stored in call_end_type variable:

• call_finished: Logged when the call is ended by the digital assistant or an automated process.

• call_end_customer_hangup: Logged when the customer explicitly hangs up the call.

• call_redirected: Logged when a transfer to a human agent (SIP transfer) is successful.

• call_redirect_error: Logged when a transfer to a human agent (SIP transfer) fails, allowing for alternative handling.

> **INFO:** With these enhancements, businesses gain improved reporting and monitoring capabilities, ensuring accurate tracking of call outcomes for more informed decision-making.

## Possibility to show/ hide password

New functionality to show and hide password was added - just click on the eye icon.

User can use it on login page, My account page, Organization page, reset password and change password page.

**Show password**

After clicking on the icon of an open eye, the password is shown and icon changes to closed eye.

![]()

**Hide password**

After clicking on the icon of closed eye, the password is shown as asterisks again and icon changees to opened eye.

![]()



## Digital studio loading

The digital studio loading is now much faster then in previous release. When user f.e. restart the page it shows load around 490 ms. On slower internet is the load time a but longer.

![]()

## Organization dropdown

The bug, where in some of cases Organizatin dropdown was not shown is now fixed.



# Release - 27.08.2024

## Digital studio - overview

_[Table content - see GitBook for full view]_



## Refresh button within active campaign

To prevent issues with huge amount of data loading in Digital Studio, we have introduced Refresh button within active campaign page.

Now, when the campaign is running and you would like to see the actual progress, use this button to fetch most updated data.

If you don't use Refresh button, data will be fetched every 2 minutes, if the page is active. 

![]()

## Recordings page changed to Conversations page

The Recordings page now is changed to Conversations page and is showing all conversations within the respective project, including chat ones.

Each conversation in DB has now information, wether the recording was stored or not. If Yes, recording will be shown also in Digital Studio - if not, only transcript will bw show - as shown below:

****

## DTMF processing set up

> **From this release, DTMF processing will be turned OF as a default setting and needs to be turned ON, if we want to process DTMF signal in ANS node.**

**In the advanced settings of ANS node, a new toggle switch labeled "Turn on processing of DTMF signals" is introduced. By default, this toggle is set to OFF.**

A new variable which was set by enable DTMF in YAML configuration, process_dtmf_signals, is added to the YAML configuration. This variable controls whether DTMF signals are processed. 

The voice processing logic is updated to respond to the state of the process_dtmf_signals variable:

- When the toggle is ON (process_dtmf_signals is true), DTMF signals are processed as they are received.

![]()

- When the toggle is OFF (process_dtmf_signals is false), DTMF signals, though received, are ignored and not processed.

![]()

### **Steps for Configuration**

Access ANS node advanced setting:

- Open the respective ANS node configration
- Go to the Advanced settings
- Locate the new option to toggle



![]()

Default Settings:

- For all existing accounts, this setting will be enabled by default.



![]()

## Transfer on SIP level

This feature allows administrators to configure the transfer type (attended or unattended) for each SIP account individually. This update provides greater flexibility by allowing transfer types to be configured per SIP account while maintaining a default setting for the overall environment. Previously, the transfer type could only be set globally across the entire environment using an environment variable. With this update, you can maintain a default transfer type and customize it per SIP account as needed.

**No change needed for existing SIP account registrations.**

****

## SIP/ Refer- optional header parameter

In our current SIP redirect implementation, optional SIP headers are defined using the X_<variable> format. This feature enhances compatibility with various PBX systems by allowing administrators to control the inclusion of optional SIP headers in SIP REFER requests. This feature is available in the SIP account settings within the Voice Connector and can be controlled via the Digital Studio interface.

**New Implementation**

**New configuration option allows administrators to enable or disable the sending of optional SIP headers in SIP REFER requests.**

Configurable SIP Headers:

- New Option: In the Voice Connector settings, under the SIP account configuration section, a new toggle will be available to control whether optional SIP headers (e.g., X_destination) are sent with SIP REFER requests.
- Default Setting: The default setting for this option will be ON (i.e., optional SIP headers will be sent). This setting will be applied to all existing SIP accounts.

![]()

- Turning Off SIP Header: When this option is turned OFF, only the Refer-To header will be sent in the SIP REFER request, and the X_destination and other optional SIP headers will be omitted.

![]()

Digital Studio Interface Configuration:

- This feature is configurable via the Digital Studio interface (through builder-server).
- Administrators can toggle this setting on or off per SIP account within the Connector section.

Conference Call Feature Update:

- The conference call feature respect this new configuration setting. If optional SIP headers are turned off, conference calls will be handled without sending any X_<variable> headers in SIP REFER requests.



## Import/ Export LLM configuration for CIA projects

### FE changes

There was add an Export/Import button into interface.

- When the import is successful, a msg "Import successful" is shown.
- When the import is not successful (strange JSON format or any other issue), a msg "Import unsuccessful" is present.

### BE changes

### Export functionality 

The entire LLM configuration, including prompts, custom parameters, etc., is exported into a JSON file. Clicking the Export button will generate and directly download the JSON file.

### Empty configuration

If the user exports an empty configuration, the JSON file will be generated with no fields filled in, which is acceptable.

### Import functionality

When importing, a file explorer opens to allow the user to select a JSON file from their PC.

The system checks the format of the JSON file:

Correct Format: The configuration is imported, and any existing LLM configuration is completely replaced.

**Incorrect Format: The user is notified with the message "Import unsuccessful."**



## Utterance_language extractor 

The extractor utterance_language returns the ISO code of the detected language



# Release - 15.07.2024

## Digital studio - overview

_[Table content - see GitBook for full view]_

## Conversation DB table migration (NLP application)

Part of the changes within NLP application is migration of conversations table to enable quicker bot responses, analytics being used also on BOTs and to have all conversations, not just voicebot ones in the Recordings tab in the studio.

**This migration to run requires these changes in deployment:**

### **To migrate table to new structure:**

```
DATABASE_MIGRATION_CHECKPOINT = "CreateGetConversations"DATABASE_MIGRATION_BATCH_SIZE = (default is set to 5000)IMPORTANT: temporarily increase liveness & readiness  probes delay to allow migrations to run
```

### **To migrate back to original table structure:**

```markup
DATABASE_MIGRATION_CHECKPOINT = "RevertConversations"
```

> **WARNING:** **NLP with version 1.22.10 and higher needs to have the table migrated.**

## To prepare for new conversations page

Migration of the DB table is also a preparation for the new conversation page in digital studio, where instead of recordings - all conversations will be shown.

**To support, that these conversations, if having a recording as well, can have that recording being played from the digital studio, release of voice-connector need to happen.**

### Voice connector related information:

```
Version: v1.15.5ENV: NLP_ENGINE_URL={URL for NLP Engine}
```

# New AI node property variable

We have completed a minor deployment on the Customer-Test environment, specifically related to the indexer functionality. This update introduces important changes that you need to be aware of:

## New Automatic Variable Population in AI Node

When using the indexer in the AI node, the following variables are now automatically populated and can be utilized within your workflows:

## **FINAL DOCUMENT Variables:**

- kb_document_id: Contains the internal ID of the document used. This ID can be used for advanced API calls to the indexer, if needed.
- kb_document_name: Contains the name of the document used for the final answer.
- kb_document_url: Contains the URL of the document used for the final answer. This will be empty if the URL is not populated in the document.

![]()

Use Case Example: To display to the user which document was used to prepare the answer, you can use the MSG node after the AI node. For instance:

```kotlin
For more information, check this document:[{kb_document_name}]({kb_document_url})
```

or

```csharp
My answer was based on this document:  [{kb_document_name}]({kb_document_url})
```

The end result will be a clickable link to the document used for the answer. Ensure the URL is populated in the Knowledge Base tab and is the URL of the original document.

## INDEXER Related Variables

The following variables are now available for indexer-related data:

indexer_returned where result of the index search to the indexer is stored. It's json format with

- list of documents, from which the snippets were found based on the question and snippet size
- for each document

1. id of the document
2. url of the document
3. name of the document
4. labels for the document
5. description = annotation od the document
6. individual chunks (again, as list)

Use Case Example: For reporting and troubleshooting, you can check which snippets have been found and what document descriptions were used to find the best answer without needing to check technical logs. This can also be used within the flow to work with JSON-structured variables.



![]()

## **AI NODE primary variable, where the response of GPT is stored**

The primary variable where the GPT response is stored remains the gpt_response variable. This JSON structure now also includes:

- gpt_response variable (or however you call the variable in the AI node)

it's a json structure variable, where originaly you were working with (or AI node used bu default) the key "response_text"

- **Now it also contains these keys:**

1. function_call -> if the AI node used function, you will see it here and use in the flow or troubleshooting. This key contains

name of the function used

arguments -> in our case questions, which GPT used to send to indexer
2. error -> if there was an error response form the AI node/gpt

**Example:**

![]()



## Design System Change is Coming

We are glad to announce a desig system unification and update for the Digital Studio. Here are the key changes already deployed with many more to come:

![]()

- New Default Font: We have adopted Montserrat as our new default font.
- Updated Color Scheme: The color palette has been revamped to be aligned with our official colors.

> **INFO:** This is just the beginning of the changes coming in following weeks.



## Two-Factor Authentication for Clients

You can now set up two-factor authentication using an authorization key on your mobile phone to meet specific organizational security needs.

![]()



## Role Management for Admins

Admins can now change user roles within their organization. This feature allows for the promotion and demotion of users via the /organization interface. See the GIF below:i

![]()

## Knowledge Base Improvements

- When creating the index, annotations are now automatically created in the project language, with future plans to unify this process.
- Uploading documents will now automatically generate a document description as an annotation.

![]()



## Technical and Business Variables in Overview

You can now toggle to display both technical and business variables in the variables overview:

![]()

- Business Variables: Created by the user.
- Technical Variables: Automatically generated by Digital Studio, such as:

- Location
- Phone number
- Conversation
- Channel
- Header Parameters





## **Additional changes**

- Application Performance: We have enhanced the performance and logic of the Digital Studio, ensuring greater efficiency and a smoother user experience
- Bug Fixes and Improvements: Model queries have been optimized for increased speed and efficiency, contributing to overall system reliability and performance



---

# Release - 07.06.2024

## Digital studio - overview

_[Table content - see GitBook for full view]_

## Index Parsing Methods Improvements

We have introduced new capabilities to enhance the parsing of documents into multiple chunks within the Index:

- Simple Parsing Method - Delimiters: You can now split documents by setting a delimiter (ENTER or double ENTER). The document will be divided into snippets based on the chosen delimiter. Default delimeter means snippets will be parsed with the same approach as before

> **INFO:** Use this method in case you have a clear TXT document (for example FAQ type), where you have paragraphs of text woth questions / answers and you have ENTER or double ENTER between the paragraphs. Created snippets will be then created based on these paragraphs

![]()

- Custom Parsing Method: Select specific areas to split into snippets using the SHIFT + ENTER command, allowing for more control over how the snippets are creating. For now, upload just one document at a time if you want to use this method

> **INFO:** When you upload your document, set the Custom parsing method and you press Upload -> txt version of the document will be shown to you on the next page, where you can decide by yourself how the snippets will be created

![]()

> **INFO:** The default parsing method remains unchanged, with parsing still performed after a certain number of characters.

​

## Export/Import Index from Knowledge Base Tab

We have enhanced our Knowledge Base tab to allow you to easily export and manage indexes. You can now export one or multiple indexes with a simple click. Additionally, we've updated the functionality to ensure that the exported indexes can be seamlessly re-imported.

Copy indexes functionality can be also used if you just want to copy the index (either to the same, or other project).

> **INFO:** **This will help you to move your fine tuned index from Test to Prod for example. All content of your index is exported (incl. snippets) and are uploaded to the new environment in the same way. You can also export and import whole project configuration, which includes also indexes now**

![]()

> **WARNING:** This week, we upgraded our default embedding models from text-embedding-ada-002 to the latest text-embedding-3-large. We recommend copying the active indexes in your project, which will copy it but use new embedding model to create your embeddings. 

See [https://openai.com/index/new-embedding-models-and-api-updates/]() to check why the new model is better, especially in non English languages.

## Updated URLs in Digital Studio

We redefined how the URLs are structured when using our product. The unique Project ID is now integrated directly into the URL structure, as well as information on which tab are you located and which element you have opened.

With this update, you can now share exact node paths or project paths within the conversation flow with your colleagues. When they access the shared URL, the connected project with the specified node will appear, streamlining teamwork and facilitating more frequent project sharing.

![]()

> **INFO:** This improvement applies to all aspects of Digital Studio, as well as in Customer Insight Analytics product

### Old URL structure: https://customer-test.borndigital.ai/digital-agent/conversation-flow

### Updated URL structure: https://customer-test.borndigital.ai/digital-agent/64df3ed850e70791449cceab/conversation-flow/MSG_START



## Message Node Announcement Enhancements

You can now use Announcements in your Message node UI directly and set their behaviour for Chat conversations.

![]()

## **Additional changes**

- **Global Fallback Counter in Answer Node: You can now create a global fallback counter for ANSWER nodes, instead of having individual counters for each node. This means, where applied, that fallbacks count in the whole conversation is considered.**

![]()

- Digital Email Processing tile has been removed from the main page, since email bot is now part/combination of both main products.
- Technical Logs Removed from Sidebar: As part of our UI improvements, access to Technical Logs has been removed from the sidebar, resulting in a cleaner and more user-friendly interface
- Application Performance: We have enhanced the performance and logic of the Digital Studio, ensuring greater efficiency and a smoother user experience
- Bug Fixes and Improvements: Model queries have been optimized for increased speed and efficiency, contributing to overall system reliability and performance



---

# Release - 09.05.2024

## Digital studio - overview

_[Table content - see GitBook for full view]_

​

---

## **Project Export and Import via .ZIP Files Now Includes Indexes**

You can now export and import your project as a .ZIP file along with all connected assets. Please note that this process may take some time.

> **DANGER:** The file structure for imports has changed. You will need to create new export and import packages moving forward.

![]()

> **INFO:** This feature is currently operational on MacOS. However, a minor bug has been identified on Windows (Edge and Chrome browsers). We are actively developing a hotfix for this issue.

## **Enhanced Knowledge Base Index!**

We've upgraded our knowledge base!  You can now edit, delete, or add new chunks in one dialog. 

![]()

## **Project Deletion and Associated Asset Removal**

Deleting a project will also remove all connected assets. A new dialog box will confirm that the following related assets will be deleted:

- Knowledge base indexes
- Campaign data
- Annoucements settings

![]()



## **Enhanced Capability: Creating New Nodes within Intents**

We have introduced the ability to create new nodes directly in the 'Answer' node of intents, enhancing the user experience by providing a more straightforward workflow.

![]()



## **Export Flow images with or without Comments**

You can now export your project flow as a *.PNG file, either including or excluding project comments. Test out both options to determine which best suits your needs.

![]()



## **Additional changes**

- Application Performance: Enhancements to the performance and logic of the Digital Studio now deliver greater efficiency.
- Bug Fixes and Improvements: Model queries have been optimized for increased speed and efficiency.
- Knowledge Base Indexer: Document descriptions are now limited to 1024 characters.
- Campaign Reports in XLSX: You can now export campaign data directly to XLSX format from the campaign page.

We are committed to continuous improvement and innovation to serve your needs better and exceed your expectations. Future updates are on the way, and we thank you for your ongoing support.



---

# Release - 28.03.2024

## Digital studio - overview

_[Table content - see GitBook for full view]_

​

---

## Application speed enhacements

In our latest update, the focal point of our sprint was the enhancement of speed and performance across the Digital Studio. Our dedicated efforts have culminated in significant optimizations, enabling us to achieve up to a 90% reduction in loading times for various queries through comprehensive refactoring.

****



## Better uploading documents async way 

Uploading documents to your Knowledge Base Index is now asynchronous, allowing you to monitor the progress of each file in real-time.

![]()



## Better uploading documents in bubble 

Enhanced Visibility in Chatbot Bubble: The document upload process within the chatbot bubble has been revamped for greater visibility. Stay tuned for additional updates.

![]()



## Application Status Bar Expansion

We've integrated the Indexer application into the app status bar. This addition allows you to view all active applications and their deployment versions, including the Indexer app.

![]()



## **Additional changes**

- Indexer Performance and Logic: The performance and underlying logic of the Indexer application have been enhanced for greater efficiency.
- Frontend Improvements: Minor technical updates have been made to the Flow Editor, enhancing usability.
- Elevated Customer Experience: The process of creating a new, blank project has been streamlined, focusing on user-friendliness.

We are committed to continuous improvement and innovation to serve your needs better and exceed your expectations. Future updates are on the way, and we thank you for your ongoing support.



---

# ​​Release - 08.03.2024

## Digital studio - overview

_[Table content - see GitBook for full view]_

​

---

## Variable overview 

We've introduced a user-friendly modal dialogue that displays your project variables at a glance. You can now easily identify where each variable is used across your project and swiftly navigate to change their configurations. Plus, we're showing default variables to streamline your future projects. When the blank is used in columns, these variables are defaulted when starting the project. Check out the new interface in action below:

![]()

## Enhanced Admin Controls 

Admins now have more flexibility with project variable settings:

By default, it's set to NO. Switching it to YES ensures variables are kept out of logs and not displayed anywhere. They content can not be "copied" to another variable, enhancing your project's privacy.

Initially set to YES. If changed to NO, it helps protect sensitive data (like personal client information) by preventing it from appearing in logs.

Set to NO by default. Turning this on allows selected variables to be edited externally via API, useful for dynamic updates like chat interactions. 

If at least 1 variable is defined in API editable section as YES, it is possible to update from chat interactions only variables marked as API EDITABLE YES

## Simplified interactions using shortcuts

We're excited to announce new shortcuts to make your Digital Studio experience even smoother. These shortcuts are designed to enhance your workflow and help you navigate the studio with ease. Check out the new shortcuts in action below:

![]()

Dive into this update and leverage the power of automated web scraping to bolster your knowledge base!

### Learn, how to use shortcuts 

You can find a comprehensive overview of all the new shortcuts within the app. Just navigate to FILE -> Shortcuts modal to learn more and incorporate them into your projects.

Ideal for training, deployment, and various project management tasks.

_[Table content - see GitBook for full view]_

Streamline your editing process with these handy shortcuts.

_[Table content - see GitBook for full view]_

Familiar essential shortcuts, now with ALT replacing CTRL for improved accessibility.

_[Table content - see GitBook for full view]_

Effortlessly create multiple nodes with a simple click on the canvas. Press ESC to revert to the normal cursor.

_[Table content - see GitBook for full view]_

Navigate UI changes quickly with shortcuts for the move tool, hand tool, and comment tool.

_[Table content - see GitBook for full view]_

Enhance your project view with quick zoom in/out shortcuts.

_[Table content - see GitBook for full view]_

> **INFO:** **Special Note for Mac Users: **

Don't worry, we've got you covered! Mac users can enjoy these shortcuts by using the OPTION key in place of ALT, and the COMMAND key instead of CTRL.

## Web scraping for Knowledge Base Indexing

Enhance your knowledge base with our latest addition: a web scraping function. This new feature automatically populates your knowledge base index with data collected from the web. See how it seamlessly integrates and enriches your resources:

![]()

Dive into this update and leverage the power of automated web scraping to bolster your knowledge base!



## Enhanced Application Cursors

Experience enhanced efficiency with our new application cursors! Creating multiple nodes is now as easy as pie. Utilize the shortcut SHIFT + M to add numerous message nodes to your project instantly, or press ALT + C for quick comment creation. 

![]()

For single nodes, simply drag and drop from the node panel. Try these out and streamline your project development!



## Easy Navigation to Previous Node

Navigating to the previous node has never been easier. Now, with just a click, you can access the last connected node modal, allowing you to see the pathway and understand how nodes are interconnected within your project. Discover this intuitive feature:

![]()

Embrace the simplicity of moving through your project's nodes!



## Knowledge Base Enhancements

We've upgraded the knowledge base to now allow changes to document annotations. Tailor annotations to better suit your needs with ease. Check out the improved functionality:

![]()

## **Additional Enhancements**

- Minor bug fixes and technical improvements have been implemented to ensure a smoother user experience.
- Application speed has been optimized, resulting in faster performance and reduced loading times.

We're committed to continuously improving our application to meet your needs and exceed your expectations. Stay tuned for future updates, and thank you for your continued support.



---

# Release - 13.02.2024

_[Table content - see GitBook for full view]_

​

## Enhanced Commenting Capabilities 

To foster better cooperation among users, we've introduced an advanced commenting feature. Now, you have the flexibility to add two types of comments: 

- general comments that aren't tied to any specific node
- node-specific comments for more targeted feedback.

This enhancement is aimed at smoothing collaboration among editors and users, unlocking new possibilities for project development.

![]()

> **INFO:** Stay tuned for our next release, where we will introduce shortcut keys to further enhance your experience with the builder. These shortcuts are designed to make navigation and operation within the application more intuitive and efficient.

## Simplified cURL Integration for Efficient API Interactions

We're excited to introduce a streamlined cURL pasting capability, designed to facilitate easy interaction with APIs through GET and POST requests. This feature enables the direct inclusion of cURL commands into smart function variables, automating the data fetching and submission processes.

![]()

## **Cursors Upgraded for Precision and Ease**

Following valuable user feedback, we've rolled out new cursor options to improve interaction with the application:

- The Default Cursor activates modal views of nodes upon selection.
- The Hand (Move) Tool allows for seamless movement without interacting with node modals.
- The Comment Insertion Cursor enables you to effortlessly add comments exactly where you need them.

![]()

## **Fixed edge links names**

The edge link name will always follow your connections between nodes now. This streamlines a more cleaner and user-friendly connections. This used to be an issue in past, now it´ s solved.

![]()

## **Adding the File to Top navigation**

We've reimagined the top navigation to streamline user flow and enhance accessibility. Highlights include a new import feature for *.zip files, expanding the file dropdown panel with exciting new functionalities.

![]()

## **Training Set Editing in Answer Node**

Editing training sets is now more intuitive than ever. With the "Open Training Set" feature, you gain a clearer overview of the utterances used in training sets, allowing for more precise adjustments.

![]()

## **Additional Enhancements**

- Minor bug fixes and technical improvements have been implemented to ensure a smoother user experience.
- Application speed has been optimized, resulting in faster performance and reduced loading times.

We're committed to continuously improving our application to meet your needs and exceed your expectations. Stay tuned for future updates, and thank you for your continued support.



---

# Release - 30.01.2024

## Digital Agent overview

_[Table content - see GitBook for full view]_

## Personalized Notepad: 

Introducing a notepad feature for project specific notes, enhancing your project creation experience. Take notes during meeting with client, or just write down what still needs to be done for that project.

![]()

## Undo/Redo Functionality: 

Newly added undo and redo buttons allow you to easily revert or repeat changes. You can undo up to 10 last actions.

![]()

## Document Upload via Bubble:

Uploading documents is now supported using choosing "Allow file upload" advanced feature for ANS node. Default is OFF, it needs to be used for each ANS node, where you want to allow the upload. Document is stored as Base 64 string in the uploaded_document variable.

![]()

## OPEN AI Multilanguage Support: 

We now support OPEN AI's multi-language voices, where you can choose from 6 available voices. Important - STT is not multilingual yet.

![]()

## Enhanced Flow Navigation & Create new in new modal: 

Easily navigate your flow with the 'go to next' feature and directly access Target nodes from an open node to track conversation flow. Additionally, create new nodes within an existing node for enhanced organization.

![]()

## See the training set in each modal in table form: 

Discover where your training set is utilized instantly in the training set overview.Explore this feature now!



![]()

## Improved Search Functionality: 

Our enhanced search now displays both 'text' and 'speech' inputs and variables, offering a more comprehensive search experience

![]()

## **Additional Improvements:**

- Zoom Function Enhancement: Resolved issues with the zoom function, ensuring a smoother user experience.
- Small bug fixes



### **Born Digital product team! **
