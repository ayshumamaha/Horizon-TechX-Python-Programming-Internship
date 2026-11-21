# Basic Rule-Based Chatbot

def chatbot_response(user_input):

    message = user_input.lower().strip()

    if message in ["hello", "hi", "hey"]:
        return "Hi! Nice to meet you."

    elif message in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How are you?"

    elif message in ["what is your name", "what is your name?"]:
        return "I'm Python Chatbot."

    elif message in ["what can you do", "help"]:
        return "I can respond to simple messages and greetings."

    elif message in ["thank you", "thanks"]:
        return "You're welcome!"

    elif message in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that message."


print("=" * 40)
print("          BASIC CHATBOT")
print("=" * 40)

print("Chatbot: Hello! Welcome to the chatbot.")
print("Chatbot: Type 'bye' to end the conversation.")

while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
        break

print("\nChatbot session ended.")
