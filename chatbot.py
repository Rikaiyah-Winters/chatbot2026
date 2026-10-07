from openai import OpenAI

client = OpenAI()

#determined whether or not the input is a question by the 7 question keywords w/ each word in the input
def set_user_input_category(user_input):
    question_keywords = ["who", "what", "where", "why", "when", "how", "?"]
    for keyword in question_keywords:
        #if keyword is in the user_input, then return question
        if keyword in user_input.lower():
            return "question"
        #if none of the keywords match the user_input words, then return "statement"
    return "statement"

#small function to capture the api response message
def get_api_chat_response_message(model, messages):

    #captures total api response in a variable
    response = client.chat.completions.create(
            model = model,
            messages = messages
        )

    #whittles total response to just the message text
    response_content = response.choices[0].message.content

    #returns the message text
    return response_content

#prompts user to ask something
user_input = input("\nAsk something...\n\n")

#states model
model = "gpt-6-luna"

#outlines message roles and content and passes in the user input
messages = [
        {
            "role": "system",
            "content": "You are an assistant that is very articulate and enjoys a witty turn of phrase."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

#captures the real life response with the input of the model and message (and by extention the user_input)
response_for_user = get_api_chat_response_message(model, messages)

#if user_input is a question, then concatinate "Good question" on there
if set_user_input_category(user_input) == "question":
    response_for_user = "Good question! " + response_for_user

#printing all of that in the command line
print("\n" + response_for_user + "\n")