# Customizing speech synthesis

Tailor your assistant's speech to echo your brand's unique tone and personality. With a suite of customization tools, you can fine-tune pitch, speed, accents, and even add a sprinkle of emotion.​

# Let´s start with it

![]()

Craft compelling texts for your digital voice assistant. Insert your message into the Speech text window in the Message node.

****



---

# Speech synthesis markup language (SSML)

**Get ready to fine-tune your digital assistant's voice with some SSML magic!  ** Let's play with pitches, pauses, and personalities. 

SSML stands for Speech Synthesis Markup Language, and it is an XML-based markup language used to control the synthesis of text-to-speech output. SSML provides a way to specify the pronunciation, intonation, and other aspects of the synthesized speech, giving developers fine-grained control over how the text is spoken.

Some examples of what can be controlled with SSML include:

- Voice selection: You can choose from a variety of pre-defined voices, including different genders, accents, and languages, or even specify a custom voice using SSML.
SSML is used in a variety of applications, such as voice assistants, text-to-speech software, and automated voice response systems, to provide a more natural and user-friendly experience for users.
- Pronunciation: You can specify the pronunciation of a word or phrase, including how individual phonemes should be pronounced.
- Prosody: You can control the pitch, volume, and rate of the speech, as well as insert pauses, emphasis, and other effects to give the synthesized speech a more natural-sounding intonation and rhythm.



---

# SSML tags

In the context of SSML, tags are elements of XML markup language that are used to provide instructions for controlling the synthesis of text-to-speech output. These tags are enclosed within angle brackets (< and >), and are used to define specific elements or attributes that are recognized by SSML processors.

## Generally, there are two types of tags:

Pair tags, also known as start tags and end tags, consist of two tags that surround a block of content. The first tag is the start tag, and it begins with the name of the element enclosed in angle brackets (< and >). The second tag is the end tag, which begins with a forward slash (/) followed by the name of the element enclosed in angle brackets. 

Pair tags define an element that has a beginning and an end, and the content between the tags is considered to be the value of the element.

<prosody> -  start tag
</prosody> - end tag

`<prosody> ... </prosody>`

```ssml
This sentences in not affected by SSML. <prosody> This sentence is modulated with prosody. </prosody> This sentence is no more affected by SSML, as second sentence was enclosed with end tag.
```

Non-pair tags, also known as empty tags or self-closing tags, consist of a single tag that does not surround any content. 

Non-pair tags are used to indicate that an element does not have any content but may have attributes. Non-pair tags end with a forward slash (/) before the closing angle bracket (>).

```
... <break time="2s"/> ...
```

```ssml
This is part before the break <break time="50s"/> and this is part after the break
```

****

## Taking the closer look

Delve into the Essential SSML Tags: Enhancing Your Assistant's Voice with Tag Mastery

<break> allows you to insert a pause in the speech. The time attribute specifies the duration of the pause, and the strength attribute specifies the strength of the pause.

| Exemple | Descripton |
| --- | --- |
| <break time="10ms"/> | Pause of 10 miliseconds |
| <break strength="strong"/> | Pause of set strenght Possible attribute values: x-weak, weak, medium, strong, x-strong |
| <break time="500ms" strength="weak"/> | Pause od 500 milliseconds and set strength |
| <break time ="50%"/> | Pause lasting 50 % of default |
| <break time = "1"/> | Pause of 1 second |

<emphasis> allows to emphasize a particular word or phrase in the speech. The l. .evel attribute specifies the level of emphasis, which can be either "strong" or "moderate".

<prosody> allows to adjust the pronunciation, volume, and speaking rate of the speech. The pitch, range, rate, and volume attributes can be used to adjust these aspects of the speech.

| Exemple | Description |
| --- | --- |
| <prosody rate="+5.00%"> ... </prosody> | Changing rate, increasing by +5 % |
| <prosody rate="+5.00%"> ... </prosody> | Changing rate, to slow Possible attribute values: x-slow, slow, medium, fast, x-fast |
| <prosody pitch="+5.00%">...</prosody> | Changing voice pitch, increase by +5 % |
| <prosody pitch="hight>...</prosody> | Changing voice pitch, to high Possible attribute values: x-low, low, medium, high, x-high |
| <prosody volume="+5.00%">...</prosody> | Changing volume, increasing by +5% |
| <prosody volume="soft">...</prosody> | Changing volume, to soft Possible attribute values: x-soft, soft, medium, loud, x-loud |
| <prosody emphasis="strong">...</prosody> | Setting emphasis, to strong Possible attribute values: none, moderate, strong |
| <prosody contour="(0%,+10%)(50%,+50%)(100%,+10%)">...</prosody> | Adjusting contour of speech |

<say-as> allows to specify how a particular string of text should be pronounced. The interpret-as attribute specifies the type of text to be interpreted, and the format attribute specifies the format of the text. The detail attribute can be used to provide additional information about how the text should be pronounced.

| Exemple | Description |
| --- | --- |
| <say-as interpret-as="xxx">...</say-as> | Attribute interpret-as set rule for entity Possible attribute values: date, time, digits, character, spell, address, telephone, name, URL etc. |
| <say-as interpret-as="xxx" format="yyy">...</say-as> | *Setting format for attribute, could be also set as "Undefined" interpret-as Ex. <say-as interpret-as="date" format="md">9/1</say as> set format for entity date as month-day Pronounced as: September, 1st* |

<phoneme> allows to specify the pronunciation of a particular phoneme. The alphabet attribute specifies the phonetic alphabet being used, and the ph attribute specifies the phoneme to be pronounced.

| Exemple | Description |
| --- | --- |
| <phoneme alphabet="ipa" ph="bɔˈɹn.dɪˈ.dʒɪ.təl.">Born Digital</phoneme> | Attribute alphabet sets IPA (international phonetic alphabet) Attribute ph sets phonemes be pronounced Phonemes are transcribed with IPA Born Digital = [bɔˈɹn.dɪˈ.dʒɪ.təl.] |

<sub> allows you to substitute one word or phrase for another. The alias attribute specifies the replacement text, and the content between the start and end sub-tag represents the text to be replaced.

| Exemple | Description |
| --- | --- |
| <sub alias="Born digital">BD</sub> | *Substitues text with set alias Ex. BD with alias Born Digital* |



---

## Tags usage

SSML code is written in XML format and is typically embedded within the text of the document that is being processed by a text-to-speech system. Here's an example of what SSML code might look like:

