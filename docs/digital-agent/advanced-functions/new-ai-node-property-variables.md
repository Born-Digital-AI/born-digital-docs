# New AI node property variables

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

![]()
