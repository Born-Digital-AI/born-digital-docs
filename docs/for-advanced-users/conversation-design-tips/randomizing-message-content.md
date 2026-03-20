# Randomizing  message content

Insights and guidelines on the effective implementation of randomization techniques to diversify and enhance the content of digital agent's messages.

# Message roulette:  Crafting varied responses

Discover how introducing variability in message content can contribute to a more engaging and dynamic user experience, improving the overall effectiveness of your chatbot interactions.

**Why a single well-crafted message might not be enough:**

- User Engagement: Varied and dynamic responses prevent conversations from becoming monotonous or predictable. Users are more likely to stay engaged and interested when the chatbot's responses are diverse and not repetitive.
- Human-like Interaction: A broader range of alternatives contributes to a more natural and human-like conversation. Mimicking the way humans express themselves makes interactions with the chatbot feel more authentic and relatable.
- A/B Testing Opportunities: Having multiple alternatives provides opportunities for A/B testing. This allows you to experiment with different messaging approaches and identify which ones resonate best with your audience, leading to continuous improvement in the chatbot's performance.



> **WARNING:** Currently, configuring alternatives for message content is not available as a user-friendly feature on our Flow editor GUI. Don't worry, this functionality is on our roadmap! While not as straightforward as a few clicks, here are detailed instructions on [method 1]()or[method 2]() and how to achieve this with the use of our smart function and some clever flow design

Thanks for your patience; we're crafting something amazing!

> **SUCCESS:** Tip: However, you can effortlessly configure multiple outputs for your chatbot. See .

Experiment with having multiple chat bubbles displayed in a sequence to enrich your chatbot interactions with dynamism and engagement.



---

# Method #1: Randomize the path to the next MSG NODE

This method involves creating a randomized decision tree where the chatbot dynamically selects its path based on random decisions. While it requires more clicks as you set up and maintain multiple nodes in the flow, the advantage lies in the visibility of the decision-making process.

![]()



## Step 1: Set up messages

1. Prepare multiple MSG nodes, each representing a potential message in the conversation. 
If you need to go through some MSG node basics first, check out

![]()

## Step 2: Insert the point of decision

1. **Introduce a DEC node before the MSG nodes to serve as the decision point.
**

![]()
2. **Within the DEC node, set up a new variable. Let's name it random_number. Use the smart function random_int to generate a random number which will be saved in random_number variable.**

![]()

1. Establish conditions in the DEC node to guide the subsequent path based on the randomly generated value.
Don't forget to set one of the MSG nodes as a fallback target, in case none of the conditions are met.

![]()

****

Within this step, the smart function random_int generated a whole number from 1 to 3 (included). The value is saved into random_number variable. Based on its value, one of the conditions is fulfilled and the next node is selected accordingly. In case of error when all conditions fail, flow continues to set fallback target node (Other).



## Step 3: Tie the paths back together

1. **Set the next target from all MSG nodes.**

![]()



## You're done!

![]()



---

# Method #2: Set the message content with variables

This method involves configuring the content of MSG nodes as variables. Utilizing the random_int smart function, the variable is set based on the outcome of the randomization. The variable is then used as input for the MSG node, and the content is dynamically populated based on the variable value.

![]()

While this method streamlines the process within a single node, reducing the complexity of the flow diagram, it requires more coding. 
Keep in mind that the intricacies of this method might not be immediately apparent when viewing the broader flow diagram. Working with string variables within this setup imposes restrictions on Markdown and formatting options for chatbot outputs.

## Step 1: Use random_int smart function

1. In the MSG node, create a new variable. Let's name it random_number.
2. Employ the random_int function to determine the variable value randomly.

![]()

## Step 2: Set a new variable

1. Set a new variable for the content of your message. Let's name it message_content.
2. `Set the value of the variable as a string, based on the results of randomization which is stored in random_number.`
3. Use if... else.. format.

![]()

****

## Step 3: Assign variable as input for message

1. Use the message_content variable as input for the MSG node, allowing the content to be dynamically filled based on the variable value.

![]()

## You're done!

![]()