> Hey there' <prosody rate ="slow">I'm your friendly virtual assistant. </prosody> <break time="500ms/><prosody volume="loud"> How can I help you today?</prosody>

To use SSML-enriched text as output in your digital assistant, copy it in the Speech window in MSG_NODE in the Flow editor.

![]()

![]()



---

# Tips and trick

Copywriting for your digital assistant should be simple and straightforward to make it easy for users to understand. It is essential to use clear and understandable questions that help the customer formulate their answers. If possible, it is helpful to use the same natural language and words, phrasing, and lexicon that are commonly used in everyday life. This will make it easier to communicate with the voicebot.

## **Keynotes:**

| isCh78qj7ijj |
| --- |
| In the case of voicebot, you do not have to stick to spelling and grammar as in other types of communication. Of course, spelling and grammar are still important and have a very strong influence on synthesis quality. |
| However in some cases, grammatically, orthographically and typologically correct text can lead to a result that is not pleasant to listen to, negatively affecting intonation and spoiling the quality of the synthesis. |
| Therefore, work consciously with this characteristic of the synthetic voice and make "mistakes" on purpose.  E.g., deleting or adding commas in a sentence, can significantly improve to the quality of the synthesis. |
| Deliberately using the wrong spelling can also have its advantages and, in some cases, improves the pronunciation of certain words or phrases. |

# Copywriting structure

### Sentence structure

The two basic components of a sentence are topic (téma) and comment (rhéma). The topic is the word or group of words that determine what the sentence is about, while the rheme is part of the sentence that follows and completes the topic. For example, in the sentence "My dog's name is Max", the topic is "My dog" and the rheme is "is named Max". Topic and rheme are important for proper sentence construction and are essential for understanding meaning.

> **INFO:** The flexibility in word order is a distinctive feature of Slavic languages, particularly Czech and Slovak, due to their rich inflectional systems.

****

> **WARNING:** In English, German, or other languages word order is usually set, but that does mean that we cannot use this principle to our advantage as well. In English, this principle is reversed, the more important information is put in front:

****

---

## Multiple choice question

```
CZ: Voláte kvůli své objednávce, případně dříve zakoupeného výrobku? Stačí mi jednoduchá odpověď ano nebo ne.Zboží můžete vrátit na prodejně, kurýrem nebo přes zásilkovnu. Kterou z těchto možností zvolíte?EN:Are you calling to unblock your account? Please answer with yes or no.
```

> **INFO:** TIP! In the beginning, before customers get used to the new technology, it is a good idea to provide short instructions on how to interact with the voicebot to avoid confusion and the tendency to press buttons like with IVR.

****



---

## **Multiple questions in a single message**

- If you ask the question at the end of the speech, the customer has already heard all the relevant information and is ready to respond.
- In general, people are more likely to retain the freshest information in their memory, i.e. the information they heard last (see theme).
- This will increase the likelihood that the customer will respond concisely and appropriately, and the voicebot will recognize everything correctly and provide the most complete answer to the customer's query.
- The question asked will indicate to the customer that it is time for him to start talking.

Supporting argument for positioning question at the end of the speech:

```
CZ:Chtěl bych vám nabídnout konzultaci s naším expertem. Ozve se Vám a zdarma Vám provede kalkulaci toho nejvýhodnějšího pojištění. Máte zájem? Rádi bychom Vám poskytli konzultaci zdarma. Ozve se Vám náš expert s kalkulací, které pojištění by pro Vás bylo nejvhodnější. Souhlasíte?
```

```
CZ:Máte zájem o poskytnutí konzultace? Ozval by se Vám náš expert, který zdarma provede kalkulaci nejvýhodnějšího pojištění Vám na míru.
```

Rather, the solution is built on alternating between periods when the voicebot is speaking and not listening (running text-to-speech synthesis) and when the voicebot is silent, listening and evaluating the transcript of the response (running speech-to-text transcription). If the customer speaks without the voicebot finishing speaking, speech-to-speech transcription does not run and part of the response is lost, which can lead to misrecognition of intent.

It's better if the text of the voicebot contains the question at the end of the speech. This will help to prevent the customer from jumping into the voicebot's speech. The solution is not designed to allow the customer to interrupt the virtual assistant, while the voicebot is able to go back and finish the rest of its speech.

> **INFO:** **Remember that achieving natural and expressive intonation in TTS systems can be challenging, as it requires capturing the nuances of human speech. It may take some experimentation and refinement to achieve the desired results.**



---

## Position of the question in digital assistant's message

```
CZ:Zkusíme to znovu? Vyplnil jste všechny údaje správně?Přejete si reklamaci řešit raději písemnou cestou?
```

A question should never be phrased negatively. This is because people are generally more willing to accept positive information and ideas than vice versa. Phrasing the question negatively can reduce the likelihood that the voicebot will correctly understand the customer's answer.

```
CZ:Nechcete to zkusit znovu?      Neudělali jste chybu? Jste si jistý, že jste neudělal chybu?Nepřejete si reklamaci raději řešit písemnou cestou? SK:Nechcete to skúsiť znova?   Neurobili ste chybu?  Nechceli by ste svoju sťažnosť riešiť radšej písomne?EN:Won't you try again?Don't you want to deal with reclamation via e-mail?
```

What would answer yes (ano/áno) mean in this case? Yes, I want or Yes, I indeed don't want to? This situational context cannot be discerned with 100% confidence, so we recommend phrasing questions positively or neutrally.

Question wording is a key element of the voicebot scenario. The wording of the question influences the phrasing of customer's answer, and therefore the intent that must be trained for the virtual assistant to recognize the answer.



### Question formulation

Based on the length of the sentence sometimes the quality of the synthesis can be quite fluctuating, appearing artificial and not very natural. In such cases, it is useful to shorten the copywriting or add or edit some words to the text to make the voice synthesis sound better. This approach can help create a more natural and beautiful voice synthesis without the need for complicated settings or SSML tags.

****



---

# Intonation best practice

Master the art of customizing speech synthesis intonation with SSML on our [dedicated documentation page](). Learn to personalize your AI voice with precision and creativity for a truly tailored and engaging auditory experience!

****

> **INFO:** **Remember that achieving natural and expressive intonation in TTS systems can be challenging, as it requires capturing the nuances of human speech. It may take some experimentation and refinement to achieve the desired results.**



---

## Intonation curve

Text-to-speech synthesis is also able to automatically detect the sentence type and set the corresponding intonation curve. This means that you can easily create a synthesized voice that sounds natural and matches the text you enter accurately. 

