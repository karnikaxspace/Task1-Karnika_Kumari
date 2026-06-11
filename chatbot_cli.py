"""
Rule-Based AI Chatbot – CLI Version
Infinite loop with exit commands.
"""

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! Type 'help' to see what I can do.",
    "hey": "Hey! What's up?",
    "how are you": "I'm just a bunch of rules, but I'm functioning perfectly!",
    "how are you?": "I'm just a bunch of rules, but I'm functioning perfectly!",
    "what is your name": "I'm RuleBot, your deterministic AI assistant.",
    "what's your name": "I'm RuleBot, your deterministic AI assistant.",
    "name": "I'm called RuleBot.",
    "help": "I understand: hello, hi, hey, how are you, what is your name, help, bye, exit, quit.",
    "commands": "Try: hello, how are you, name, bye.",
    "bye": "Goodbye! Have a great day.",
    "exit": "Goodbye! Have a great day.",
    "quit": "Goodbye! Have a great day.",
    "thanks": "You're welcome!",
    "thank you": "My pleasure.",
}

fallback = "I don't understand that yet. Type 'help' to see what I know."

def get_response(user_input):
    clean = user_input.lower().strip()
    return responses.get(clean, fallback)

def main():
    print("🤖 RuleBot CLI – Deterministic Chatbot")
    print("Type 'bye', 'exit', or 'quit' to stop.\n")
    
    while True:
        user_msg = input("You: ").strip()
        if user_msg.lower() in ["bye", "exit", "quit"]:
            print("RuleBot: Goodbye! Have a great day.")
            break
        reply = get_response(user_msg)
        print(f"RuleBot: {reply}")

if __name__ == "__main__":
    main()