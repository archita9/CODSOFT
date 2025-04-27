import re  # Regular expressions for pattern matching

print("Hello! I'm your rule-based chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if re.search(r'\b(bye|exit|quit)\b', user_input):
        print("Chatbot: Goodbye! Take care!")
        break

    # Greeting
    elif re.search(r'\b(hi|hello|hey)\b', user_input):
        print("Chatbot: Hey there! How can I help you?")

    # Asking how are you
    elif re.search(r'how are you', user_input):
        print("Chatbot: I'm doing great! Thanks for asking. How about you?")

    # Asking for name
    elif re.search(r'\b(name|who are you)\b', user_input):
        print("Chatbot: I'm a simple chatbot created to assist you!")

    # Asking for help
    elif re.search(r'\b(help|support)\b', user_input):
        print("Chatbot: Sure, I'm here to help you. Please tell me your problem.")

    # Asking about weather
    elif re.search(r'weather', user_input):
        print("Chatbot: I can't check real-time weather yet, but I hope it's sunny where you are!")

    # Random fallback response
    else:
        print("Chatbot: Sorry, I'm still learning. can you ask something else?")