> **SUCCESS:** **Pro-tip! ** For neural voices provided by Microsoft Azure, feel free to use the [Audio content creator tool]() in Azure Speech Studio. Fine-tune synthesized speech audio to fit your scenario. Define lexicons and control speech parameters such as pronunciation, pitch, rate, pauses, and intonation

![]()

![]()

- In the dialogue window, you can see the width of each word segment(x-axis) on the intonation curve.
- Keep in mind that longer words contain more vowels and therefore more opportunities for the intonation curve to be modified.
- By default, the intonation curve is represented by a straight line at 0%. However, this does not mean that the basic intonation is completely flat! The tool allows you to adjust the pitch relative to the automatic basic synthesis.
- A maximum of five intonation points can be plotted on the curve for a single section.

In Azure Audio Content Creator, you can adjust intonation in sections, which means you can set intonation for each sub-section, phrase, or word separately, instead of having to set intonation for the whole sentence. This allows you to capture different intonation nuances more accurately and gives you more control over how the neural voice will appear.

![]()

Accentuating intonation allows listeners to distinguish between the different ideas and information contained in a sentence. By adjusting intonation curves, you can highlight important points or emphasize changes in mood or emotion, which will help the listener better understand and remember what the voice is saying.

****

> **INFO:** When adjusting intonation curves, you should consider several factors such as sentence length, rhythm, accent, and the emphasis you want to convey. It is important to remember that intonation is a complex subject and that you need to practice and try different approaches.



---

## Melody patterns

Here are some examples of inflexion patterns you can achieve:

To create a rising intonation pattern, you would place anchor points at the beginning of a phrase or sentence and gradually raise the pitch as you move forward in time. This pattern is commonly associated with questions or uncertainty.

A falling intonation pattern involves placing anchor points at the beginning of a phrase or sentence and gradually lowering the pitch as you move forward in time. This pattern often signals a statement or completion.

You can create a fluctuating intonation pattern by adding anchor points at various positions along the Intonation curve. This pattern involves both rising and falling pitch movements, conveying emphasis or highlighting important information.

A plateau intonation pattern maintains a relatively steady pitch without significant changes. You would position anchor points at similar heights along the curve, resulting in a flat or level pitch. This pattern is often used for conveying neutral or declarative statements.

**Want more detailed tips **

****



---

## Pauses and breaks best practice

### Basics

The <break> tag is used to create a pause of a given length in the text. This tag can be used, for example, to express a pause between words or sentences, which can help to improve the naturalness of the delivery. 

> **INFO:** Azure Audio content creator tool offers both predefined tags and the ability to incorporate breaks of a length of our choosing.



The <break> tag in SSML is used to insert a pause or a break in the speech output. It allows you to specify the duration and the strength of the pause. The <break> tag can be used with the following attributes:

time:
Specifies the duration of the pause in seconds or milliseconds. For example, <break time="500ms"/> inserts a pause of 500 milliseconds.

![]()

strength: 
Specifies the strength or intensity of the pause. It can have values like "none", "x-weak", "weak", "medium", "strong", or "x-strong". The actual interpretation of these values may depend on the specific text-to-speech engine used.

![]()

### Example

- Hello, <break time="500ms"/> how are you today?
- Hello, <break strenght="medium"/> how are you today?

**A normal punctuation dot is an interruption of approximately 200-300 ms. If you find these pauses too long, we recommend replacing the punctuation with a shorter break. Ideally 100 ms, but never less than 50 ms.**

![]()

> **WARNING:** The punctuation must be replaced by SSML break! Putting a break tag after punctuation would paradoxically make the pauses even longer (default punctuation pause length 300 ms + additional break tag length).

By setting different pause lengths, we can influence the rhythm of speech. For example, set a shorter pause between sentences that form a single thought than at the front of different thoughts. Millisecond differences in pause length are almost imperceptible to the conscious human. However the different impression of synthesis is mainly created by the change of rhythm between sections. We can take advantage of this and better separate the individual information.

![]()

![]()

**In the example shown in the figure above, the texting can be divided into the sections acknowledgement → argumentation → call to action → confirmation question. The argumentation consists of several sentences that form a unified train of thought, so it contains shorter pauses. On the other hand, a 100ms gap between sections is more distinctive.**



The break also affects the intonation of the sentence and acts as an intonation dot, i.e. the intonation curve drops at the end.

Sometimes, however, we need to edit a pause between words or parts of sentences without intonating a full stop after the sentence. A softer drop in voice and at the same time a pause are provided by other signs, the most prominent of which is the punctuation mark, and slightly more subtle are the colon, semicolon or dash.

> > Prominent pauses:
> > Něco končí <break strengh = "weak"/> Něco začíná.
> > Něco končí <break time = "100ms" /> Něco začíná.
> > Něco končí. Něco začíná.

> > Softer pauses:
> > Něco končí; něco začíná.
> > Něco končí, něco začíná
> > Něco končí: něco začíná.
> > Něco končí- něco začíná.

It is recommended that these marks be added at the point where the voice drop and short pause are to occur, or that they replace the original punctuation. If the pause is too short, write several of these signs in a row, adding their lengths together.

> > Něco končí,,, něco začíná.
> > Něco končí;; něco začíná.

### Example

![]()

Note that we have applied multiple strategies to improve the quality of the synthesis in the example.

1. We have rewritten the graphical distinction of the options with words (A. ---> option A);
2. Replacing punctuation marks with a break tag of a chosen length;
3. Combining additional punctuation marks between words for finer and shorter pauses with less effect on intonation.

**The question mark serves as a punctuation mark that not only indicates a question but also functions as a pause. When a question is posed, there is typically a brief interruption of around 300 milliseconds.**

However, if the question is followed by additional text, this pause can disrupt the flow of speech and give the impression that the voicebot has finished speaking. To prevent the voicebot and the user from overlapping in their speech, it is important to consider certain strategies for phrasing questions and placing them appropriately within the speech. The chapter on copywriting delves into these strategies in more detail.

Let's review some fundamental principles of good practice:

- **Each message should contain only one question.**
- Each question should focus on a single topic. For example, instead of asking, "Would you like to create a new account and join our Premium Club?" it is better to ask separate questions for each option.
- It is advisable to include the question at the end of the message so that the user has already received all the necessary information.

Let's address one specific case of choice questions (e.g., "Do you want A or do you want B?"). 

In this scenario, it is crucial to ensure good synthesis and emphasize distinctive intonation to convey the question's intent clearly and elicit the expected response. One recommendation is to structure the sentence in a way that presents each option as a separate sentence.

