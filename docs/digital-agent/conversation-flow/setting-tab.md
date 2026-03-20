# Setting tab

Our goal is to ensure a seamless onboarding experience for the Digital Agent and the comprehensive suite of Digital Studio products.

Within the project settings, personalization options are available, but some are specifically designed for advanced users. It's essential to proceed carefully and have a thorough understanding before making adjustments.

> **INFO:** Before delving into settings, it's recommended to save the current version in case of any issues. You can easily revert changes at any time using the [Project Version History]() feature.

![]()

## **Basic Project Settings Include Three Categories:**

1. Configuration: Customize project settings such as project description, the starting node of the flow, and advanced configurations.
2. Vocabulary: Customize the vocabulary used within the conversation flow.
3. Stopwords: Add specific words that halt or stop the conversation flow when encountered.

For more detailed information and guidance regarding each setting, explore the specific sections within the project settings. Taking a cautious approach while modifying settings ensures a smooth and optimal project configuration.

---

## Configuration

![]()

****

****

****

****

****

****

****

****

****

## 

## Vocabulary

The Vocabulary feature serves as a dictionary of corrections used during utterance processing. It allows users to specify custom corrections for words or phrases, which take precedence over the default corrections provided for each language.

![]()

**Key Concepts:**

1. **Custom Corrections:**

- Users can define custom corrections by specifying key-value pairs. The key represents the word or phrase to be corrected, while the value indicates the replacement text.
2. **Case Sensitivity:**

- Vocabulary corrections are case-sensitive. Each key is matched against the input utterance as a whole word, ensuring that partial matches of syllables within words are not corrected.
3. **Regular Expressions:**

- Vocabulary supports the use of regular expressions, enabling users to provide multiple word forms or patterns with a single correction entry.
4. ### Sequential Evaluation of Vocabulary Corrections

The Vocabulary feature evaluates corrections sequentially in the order they appear in the configuration. This means that if multiple corrections conflict, the correction listed first will be applied. Therefore, it is not advisable to order corrections alphabetically.


Example: Suppose we have the following corrections:

- `"Hello" corrected to "Greeting"`
- `"Hello World" corrected to "bonus program Hello word"`

If the input sentence is "I am interested in Hello World", the first correction will be applied, transforming the sentence into "I am interested in Greeting World". The second correction will not be applied because "hello world" is no longer present in the sentence. This can potentially impact intent recognition, as the sentence has been altered suboptimally.

** ****Here are some tips for custom vocabulary use-cases:**

****

****

****

****

****

****

****



## Stopwords

Stopwords are common words in a language that are typically filtered out during text processing as they do not carry significant meaning and are unlikely to contribute to the understanding of the text. Examples of stopwords include articles, conjunctions, and prepositions.

![]()

**Importance of Removing Stopwords:**

- Enhances Text Processing: By removing stopwords, text processing algorithms can focus on more meaningful content, improving the accuracy of tasks such as sentiment analysis, topic modeling, and text classification.
- Reduces Noise: Stopwords often occur frequently in text but convey little semantic information. Removing them helps reduce noise and extract the most relevant information from the text.

**Key Features of Stopwords Handling:**

1. **Default stopword list:**

- For each language, a default list of stopwords is provided. These lists contain common stopwords in the respective language.
2. **Stopword removal configuration:**

- Stopword removal can be toggled on or off in the project configuration. This allows users to customize whether stopwords are removed during text processing.
3. **Custom stopword list:**

- Users have the flexibility to specify a custom list of stopwords. In cases where the default stopwords do not suit the project's requirements, the custom stopword list takes precedence. The custom list is used for stopwords removal, and the default list is ignored.
4. **Preprocessing order:**

- Stopword removal is one of the initial preprocessing steps. If stopwords are removed, subsequent preprocessing steps such as vocabulary corrections do not operate on them, as they are already eliminated from the text.
