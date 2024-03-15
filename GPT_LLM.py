from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="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")

def chat_gpt(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use a different model, for example, davinci-codex
        messages=messages
    )
    return response.choices[0].message.content


conversation = []

while True:
    user_input = input("YOU: ")

    # Add user input to conversation history
    conversation.append({"role": "user", "content": user_input})

    if user_input.lower() == 'exit':
        break

    # Get response from GPT-3
    response = chat_gpt(conversation)

    # Print GPT-3 response and add it to conversation history
    print(f"BOT: {response}")
    conversation.append({"role": "assistant", "content": response})