To assess the quality of synthesis, intonation, and the initial impression the question makes, experiment with different writing styles and punctuation. It is possible that breaks or punctuation marks may not provide a sufficiently distinct separation between the two options. In such cases, trying out a question mark after each option could be worth considering.




![]()

Please note that this is not a violation of the rule stating that only one question should be included in each text. It's important to remember that speech synthesis input notation serves a different purpose than regular text and does not necessarily adhere to grammar or spelling conventions. In this instance, it is considered a single question, with each option represented by a distinct intonation pattern that visually resembles a question mark.

In the case of "Do you want coffee? Or do you want tea?" a pause between the two options might be excessively long. Unfortunately, this gap cannot be shortened using the break tag. One possible approach is to remove the space after the first question mark (e.g., "Do you want coffee?Or do you want tea?"). In certain cases, combining the options into one continuous string can be helpful, with the question mark indicating the intonation but without the unwanted extended pause.

However, note that this is just one of the potential solutions and not the only correct way to adjust the intonation in such cases.



---

# Pronunciation best practice

## Phoneme-defined pronunciation

Stress can have a huge impact on pronunciation. 

**When a word is stressed, the stressed syllable is typically pronounced with greater intensity, higher pitch, and longer duration compared to unstressed syllables. Additionally, the quality of vowels in stressed syllables may also be affected, with stressed vowels often being pronounced with more clarity and fullness.**



In Czech, stress is generally fixed on the first syllable of a word. This means that the first syllable receives the primary stress, while the subsequent syllables have secondary stress or are unstressed. However, it's important to note that stress patterns can vary depending on the word and its inflectional or derivational forms.

To provide some examples in IPA (International Phonetic Alphabet), let's consider a few Czech words:

> > "kniha" (book): /ˈkɲɪɦa/
> > The primary stress falls on the first syllable (/kɲ/), making it more prominent in pronunciation.

> > "univerzita" (university): /ˌunɪvɛrˈzɪta/
> > The primary stress is on the second syllable (/ɪv/), while the first syllable (/u/) carries secondary stress. The following syllables (/ɛrˈzɪt/ and /ta/) are unstressed.

> > "překvapení" (surprise): /ˌpr̝̊ɛkvaˈpɛɲi/
> > The primary stress is on the second syllable (/ɛkva/), and the first syllable (/pr̝̊/) carries secondary stress. The final syllable (/ɲi/) is unstressed.

These examples illustrate the general stress patterns in Czech, where the stressed syllables are emphasized in terms of intensity, pitch, duration, and sometimes vowel quality. It's important to consult native speakers or audio resources to further refine your pronunciation and understand the intricacies of Czech stress patterns.

When incorporating English words into the  Czech language, the stress patterns of these borrowed words tend to follow the stress patterns of Czech words. However, there may be some adjustments to fit the Czech stress rules. Here are a few guidelines for handling English words in Czech:

- First-syllable stress: As mentioned earlier, Czech generally has stress on the first syllable of a word. When adopting English words, the primary stress is often placed on the first syllable to align with Czech stress patterns.

> > Example: "computer" in English has stress on the second syllable (/kəmˈpjuːtər/), but in Czech, it would typically be pronounced with stress on the first syllable: /ˈkɔmpjutr/.

- Adaptation of vowel sounds: English vowels can have different qualities compared to Czech vowels. When adapting English words into Czech, the vowel sounds may be modified to match the Czech vowel inventory.

> > Example: "restaurant" in English (/ˈrɛstərɒnt/) could be adapted in Czech as /ˈrɛstaurant/.

- Retaining original stress: In some cases, English words may retain their original stress patterns, particularly when they are relatively recent borrowings or specialized terms that have become familiar to Czech speakers.

> > Example: "hotel" in English has stress on the first syllable (/hoʊˈtɛl/), and this stress pattern is often preserved when using the word in Czech: /ˈhotɛl/.

  Adaptation of English words in Czech can vary depending on individual preferences, language register, and the familiarity of the borrowed word to Czech speakers. Therefore, there can be some variability in how English words are pronounced within the Czech language context.



## Foreign words pronunciation

When using Azure's Speech Studio with neural voices to handle foreign word pronunciation, here are some tips to ensure accurate pronunciation:

- Phonetic spelling: Provide a phonetic spelling of the foreign words using the International Phonetic Alphabet (IPA) or a transcription system familiar to the base language neural voices. This helps the TTS system understand the correct pronunciation of the word.
- Lexicon customization: Utilize the lexicon customization feature in Azure's Speech Studio to add pronunciation rules for specific foreign words. This allows you to specify the pronunciation of each word or phrase more precisely.
- Pronunciation rules: Create pronunciation rules for common patterns found in foreign words. For example, if there is a consistent pattern of stress in the foreign language, you can define rules to apply stress in the appropriate position.
- Contextual cues: Provide additional context within the text to help guide the TTS system's pronunciation. This could include nearby words or phrases that assist in determining the correct pronunciation of the foreign word.
- Test and iterate: After applying the above techniques, listen to the generated speech and identify any mispronunciations. Adjust the phonetic spellings, lexicon entries, or pronunciation rules as necessary and continue testing until the desired pronunciation is achieved.

It's important to note that while these tips can improve the accuracy of foreign word pronunciation in TTS systems, the results may still vary. TTS systems are trained on large datasets and generalize pronunciation based on the language's phonetic patterns. Handling foreign words can be challenging due to the diverse pronunciation rules across languages.

 Examples:

---

Some phrases or individual words from foreign vocabulary are trained in the default text-to-speech model and synthesized is smooth, localized to base language, and pleasant to the ear. Sounds fine without adjustments:

- ***Nejpoužívanější vyhledávač v Česku je Seznam, nikoliv Google.***
- ***Letíme na dovolenou se společností Lufthansa.***
- ***Koupím ojetý renault.***

Other phrases or words can be very similar and comprehensible, with a few tweaks here and there. Even though their pronunciation is nearly correct, this can cause an uncanny valley effect:

- *Ceny maji jako Deutsche bahn, ale služby jako nejposlednější drožka.*

> > deutsche is pronounced correctly like [dɔ͡ɪˈt.ʃɛ.], but bahn sounds like [ba.ɦaːˈ.ẽˈ] and would be needed to be adjusted

- *Potřebuji znát vaši IP adresu.*

> > IP being pronounced like [iːˈ.pɛː], which would be comprehensible, but in the case would be better to adjust English pronunciation to Czech as [a͡j.piː]
> > 🇨🇿Pronunciation of numbers followed by currency signs is quite different from common reading rules.With prices, sums of money, or values, we often omit words describing the decimal order of fractional part ([desetiny, setiny])

