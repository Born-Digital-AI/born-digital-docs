# Knowledge base

Learn how the Knowledge base empowers your digital agent by providing the necessary information to answer your users` questions by leveraging both Generative AI and Internal knowledge.

# Creating a Knowledge base

Knowledge base files typically contain internal information, customer queries (FAQ), and specific answers based on previous analysis. It can also contain internal documents like General Terms and Conditions, Privacy Policies, NDAs agreements, and more. The Knowledge base is a vital component of our ['AI' node](), allowing us to extract knowledge from it and use OpenAI's generative solutions to provide answers.

In this chapter, we'll guide you through creating, managing, and utilizing Knowledge base index files.

## Creating an new index

![]()

****

## Gathering knowledge

Collect relevant information from various sources such as FAQs, manuals, documentation, and subject matter experts. Ensure that the gathered data is accurate, up-to-date, and aligned with the intended purpose of the digital agents.

### Method 1: Uploading text documents

You can easily upload knowledge from text documents directly from your computer. 

![]()

****

> **WARNING:** Each file must be under 100 MB, and the entire upload should not exceed 200 MB.

Before uploading a document to the index, you have the option to configure parsing settings to tailor the integration process according to your requirements. 

### Parsing options

1. No parsing: Selecting this option will bypass any parsing of the document content. The document will be uploaded as-is into the index.
2. Simple parsing (No LLM): This is the default parsing option recommended for most scenarios. It involves basic parsing without utilizing large language models (LLMs).

Simple Parsing Method - Delimiters: You can now split documents by setting a delimiter (ENTER or double ENTER). The document will be divided into snippets based on the chosen delimiter. Default delimeter means snippets will be parsed with the same approach as before

> **INFO:** Use this method in case you have a clear TXT document (for example FAQ type), where you have paragraphs of text woth questions / answers and you have ENTER or double ENTER between the paragraphs. Created snippets will be then created based on these paragraphs

![]()

1. Advanced Parsing: This option involves parsing the document content using large language models. However, it's essential to consider the potential cost implications, as utilizing LLMs can significantly increase token consumption and, consequently, expenses.
2. Custom Parsing: Select specific areas to split into snippets using the SHIFT + ENTER command, allowing for more control over how the snippets are creating. For now, upload just one document at a time if you want to use this method

> **INFO:** When you upload your document, set the Custom parsing method and you press Upload -> txt version of the document will be shown to you on the next page, where you can decide by yourself how the snippets will be created

![]()

​

### Chunk size



You have the flexibility to adjust the chunk size parameter, which determines the size of text portions processed during parsing. The default chunk size is set to 300 tokens.

**Best practices**

- Unless specifically required, utilize the default option of simple parsing (no LLM) to minimize costs and token consumption.
- Adjust the chunk size parameter based on the size and complexity of the documents being parsed to optimize processing efficiency.
- We recommend using *.txt, .html, .json, or .pdf files for optimal results. *.docx files have a different code structure and may produce lower-quality outcomes.

### 

# Method 2: Webscrapping / webcrawling

Web crawling enables you to extract knowledge from websites and integrate it into your knowledge base. Here's how to do it:

![]()

****

### Current Limitations

- **Security issues have been identified on several websites, including financial and banking sites containing sensitive data. The latest technology, including web scraping tools, cannot access content on these sites due to enhanced security measures and scam prevention. Additionally, concerns regarding compliance with cookie and privacy policies have been reported on multiple websites. Current technologies, such as ChatGPT 4.0, are also affected by these limitations.**
- No Automatic Refresh or Sync: Currently, the platform does not support automatic refresh or synchronization for web scraping. Users must manually refresh the scraping process to update the content.
- Static Web Pages Preferred: Web crawling, which is essentially web scraping of pages, may not yield the best results for pages with dynamic fields, values, or information. It's more suitable for static web pages as a quick and easy solution to initiate the knowledge base.
- Inconsistent Information Retrieval: The effectiveness of web scraping depends on the structure and design of the target website. If the website is poorly constructed or has inconsistent formatting, the extracted information may not be accurate or useful.
- HTML Formatting: Web scraping retrieves content in HTML format, including tags, which can affect searchability in the index and, the number of snippets needed to attain necessary information and increase token consumption during processing in the flow.
- Language processing dependencies on website code:  Web scraping for website content in a language that employs special accented characters in its alphabet will proceed correctly only when the HTML code of the website includes language information.

> **DANGER:** Web scraping is not a suitable method for building a knowledge base if your website contains files other than HTML code, such as PDFs. Text files can be uploaded directly into the index.

> **WARNING:** When constructing a knowledge base through web scraping, if the content is in language other than English, e.g. Czech, it is essential to ensure that the respective website has the language in HTML code defined, e.g. as <head lang="cs-CZ">. Otherwise, it will be processed as if it were in English, potentially leading to difficulties in processing characters with diacritics.


**The same principle applies to other languages utilizing accented or special characters within their alphabets.**

![]()

### Best Practices

- Use APIs Where Possible: Instead of relying solely on web scraping, consider utilizing APIs (such as FETCH_URL) provided by websites whenever available. APIs offer a more reliable and structured way to access data and ensure consistency in information retrieval.
- Consider Dynamic Content: Evaluate the nature of the content on the target website before opting for web scraping. If the website contains dynamic fields or frequently updated information, web scraping may not be the most suitable approach.
- **Leverage ChatGPT-4 Analysis: We recommend building indexes using GPT-4 analysis of the web. This approach leverages advanced language models for enhanced understanding and extraction of information. However, it's important to note that utilizing GPT-4 analysis may result in increased costs.**

 While web scraping capabilities may not deliver the best outcomes yet, our team is continuously working to enhance and optimize this functionality. Stay updated on platform updates and improvements to leverage the latest advancements!

> **INFO:** **General tips for building strong knowledge:**

- Start with a general_faq index for common questions and information, then create more specific, smaller indexes to address specific fields within the conversation flow.
- Shorter and well-structured documents tend to perform better within the knowledge base. Ensure that documents are concise, organized, and focused on providing clear and relevant information.
- Currently, our platform can only process textual input. When creating content for the knowledge base, focus on textual information such as FAQs, manuals, guides, and articles. Avoid including non-textual elements such as diagrams, images, or infographics, as they will not be processed by the system.
- Whenever possible, structure the content of the knowledge base using headings, bullet points, and numbered lists. This enhances readability and makes it easier for users to navigate and extract relevant information.
- If you need to input tables into the knowledge base, for better interpretation of its content by LLM, it's preferable to insert the table in Markdown or HTML format.
- Uploading PDFs that are converted from images or contain graphical elements (such as background images) may not be processed correctly, or the platform may reject the file for indexing.

---

# Managing the Knowledge base

Once you've created an index, you can efficiently manage it by utilizing four key buttons:

## Open index and upload more docs

Click this icon to access and view the current index. This way, you may add other documents to your existing index and build your knowledge base bit by bit.

![]()

## Copy index

Click on  icon to duplicate the selected index for creating backups or making variations.

![]()

> **INFO:** Having administrative privileges within your organization or an editorial role across multiple projects, or being the owner of several projects within the organization, grants you the ability to copy an index across projects. 

Simply click on the dropdown arrow during duplication and select the project to which the copied index should be assigned.

## Export/Import Index 

We have enhanced our Knowledge Base tab to allow you to easily export and manage indexes. You can now export one or multiple indexes with a simple click. Additionally, we've updated the functionality to ensure that the exported indexes can be seamlessly re-imported.

Copy indexes functionality can be also used if you just want to copy the index (either to the same, or other project).

> **INFO:** **This will help you to move your fine tuned index from Test to Prod for example. All content of your index is exported (incl. snippets) and are uploaded to the new environment in the same way. You can also export and import whole project configuration, which includes also indexes now**

![]()

## Edit index

When you want to edit an index, click on the pencil icon . This will open an overview of individual documents. 
In this overview, you'll see document names, and annotations that were automatically generated. You can also view the number of tokens contained in the documents, among other details.

![]()

You can manage the entire index or focus on editing specific files within. You can filter the overview, add tags, download documents from the index, delete, or edit their content.

To maintain clarity, it's recommended to name your files in a way that reflects their content.


### Editing Documents

Documents can be edited by clicking on the pencil icon. This opens a text window where you can rewrite the document's annotation, the document text itself, or add/remove tags.

![]()

> **INFO:** Tip! 
When you press CTRL + F with the editing window, you can search the document's content. The search feature supports regular expressions , case sensitivity , whole word search , and searching within the selected text .


Pressing CTRL + H opens up the find and replace function within the document. This functionality provides a convenient way to edit and modify text within the document efficiently.

### Editing Snippets

**If parsing was enabled during index creation, each document was segmented into snippets. Each of these snippets can be edited individually.**

![]()

If needed, you can download the index documents and data to gain insight into its contents.

You can download documents:

- Individually by clicking on the download icon.

![]()

- In bulk by selecting multiple documents and clicking on the same icon in the table header.

![]()

- If "Select All" is chosen in the multi-select mode, the entire content of the index including metadata will be downloaded as a .zip file.

![]()

### Individual labelling

To add labels individually to a single document open the document for editing. Scroll down to the tag field and input the desired tags. You can create labels by clicking into the field, typing the label name, and pressing enter. A document can have multiple tags.

![]()

### Bulk Labelling 

**For adding the same tags to multiple documents simultaneously:**

- First, select the documents to which you want to add tags. (If you want to add a tag to all documents, simply use the "select all" option in table header.)
- Then, click on the pencil icon in the table header.
- Fill in the labels and click on save. This action will add the specified tags to all selected documents.

![]()

To delete a document from the index, look up the document and simply click on the trash bin icon. Make sure you've selected the right document before confirming deletion!

![]()

If you need to delete multiple documents at once, you can select them in the multi-select mode and then click on the trash bin icon in the table header.

![]()

## Delete index

By clicking on icon, remove the index when it's no longer needed.

![]()

> **WARNING:** **Be cautious when deleting a Knowledge base index, as this action cannot be undone **

---

# Integrating Knowledge base into a conversation flow

Integrating the knowledge base into the conversational flow is a crucial aspect of enhancing the capabilities of the digital agent. This integration is achieved through the AI node.

![]()

****

> **WARNING:** Without enabling the Knowledge base function and choosing the source index, the digital agent won't have access to any customized knowledge you've prepared. In this case, the LLM will use its pre-trained general knowledge and make answers on the spot, or it may even start hallucinating.

---

# Creating the index sources

Requirements: ChatGPT4.0

Please note that this is for testing and workflow purposes only, as ChatGPT may face challenges when handling more than 50 rows in a single sheet.

## Prompt #1 - Generate txt files

Copy and paste the text below to see the example:

---

You are an automated task manager specialized in data processing. Your task today involves handling an uploaded Excel spreadsheet to create individual *.txt files based on its content. Before you proceed, please carefully review the following instructions:

1. Ignore the First Row: The first row of the spreadsheet is the header. Do not create a .txt file for this row.
2. Column 'File_name': Use the data in this column as the name for each .txt file.
3. Column 'Body_header': This column contains data that should be placed as the first line in the body of the text file.
4. Column 'Body_subheader': The contents of this column should follow as the second line in the text file's body.
5. Separate Files: Generate a distinct .txt file for each row in the Excel sheet, excluding the header row. The file name and content should be derived from the relevant columns as specified.

Now, with these instructions in mind, please process the inserted *.xlsx file and create a separate .txt file for each row following the guidelines provided.

---

## Prompt #2 - Generate zip file

Please copy this text below:

---

Your next task as an automated file manager involves a crucial step of archiving. After successfully creating individual *.txt files from the Excel spreadsheet, it's time to consolidate them. Please follow these instructions to proceed:

1. Gather All .txt Files: Locate all the .txt files you've just created from the Excel sheet. Ensure none are missed.
2. Combining Files: Combine these individual .txt files into a single archive. The format for this archive should be *.zip.
3. Naming the Archive: Name the .zip file in a way that clearly identifies its contents or its source (for example, 'Processed_TextFiles.zip' or a name that reflects the project or date).
4. Checking for Completeness: Before finalizing the archive, ensure that every .txt file is included in the .zip file. This step is crucial to maintain data integrity and completeness.
5. Final Output: Once the .zip file is created and all files are confirmed to be included, your task is complete. The archive should now be ready for storage or distribution as required.

Please proceed with these steps to create the combined *.zip file from the individual text files.

---

# FAQs and troubleshooting

****

****

****

****

****

****

****

****

****

****

****
