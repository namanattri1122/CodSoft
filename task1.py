# Simple Rule-Based Chatbot
# Created using basic logic and conditions

def convert_to_lower(text):
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result


print("Chatbot: Hello! I am a simple chatbot.")
print("Chatbot: Type 'bye' to end the chat.")

while True:
    user_input = input("\nYou: ")

    # Convert input to lowercase for easy comparison
    user_input = convert_to_lower(user_input)

    if user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day 😊")
        break

    elif user_input == "hello" or user_input == "hi":
        print("Chatbot: Hi there! How can I help you?")

    elif user_input == "how are you":
        print("Chatbot: I am fine. Thanks for asking!")

    elif user_input == "what is your name":
        print("Chatbot: I do not have a name yet. You can name me if you want.")

    elif user_input == "help":
        print("Chatbot: You can say hello, ask how I am, or type bye to exit.")

    else:
        print("Chatbot: Sorry, I did not understand that.")
