
"""
Rule-Based AI Chatbot – Project 1 (DecodeLabs)
Deterministic responses using dictionary mapping + fallback.
"""

import streamlit as st

# ---------- Page config ----------
st.set_page_config(page_title="RuleBot", page_icon="🤖", layout="centered")

st.title("🤖 RuleBot – Rule-Based AI Chatbot")
st.markdown("### *Deterministic. Predictable. Safe.*")
st.markdown("I respond to specific commands. No hallucinations, just pure logic.")

# ---------- Knowledge base (hash map) ----------
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

# ---------- Session state for chat history ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm RuleBot. Ask me something or type 'help'."}
    ]

# ---------- Display chat history ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------- Input & response ----------
user_input = st.chat_input("Type your message here...")

def get_response(user_msg):
    # Sanitize: lowercase, strip whitespace
    clean_msg = user_msg.lower().strip()
    # Direct lookup in dictionary (hash map)
    return responses.get(clean_msg, fallback)

if user_input:
    # Append user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get bot response
    bot_reply = get_response(user_input)
    
    # Append bot message to history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.write(bot_reply)
    
    # Auto-scroll (Streamlit handles it, but we need to rerun)
    st.rerun()

# ---------- Sidebar with info ----------
st.sidebar.header("ℹ️ About RuleBot")
st.sidebar.markdown("""
- **Type:** Deterministic Rule-Based
- **Lookup:** O(1) dictionary (hash map)
- **Fallback:** Generic response for unknown inputs
- **Exit commands:** `bye`, `exit`, `quit`
- **White box:** Every response is hard‑coded and explainable.
""")

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = [
        {"role": "assistant", "content": "Chat cleared. Hi again! Ask me something."}
    ]
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption("Project 1 – DecodeLabs Industrial Training Kit")