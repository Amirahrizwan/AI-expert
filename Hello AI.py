# Simple Chatbot Program

print("Hello! I am ChatBot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi there! How can I help?")
    
    elif user == "how are you":
        print("Bot: I'm good! Thank you for asking 😊")
    
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break
    
    else:
        print("Bot: Sorry, I don't understand that.")
