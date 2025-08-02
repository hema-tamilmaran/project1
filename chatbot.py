def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type something to talk (type 'bye' to exit).")

    while True:
        user_input = input("You: ").lower()

        # Greetings
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! How can I help you?")
        
        # Common phrases
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm doing well, thank you! What about you?")
        elif user_input in ["i am fine", "i'm fine", "i am good"]:
            print("Chatbot: Great to hear that!")

        # Time-based greetings
        elif user_input == "good morning":
            print("Chatbot: Good morning! Hope you have a great day!")
        elif user_input == "good night":
            print("Chatbot: Good night! Sleep well!")
        elif user_input == "good afternoon":
            print("Chatbot: Good afternoon! How’s your day going?")

        # Asking for chatbot's name
        elif user_input in ["what is your name", "who are you"]:
            print("Chatbot: I'm a simple rule-based chatbot created with Python!")

        # Thank you response
        elif user_input in ["thank you", "thanks"]:
            print("Chatbot: You're welcome!")

        # Farewell
        elif user_input in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        # Fallback response
        else:
            print("Chatbot: Sorry, I didn't understand that. Try saying 'hello', 'how are you', or 'bye'.")

# Run the chatbot
chatbot()