> > `19,99 - [devatenáct celých, devadesát devět setin] 19,99 Kč - [devatenáct korun devadesát devět haléřů] v akci jen za 19,99 Kč - [v akci jen za devatenáct devadesát devět] rohlík stojí 1,50,- - [rohlík stojí korunu padesát]`

Azure's speech synthesis recognizes some words or signs for currency

> > `A. Czech currency 100 Kč [sto českých korun] 1000 CZK [tisíc českých korun]`

> > `B. Dollars 10 $ [10 dolarů] 3 $ [3 dolary]`

> > `C. Euros 3 € [3 eura] 1000 € [tisíc eur] 1 € [jedno euro]`

> > `D. British pounds. 1 £ [jedna libra] 3 £ [tři libry] 10 £ [deset liber]`

> > E. Not all international currency symbol are supported (besides few most common they're usually not)

### 

Pronunciation of digits depends on:

- length of a digit string
- input format
- language and neural persona
- SSML rules
- reading rules and their localization
- numeric type (integer, float, ordinal)



## **Integers**

 Czech language

- `If digits have fewer than or exactly 6 digits, they are always read decadically as default, regardless of whether a space separates orders of thousands

1234
1 234
Both numbers are pronounced as: TISÍC DVĚ STĚ TŘICET ČTYŘI
12345
12 345
Both numbers are pronounced as: DVANÁCT TISÍC TŘI STA ČTYŘICET PĚT
123456
123 456
Both numbers are pronounced as: STO DVACET TŘI TISÍC ČTYŘI STA PADESÁT ŠEST
`
- `If digits have 7 or more characters, they are read decadically only if the order of thousands is separated by a space. Numeric string notation without spaces defaults to reading each digit in turn.

1234567 is pronounced JEDEN DVA TŘI ČTYŘI PĚT ŠEST SEDM
1 234 567 is pronounced MILION DVĚ STĚ TŘICET ČTYŘI TISÍC PĚT SET ŠEDESÁT SEDM
123456789 is pronounced JEDEN DVA TŘI ČTYŘI PĚT ŠEST SEDM OSM DEVĚT
123 456 789 is pronounced STO DVACET TŘI MILIONÚ ČTYŘI STA PADESÁT ŠEST TISÍC SEDM SET OSMDESÁT DEVĚT`



- `If we need shorter numbers to be read each digit in turn, there are several ways to do it
A. Add spaces in between
1 2 3 4 5 6 is pronounced JEDEN DVA TŘI ČTYŘI PĚT ŠEST

B. Add commas in between
1, 2, 3, 4, 5, 6 is pronounced JEDEN DVA TŘI ČTYŘI PĚT ŠEST with more distinct pauses between each of them

C. Use SSML alias for spelling (hláskování)
<say-as interpret-as="spell" format="undefined">123456</say-as> is pronounced JEDEN DVA TŘI ČTYŘI PĚT ŠEST`



- `If we need longer number to be read each digit in turn, copywriting input needs to be adapted accordingly

A. Use numeric string without spaces
1234567890

B. Separate each digit with spaces
1 2 3 4 5 6 7 8 9

C. Separate each digit with interpunction
1,2,3,4,5,6,7,8,9

These numbers will be pronounced as JEDEN DVA TŘI ČTYŘI PĚT ŠEST SEDM OSM DEVĚT`

 Slovak language

- If digits have fewer than or exactly 6 digits, they are always read decadically as default, regardless of whether a space separates orders of thousands.

> > `123456
> > 123 456
> > Both numbers are pronounced as: stodvadsaťtri tisíc štyristo päťdesiatšesť`

- **If digits have 7 or more characters, they are read decadically only if the order of thousands is separated by a space. Numeric string notation without spaces defaults to reading each digit in turn.**

> > `1234567 is pronounced [jedna dva tri štyri päť šesť sedem]
> > 1 234 567 is pronounced [jeden milión dvestotridsaťštyri tisíc päťsto šesťdesiatsedem]`

- The maximal length of spaced numerical string which is pronounced decadically is 15 digits (10^14), in EN system for hundreds of trillions, in SK stovky bilionov.

> > `111 222 333 444 555
> > is pronounced [sto jedenásť biliónov ...]`

- Spaced numerical strings longer than 15 digits are pronounced as multiple numbers, each containing 15 digits of less

> > `111 222 333 444 555 666 will be divided as 111 222 333 444 555 | 666
> > [sto jedenásť biliónov ... päťstopäťdesiatpäť | šesťstopäťdesiatšesť`

- If we need shorter numbers to be read each digit in turn, there are several ways to do it

> > `Add spaces in between
> > 1 2 3 4 5 6 is pronounced jedna dva tri štyri päť šesť`

> > `Add commas in between
> > 1, 2, 3, 4, 5, 6 is pronounced jedna dva tri štyri päť šesť with more distinct pauses between each of them`

> > `Use SSML says-as for spelling (hláskování)
> > <say-as interpret-as="spell" format="undefined">123456</say-as> is pronounced jedna dva tri štyri päť šesť`

- If we need longer number to be read each digit in turn, copywriting input needs to be adapted accordingly

> > Use numeric string without spaces
> > 1234567890

> > Separate each digit with spaces
> > 1 2 3 4 5 6 7 8 9

> > Separated each digit with interpunction
> > 1,2,3,4,5,6,7,8,9

> `These number will be pronounced as jedna dva tri štyri päť šesť sedem osem deväť`




 English language

- If digits have fewer than or exactly 6 digits, they are always read decadically as default, regardless of whether orders of thousands are separated by a space.

> > `1234
> > 1 234
> > Both numbers are pronounced as: [one thousand two hundred thirty-four]
> > 12345
> > 12 345
> > Both numbers are pronounced as: [twelve thousands three hundred and forty-five]
> > 123456
> > 123 456
> > Both numbers are pronounced as:[one hundred twenty-three thousands four hundred fifty-six]`

- **If digits have 7 or more characters, they are read decadically only if the order of thousands is separated by a space. Numeric string notation without spaces defaults to reading each digit in turn.**

> > `1234567 is pronounced [one two three four five six seven]
> > 1 234 567 is pronounced [one million two hundred twenty-three thousands five hundred sixty-seven]`

- The maximum length of spaced numerical string which is pronounced decadically is 15 digits (10^14), in EN system for hundreds of trillions.

> > `111 222 333 444 555
> > is pronounced [ one hundred and eleven trillion...]`



- Spaced numerical strings longer than 15 digits are pronounced as multiple numbers, each containing 15 digits of less

> > `111 222 333 444 555 666 will be divided as 111 222 333 444 555 | 666
> > [one hundred and eleven trillion ... five hundred fifty five | six hundred sixty six]`

- If we need shorter numbers to be read each digit in turn, there are several ways to do it

> > `Add spaces in between
> > 1 2 3 4 5 6 is pronounced [one two three four five six]`

> > `Add commas in between
> > 1, 2, 3, 4, 5, 6 is pronounced one two three four five six with more distinct pauses between each of them`

> > `Use SSML alias for spelling (hláskování)
> > <say-as interpret-as="spell" format="undefined">123456</say-as> is pronounced one two three four five six`



- If we need longer number to be read each digit in turn, copywriting input needs to be adapted accordingly

> > `Use numeric string without spaces
> > 1234567890
> > [one two three four five six seven eight nine zero]`

> > If all subsequent triplets are made with 000, the string is read decadically even without spaces
> > 
> > - `100000 - [one million]`
> > - `1100000 - [eleven million]`
> > - `111000000 - [one hundred eleven million]`
> > - `2000000000 - [two billion]`
> > - `123000000000000 - [one hundred twenty-three trillion]`

> > But when zeros cannot be divided into triplets, the numerical string is pronounced one digit at a time
> > 
> > - `123100000000000 - [one two three one zero zero zero ... ]`



- If we need longer numbers to be read decadically, divide orders of thousands, millions, billions, trillions by space

> > - `1 234 567 - [one million to hundred thirty-four thousands five hundred sixty-seven]`
> > - `123 000 000 000 001 - [one hundred twenty-three trillion and one]`



 Polish language


- **If digits have exactly 4 digits.**

> > `A. If we have numbers 1000, 2000, 3000, etc. The numbers are read by Azure neural voices as:
> > 1000 - tysięczny rok – year one thousand
> > 2000 - dwutysięczny rok – year two thousand
> > 3000 - trzytysięczny rok - year three thousand etc. - This is WRONG.
> > 
> > It should be pronounced as:
> > 1000 - tysiąc
> > 2000 - dwa tysiące
> > 3000 - trzy tysiące`

This situation can also occur with other numbers, for example 4999 is pronounce as
cztery tysiące dziewięćset dziewięćdziesiąty dziewiąty rok - this is WRONG.
CORRECT is cztery tysiące dziewięćset dziewięćdziesiąt dziewięć.
Every number needs to be checked!

> > **B.**

| c47d73faeaa84704b14a292c5c517450 | 938838ac108346f1849c0d507ff1ce4e |
| --- | --- |
| **NUMBER** | **OK/NOK** |
| 1234 | OK |
| 2234 | OK |
| 3234 | OK |
| 4234 | OK |
| 5234 | NOK |
| 6234 | NOK |
| 7234 | NOK |
| 8234 | NOK |
| 9234 | NOK |

1..., 2..., 3..., 4... (thousand) are pronounced CORRECT.

5..., 6..., 7..., 8..., 9... (thousand) are pronounced WRONG.

`5324 – pięć TYSIĄCE - correct is pięć TYSIĘCY`

`6234 - sześć TYSIĄCE - correct is sześć TYSIĘCY`

`7324 – siedem TYSIĄCY - correct is siedem TYSIĘCY`

`8324 - osiem TYSIĄCE - correct is osiem TYSIĘCY`

`9324 - dziewięć TYSIĄCE - correct is dziewięć TYSIĘCY`



## Phone numbers

 Czech language

**For the pronunciation of telephone numbers:**

> > `A. Write them down in iso format including prefix
> > Volejte +420 800 148 148
> > is pronounced VOLEJTE PLUS ČTYŘI STA DVACET, OSM SET, STO ČTYŘICET OSM, STO ČTYŘICET OSM`

> > `B. Separate custom sections with interpunction
> > Volejte 800, 148, 148
> > is pronounced OSM SET, STO ČTYŘICET OSM, STO ČTYŘICET OSM
> > Volejte 212-456-789
> > is pronounced DVĚ STĚ DVANÁCT, ČTYŘI STA PADESÁT ŠEST, SEDM SET OSMDESÁT DEVĚT
> > Volejte 800, 54, 12, 12
> > is pronounced OSM SET, PADESÁT ČTYŘI, DVANÁCT, DVANÁCT
> > Volejte 800, 12, 7, 7, 7. 7
> > is pronounced OSM SET, DVANÁCT, SEDM, SEDM, SEDM, SEDM`

> > C. Write them down as alphabetical string
> > Volejte osm set dvanáct čtyři sedmničky
> > Volejte osm set dvanáct sedm sedm sedm sedm

> > `D. Separate sections with spaces, as long it's meant to be pronounced in 3-2-2-2 or 3-2-1-1-1-1
> > 800 54 12 12
> > is pronounced OSM SET, PADESÁT ČTYŘI, DVANÁCT, DVANÁCT
> > 800 54 1 2 1 2
> > is pronounced OSM SET, PADESÁT ČTYŘI, JEDNA, DVA, JEDNA, DVA`




 Slovak language

**For the pronunciation of telephone numbers:**

> > `A. Write them down in iso format including prefix
> > Volajte +421 800 148 148
> > is pronounced VOLAJTE PLUS ŠTYRI DVA JEDEN, OSEMSTO, STOŠTYRIDSAŤOSEM, STOŠTYRIDSAŤOSEM`

> > `B. Separate custom sections with interpunction
> > Volejte 800, 148, 148
> > is pronounced OSEMSTO, STOŠTYRIDSAŤOSEM, STOŠTYRIDSAŤOSEM
> > Volejte 800-148-148
> > is pronounced OSEMSTO, STOŠTYRIDSAŤOSEM, STOŠTYRIDSAŤOSEM
> > Volejte 800, 54, 12, 12
> > is pronounced OSEMSTO, PÄŤDESIATŠTYRI, DVANÁSŤ, DVANÁSŤ
> > Volejte 800, 12, 7, 7, 7. 7
> > is pronounced OSEMSTO, DVANÁSŤ, SEDEM, SEDEM, SEDEM, SEDEM`

> > C. Write them down as alphabetical string
> > Volajte na osemsto dvanásť štyri siedmičky
> > Volajte na osemsto dvanásť sedem sedem sedem sedem




 English language

**For the pronunciation of telephone numbers:**

> > `A. Write them down in iso format including prefix
> > Call +1-212-456-7890 (USA)
> > is pronounced [call plus one - two one two - four five six - seven eight nine zero]
> > Call +44 7911 123456 (UK)
> > is pronounced [call plus four four, seven nine one one, one two three four five six]`

> > `B. For USA, obey domestic 3-3-4 format
> > Call 212-456-7890
> > is pronounced [call one - two one two - four five six - seven eight nine zero]`

> > `C. For the UK, obey area code formatting ( 3-4 digits + 8-7 digits)
> > 020 (London) 1234 5676
> > is pronounced [zero two zero, one two three four, five six seven eight]`

> > `D. To customize pronunciation, separate digits with spaces or punctuation
> > Call 4 4 4 4, 1 2 3, 1 2 3
> > is pronounced [call four four four four, one two three, one two three] with more distinctive pauses between comma-separated sections
> > Call 800, 12, 34, 12, 34
> > is pronounced [call eight hundred, twelve, thirty- four, twelve, thirty-four]
> > Call 800 12 34 12 34
> > is pronounced [call eight hundred one two three four one two thirty-four`

> > `E. For 10-digit phone number (prefix not included), you can use SSML alias with attribute
> > <say-as interpret-as="telephone" format="undefined">1234567890</say-as>
> > [one two three four five six seven eight nine o]`






## Long numerical strings (IDs, codes)

###  Czech language

For pronunciation of long numerical strings (order IDs etc.):

> > `A. Write numerical strings without spaces to be read one digit in turn
> > Objednávka 01304578931
> > Objednávka NULA JEDNA TŘI NULA ČTYŘI PĚT SEDM OSM DEVĚT TŘI JEDNA`

> > `B. Customize pronunciation by breaking it into smaller chunks with interpunction
> > Objednávka 01, 30, 45, 78, 9-3-1
> > Objednávka NULA JEDNA, TŘICET, ČTYŘICET PĚT, SEDMDESÁT OSM, DEVĚT TŘI JEDNA`




 Slovak language

For pronunciation of long numerical strings (order IDs etc.):

> > `A. Write numerical strings without spaces to be read one digit in turn
> > Objednávka 01304578931
> > Objednávka NULA JEDEN TRI NULA ŠTYRY PÄŤ SEDEM OSEM DEVÄŤ TRI JEDEN`

> > `B. Customize pronunciation by breaking it into smaller chunks with interpunction
> > Objednávka 01, 30, 45, 78, 9-3-1
> > Objednávka NULA JEDEN, TRIDSAŤ, ŠTYRIDSAŤPÄŤ, SEDEMDESIAŤOSEM, DEVÄŤ TRI JEDEN`

 English language

For pronunciation of long numerical strings (order IDs etc.):

> > `A. Write numerical strings without spaces to be read one digit in turn
> > Order 01304578931
> > [o one three o four five seven eight one three one]`

> > `B. Customize pronunciation by breaking it into smaller chunks with interpunction
> > Order 01, 30, 45, 78, 9-3-1
> > [zero one, thirty, forty-five, seventy-eight, nine three one]`






## Numeric date notation



** Czech language

Dates are pronounced correctly by default when put down in ISO format:**

> > `A. ISO DD-MM-YYY
> > 01-11-1995
> > 1-11-1995
> > Pronounced as [1. listopadu 1995]`

> > `B. ISO YYYY-MM-DD
> > 1995-11-01
> > 1995-11-1
> > Pronounced as [1. listopadu 1995]`

> > `C. ISO DD.MM.YYYY
> > datum 01.11.1995
> > datum 01. 11. 1995
> > datum 1.11.1995
> > datum 1. 11. 1995
> > Pronounced [as 1. listopadu 1995]`

**
A safe and simple way is to transcribe the date alphanumerically:**

> > `datum 1. listopadu 1995
> > prvního listopadu 1995
> > Pronounced as [1. listopadu 1995]`

> > `prvního jedenáctý 1995
> > Pronounced as [prvního jedenáctý 1995]`


These formats WON'T WORK and will be pronounced incorrectly, even if tagged with SSML alias reading rules for dates

> > - `DD.MM - 1.11. - [jedna hodina jedenáct minut]`
> > - `DD. MM - 1. 11. - [první jedenáctý]`
> > - `DD/MM - 01/11 - [nula jedna lomítko jedenáct]`
> > - `DD/MM/YYYY - 01/11/1995, 1/11/1995 - [nula jedna lomítko jedenáct lomítko 1995]`
> > - SSML alias reading rules not supported

To be pronounced correctly, dates containing only date + month must be written manually

> > prvního listopadu
> > dne 2. listopadu
> > 31. března
> > 17. listopad

 Slovak language

**Dates are pronounced correctly by default when put down in ISO format**

> > `A. ISO DD-MM-YYY
> > 01-11-1995
> > 1-11-1995
> > Pronounced as [1. novembra 1995]`

> > `B. ISO YYYY-MM-DD
> > 1995-11-01
> > 1995-11-1
> > Pronounced as [1. novembra 1995]`

> > `C. ISO DD.MM.YYY
> > datum 01.11.1995
> > datum 01. 11. 1995
> > datum 1.11.1995
> > datum 1. 11. 1995
> > Pronounced [as 1. novembra 1995]`

**
Safe and simple way is to transcribe date alphanumerically**

> > `dátum 1. novembra 1995
> > prvého novembra 1995
> > Pronounced as [1. novembra 1995]`

> > `prvého jedenástý 1995
> > Pronounced as [prvého jedenástý 1995]`


These formats listed below WON'T WORK and will be pronounced incorrectly, even if tagged with SSML alias reading rules for dates

> > - `DD.MM - 1.11. - [jedna hodina jedenásť minút]`
> > - `DD. MM - 1. 11. - [prvý jedenásť]`
> > - `DD/MM - 01/11 - [nula jeden lomka jedenásť]`
> > - `DD/MM/YYYY - 01/11/1995, 1/11/1995 - [jeden lomka jedenásť lomka 1995]`
> > - SSML alias reading rules not supported

 English language

**Dates are pronounced correctly by default when put down in ISO format**

> > `A. ISO DD-MM-YYY
> > 01-11-1995
> > 1-11-1995
> > Pronounced as [the first of November 1995]`

> > `B. ISO YYYY-MM-DD
> > 1995-11-01
> > 1995-11-1
> > UK and US: Pronounced as [the first of November 1995]`

> > `C. ISO DD.MM.YYY
> > date 01.11.1995
> > datum 1.11.1995
> > UK: Pronounced as [the first of November 1995]
> > US: Pronounced as [January eleventh 1995]`

> > `D. ISO DD/MM/YYYY and YYYY/MM/DD
> > 01/11/1995
> > 1995/11/01
> > UK: Pronounced as [the first of November 1995]
> > UK: Pronounced as [Janualy eleventh 1995]`

> > `D. Also
> > Nov,1st 1995
> > November 1st 1995
> > Pronounced as [November first, 1995]
> > 1 November 1995
> > 1 Nov 1995
> > 1st November 1995
> > Pronounced as [the fist of November 1995]`

**
These inputs WON'T BE pronounced correctly**

- `1 st November 1995 - [one es tee November 1995]`
- `date 1. November 1995 - [one November 1995]`
- `November, 1. 1995 - Pronounced as [November one 1995]`
- `01/11 (EN-UK voices) - [zero one eleventh]`
- `1.11.1995 - [one. eleven. 1995]`
- Be mindful of US date format MM/DD

> > - 01/11 (EN-US voices) - [January the eleventh]

- **Various SSML tag says-as formats of attribute date are supported**

> > - `DMY  - US:[November 1st 1995] , UK:[the first of November 1995]`
> > - `MDY: <say-as interpret-as="date" format="mdy">1/11/1995</say-as>- US:[January 11th 1995] , UK:[the 11th of January 1995]`
> > - `MD: <say-as interpret-as="date" format="md">1/11</say-as> - US:[January 11th] , UK:[the 11th of January]`
> > - `DM: <say-as interpret-as="date" format="dm">1/11</say-as>- US:[November 1st] , UK:[the 1st of November]`
> > - MY: <say-as interpret-as="date" format="my">11/1995</say-as>- US, UK:[November 1995]¨
> > - `YM: <say-as interpret-as="date" format="ym">1995/11</say-as>- US, UK:[November 1995]`

## Time notation

 Czech language 

**Standard iso format is supported and is pronounced as time correctly by default**

> > - `HH:mm - 15:52 - [Patnáct hodin padesát dvě minuty]`
> > - `HH:mm:ss - 15:52:25 - [Patnáct hodin padesát dva minut dvacet pět sekund]`
> > - `HH.mm - 15.52 - [Patnáct hodin padesát dva minut]`

**
Whole hours, even if written down digital, are pronounced as analog time**

> > - `HH:00 - 15:00 - [Patnáct hodin]`
> > - `HH:00:00 - 15:00:00 - [Patnáct hodin]`

**
The Czech SI unit system IS NOT SUPPORTED**

> > `Won't pronounce hod or h as hodin/hodiny
> > 15 hod - [patnáct hod]
> > 15 h - [patnáct há]
> > Won't pronounce min or mins as minut/minuty
> > 15 min - [patnáct min]
> > 15 hod 15 min - [patnáct hod patnáct min]`

**
In case you need time to be pronounced as analog or Czech SI units to be pronounced correctly, it is necessary to transcribe your input**

> > - 15 hod → 15 hodin
> > - 15 min → 15 minut
> > - 2 min → 2 minuty
> > - 15:15 → čtvrt na čtyři | čtvrt na čtyři
> > - 12:00 → poledne
> > - 12:30 → půl jedné odpoledne

 Slovak language

**Standard iso format is supported and is pronounced as time correctly by default**

> > - `HH:mm - 16:10 - [šesťnásť hodín desať minút]`
> > - `HH:mm:ss - 16:10:10 - [šesťnásť hodín desať minút desať sekúnd]`
> > - `HH.mm - 16.10 - [šestnásť hodín desať minút]`

**
Whole hours, even if written down digitally, are pronounced as analog time**

> > - `HH:00 - 16:00 - [šestnásť hodín]`
> > - `HH:00:00 - 16:00:00 - [šestnásť hodín]`

*
Slovak SI unit system IS SUPPORTED only for hod and min*

> > `16 hod - [16 hodín]
> > 15 min - [15 minút]
> > 15 h 10 min - [15 hodín 10 minút]`

> > `Won't read properly other SI formats such as
> > 16 h - [16 h]
> > 10 s - [15 s]
> > 10 sek - [10 sek]`

> > `If you need word seconds to be pronounce, write that down manually
> > 16 hod 10 min 10 sekúnd - [16 hodín 10 minút 10 sekúnd]`

**
In case you need time to be pronounced as analog or Slovak SI units to be pronounced correctly, it is necessary to transcribe your input**

> > - 15:15 → štvrť na štyri
> > - 12:00 → poludnie
> > - 12:30 → pôl jednej
> > - 10 s → 10 sekúnd
> > - po 8:00 → po osmej hodine

 English language

Standard ISO format is supported and pronounced correctly by default:

> > - 15:15 → quarter past three
> > - 12:00 → at noon
> > - 12:30 → half past twelve
> > - 10 s → 10 seconds
> > - around 8 - around 8-ish

**In case you need time to be pronounced as analog or time notation to be pronounced correctly, it is necessary to transcribe your input:**

> > `A. 10 o'clock
> > [10 o'clock]`

> > `B. 10:00 AM
> > 10 a.m.
> > 10 AM
> > [10 A. M.]`

Also, other formats of time are supported:

> > `A. HH:mm:ss
> > 10:50:10
> > [10 hours 5 minutes and 20 seconds]`

> > `B. HH:mm
> > 15:00
> > UK,US: [three P.M.]
> > 10:00
> > UK, US: [ten o'clock]
> > 10:45
> > UK, US: [ten forty five]`

 Standard ISO format is supported and pronounced correctly by default.



---

# Customizing speech synthesis of variables

A variable is a named storage location that holds a value in computer programming. It is a fundamental concept used to store and manipulate data within a program. In the context of voicebots and speech applications, variables can be used to store and retrieve information that is relevant to the conversation or user interaction.

### General use

To use variables in the speech output of a voicebot, you need to incorporate the variable values within the text that the voicebot will read out loud (in the Message node, fill in the Speech window). 

General approach:

1. Define and store the variable values: In your voicebot's code or script, define and store the necessary variable values based on user input or other relevant data. For example, you might have a variable named customer_name that stores the user's name.
2. Construct the speech output text: Craft the message, and include the variable values where appropriate.
3. Set Speech in Message node: Paste the constructed speech input for the text-to-speech engine to convert it into audible speech. Your digital assistant will then speak the generated text, incorporating the variable values dynamically.

![]()

## Common problems and FAQ

****

****

****
