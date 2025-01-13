

from textblob import TextBlob

def rule_based_response(user_input):
    user_input = user_input.lower()

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day!"
    elif "help" in user_input:
        return "I can answer your basic questions. Just ask!"
    else:
        return None

def ai_response(user_input):
    # Using sentiment analysis for dynamic responses
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "That's great to hear!"
    elif polarity < 0:
        return "I'm sorry to hear that. How can I help?"
    else:
        return "Tell me more about that."

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break

        response = rule_based_response(user_input)
        if response:
            print("Chatbot:", response)
        else:
            print("Chatbot:", ai_response(user_input))

if __name__ == "__main__":
    chatbot()
