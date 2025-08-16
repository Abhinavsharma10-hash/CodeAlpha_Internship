# TASK 4: Basic Chatbot

def chatbot():
    print("Welcome to Simple Chatbot! (type 'exit' to end)")

    while True:
        user_input = input("You: ").lower()   # take input and convert to lowercase

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break   # exit the loop when user says bye
        elif user_input == "exit":
            print("Bot: Chat ended.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
