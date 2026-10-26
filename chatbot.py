from openai import OpenAI

client = OpenAI()


def get_api_chat_response_message(model, messages):

    
    response = client.chat.completions.create(
            model = model,
            messages = messages
        )

    
    response_content = response.choices[0].message.content

    
    return response_content


#user_input = input("\nAsk something...\n\n")


model = "gpt-6-luna"
########################################

plot_description = """In the heart of the bustling metropolis of Astoria, the old Henderson House stands as a
silent sentinel, its imposing facade a stark contrast to the modern skyscrapers that
surround it. Once a grand mansion, it now sits abandoned, its windows broken, its
once-luxurious gardens now a tangle of weeds and ivy. The house is said to be haunted, its
halls echoing with the whispers of a tragic past.
When seventeen-year-old Mia Alvarez moves to Astoria with her family, she is immediately
drawn to the mystery of the old house. Despite the warnings of her new friends, Mia
becomes determined to uncover the truth behind the rumors that surround it.
As Mia delves deeper into the history of the Henderson House, she discovers a dark and
twisted tale. The house was once the home of the wealthy and influential Henderson
family, until one fateful night when a series of mysterious disappearances rocked the city.
The family was never seen again, and the house was left abandoned, a grim reminder of
the tragedy that had befallen it.
Determined to unravel the mystery, Mia enlists the help of her friends, including the
charming and enigmatic Alex. Together, they embark on a dangerous journey into the heart
of the city's dark underbelly, where they must confront not only the malevolent spirits that
haunt the Henderson House but also the sinister forces that seek to keep its secrets buried.
As they dig deeper, Mia and her friends uncover a web of lies and deceit that stretches
back decades, and they realize that the key to solving the mystery may lie closer to home
than they ever imagined. But with each step closer to the truth, they also draw closer to
danger, and Mia must confront her own fears if she is to uncover the secrets of the
Henderson House and escape its haunting legacy.
"""

plot_prompt = f"""
Summarize the text below, in between < and >, in no more than 100 words.

<{plot_description}>

Write this as one paragraph.
"""

#regular messages, below is the book review messages.
book_summary_messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": plot_prompt
        }
    ]

#book summary api call
book_summary = get_api_chat_response_message(model, book_summary_messages)

########################################
book_reviews = {
    """I read The Forgotten House and found it to be average. The writing was decent, and the
plot was somewhat engaging, but it didn't leave a lasting impression on me.""",
"""I found The Forgotten House to be predictable and lacking in originality. The plot felt
formulaic, and the characters were one-dimensional. Overall, a disappointing read.""",
"""A thrilling tale that kept me on the edge of my seat! The author expertly weaves together
mystery, suspense, and a touch of the supernatural. A must-read for fans of young adult
fiction!""",
"""The writing style of this book didn't resonate with me. I found it to be overly descriptive,
which slowed down the pacing of the story. The characters also felt clichéd and
uninteresting.""",
"""I struggled to connect with the characters in this book. They felt flat and underdeveloped,
which made it difficult to care about their fates. The plot, while intriguing, was ultimately let
down by the lack of depth in the characters.""",
"""I couldn't put this book down! The characters are relatable, the plot is engaging, and the
setting is beautifully described. A captivating read from start to finish!""",
"""The Forgotten House was an okay read. The story was interesting enough to keep me
turning the pages, but I didn't feel particularly invested in the characters or the outcome.""",
"""The Forgotten House is a hauntingly beautiful story that lingers long after the final page.
The author's descriptive prose brings the city to life, while the mystery keeps you guessing
until the end. Highly recommend!""",
"""An atmospheric masterpiece! The author's vivid descriptions make you feel like you're
right there in the city, exploring its secrets alongside the characters. A captivating and
immersive read!""",
"""While the premise of The Forgotten House was intriguing, I felt that the execution fell
short. The story lacked depth and complexity, and the ending left me feeling unsatisfied.
Overall, not a book I would recommend.""",
"""The Forgotten House was an alright book. The premise was intriguing, but the execution
fell a bit flat for me. I think it could have been more engaging with stronger character
development.""",
"""A gripping mystery with a supernatural twist! The characters are well-developed, the plot is
fast-paced, and the setting is richly detailed. A definite must-read for fans of the genre!""",
"""The Forgotten House started off strong, but I found the middle portion of the book to be
slow and repetitive. The resolution felt rushed and unsatisfying, leaving me wanting more.""",
"""I finished The Forgotten House and felt indifferent about it. The story was fine, but it didn't
leave a lasting impression on me. It's a decent read if you're looking for something light."""
}

book_reviews_with_sentiments = []

for review in book_reviews:
    review_prompt = f"""Please determine the sentiment of {review} as a single word, 'positive' or 'negative'."""
    #this should just return the words positive or negative
    #sets up review_prompt and reviews to be sent to the api call
    review_messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": review_prompt
            }
        ]

    #sends out api call. same function as before just sending it the review_messages info and saving it to a differnet variable
    sentiment = get_api_chat_response_message(model, review_messages)

    #still within the loop, we're appending each review and sentiment as/after they've been evaulated by the api
    book_reviews_with_sentiments.append({
        "review": review,
        "sentiment": sentiment,
    })

########################################

positive_book_reviews = []

#brws is an array
#each review is a dictionary
#traversing it means: 
for review in book_reviews_with_sentiments:    
    if review["sentiment"] == "positive":
        positive_book_reviews.append(review["review"])

email_prompt = f"""Please write a book release announcement email using the book summary below, in between < and >.
<{book_summary}>.

Please also include a couple of reviews from: {positive_book_reviews}"""

email_announcement_messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant that is good at writing promotional emails."
    },
    {
        "role": "user",
        "content": email_prompt 
    }
]

promotional_email = get_api_chat_response_message(model, email_announcement_messages)



#printing both of them
#print("\n" + book_summary + "\n")
#print(book_reviews_with_sentiments)
print(promotional_email)