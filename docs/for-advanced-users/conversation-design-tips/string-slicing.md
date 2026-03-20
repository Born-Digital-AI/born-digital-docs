# String slicing

Let's delve into the concept of string slicing and how it can be applied to extract meaningful pieces of information to be used in conversational design.

# Example use case

Consider an order ID composed of 12 digits, structured as follows:

- The first 4 digits represent the year of creation.
- The last digit denotes the type of buyer, where '4' indicates a purchase by an individual and '5' denotes a purchase by a company.
- The fifth and sixth digits represent the product category, with specific numerical codes assigned to different product types. For instance, '10' might represent a refrigerator, '25' a washing machine, '06' a computer, and so forth.

![]()

Let's take the following order ID as an example. From user's utterance we have extracted an order id and saved it as a string to a variable named order_id.

![]()

Now, let's break down this order ID into its constituent parts using string slicing:

**General rules:**

1. **Slicing from the start:**

- When slicing from the start of the string, you specify the starting index as 0.
- `Example: string_variable[start:]`
- This will slice the string starting from the specified index start until the end of the string.
2. **Slicing from the end:**

- When slicing from the end of the string, you can use negative indices to specify positions relative to the end of the string.
- `Example: string_variable[-end:]`
- This will slice the string starting from end positions from the end of the string until the end of the string.
3. **Slicing in an interval:**

- You can also specify an interval (step) between characters to be included in the slice.
- `Example: string_variable[start:end:interval]`
- The interval specifies how many characters to skip after each character is included in the slice.
- Omitting start and end (or both) will default to the start and end of the string, respectively.
- Omitting interval will default to 1, meaning consecutive characters will be included.
- If interval is negative, the slice will be performed in reverse order.


Let's break it down for order_id = "202406987614" and save each substring to a separate variable:

**Extracting the year**

- The first 4 digits in order_id represent the year, so we have to slice the string after 4 characters from the start of the string.
- 202406987614
- Store value "2024" in a variable named order_year.

```
order_id[:4]
```

![]()

**Identifying the product category**

- The product category is coded as the fifth and sixth digits in the string, so we have to slice out all characters between the fifth (included) and the seventh (excluded).
- 202406987614
- Store value "06" in a variable product_category.

```
order_id[5:7]
```

![]()

**Determining the buyer type**

- The last digit in a string represents buyer type, so we have to slice 1 character from the end of a string.
- **202406987614**
- `Store value "4" in a variable named buyer_type.`

```
order_id[-1]
```

![]()



---

# Other use cases and ideas

Here are additional use cases for utilizing string slicing in chatbots and voicebots:

1. **Extracting Date and Time from ISO Format:**

- You can use string slicing to extract different parts of the date and time from the YYYY-MM-DD-T-HH:mm.SS format.
- For example, if you need only the date, you can use string_variable[:10] to slice the first 10 characters.
- To extract the time, you can use string_variable[11:19] to slice the time segment.
2. **Extracting Area Code from Phone Numbers:**

- If you have phone numbers in a format with an area code, you can use string slicing to extract this area code.
- For instance, if the area code always consists of a certain number of digits (e.g., 3), you can use string_variable[:3] to slice the first three digits.
3. **Extracting Last 4 Digits from Social Security Numbers:**

- If you need to extract a specific part from a social security number, such as the last 4 digits, you can use string slicing.
- By using a negative index, you can easily obtain the last part of the string, for example, string_variable[-4:] to extract the last 4 characters.
4. **Extracting Information from Personal Identification Numbers (PINs) or Social Security Numbers (SSNs):**

- Personal identification numbers, such as social security numbers, often encode information like date of birth and gender. String slicing can be used to extract this information.
- For example, in some systems, the first few digits of a social security number might encode the individual's birthdate and gender.
- By defining specific slicing patterns, you can extract the relevant portions of the SSN to obtain the date of birth and gender information.
- For instance, you might use string_variable[:6] to extract the first six digits representing the birthdate, and then further processing can decode these digits to derive the actual date of birth and gender.
