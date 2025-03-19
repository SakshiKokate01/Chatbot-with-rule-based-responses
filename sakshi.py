def simple_chatbot():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        elif "your name" in user_input:
            print("Chatbot: I am a simple chatbot.")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing well! Thanks for asking.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that.")


# Run the chatbot
simple_chatbot()
