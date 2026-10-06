from openai import OpenAI

client = OpenAI()

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
            "content": "You are an assistant that always answers in the form of a poem."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

#captures the real life response with the input of the model and message (and by extention the user_input)
response_for_user = get_api_chat_response_message(model, messages)

#printing all of that in the command line
print("\n" + response_for_user + "\n")