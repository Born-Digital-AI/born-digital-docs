# Best practices for writing training set

Outline for best practices for developing a robust training set

Creating an effective training set is crucial for the success of any AI-driven system, especially in conversational AI. A well-crafted training set ensures that the model accurately understands user intents, responds appropriately, and continuously improves over time. I

In this section, we will outline best practices for developing a robust training set, covering guidelines on data diversity, labeling consistency, and balancing between overfitting and underfitting. By following these practices, teams can build more reliable, scalable, and efficient AI models that enhance user experience and meet business objectives.

1. Diversity of Utterances: 
Include a wide range of phrases and variations for each intent. This helps the model understand different ways users might express the same request. Consider different dialects, regional variations, and slang that users may employ.
2. Use Real User Data: 
Whenever possible, use real interactions from users to create training data. This ensures the training set reflects genuine language patterns and user behavior.
3. Balance Intent Representation: 
Ensure that all intents are adequately represented in the training set. Avoid over-representing some intents while neglecting others, as this can lead to biased performance.
4. Contextual Examples: 
Include examples that reflect different contexts in which the intents might be used. This helps the model understand when and how to apply specific intents.
5. Label Clearly: 
Make sure each utterance is clearly labeled with its corresponding intent. Consistent and clear labeling is essential for effective training and evaluation.
6. Include Edge Cases: 
Incorporate edge cases and less common utterances to improve the model’s robustness and ability to handle unexpected inputs.
7. Iterative Improvement: 
Regularly review and update the training set based on model performance and user feedback. This iterative process helps improve accuracy over time.
8. Testing and Validation: 
Create a separate validation set to test the model’s performance on unseen data. This helps ensure that the model generalizes well and doesn't just memorize the training examples.
9. Avoid Ambiguity: 
Strive for clarity and specificity in the examples. Ambiguous phrases can confuse the model and lead to incorrect intent classification.
10. Documentation: 
Keep thorough documentation of the training set, including the rationale for chosen examples and how they relate to user intents. This can help future modifications and training efforts.
