# 🤖 Project 1: Rule‑Based AI Chatbot

**Author:** Karnika Kumari  
**Batch:** 2026 | DecodeLabs Industrial Training Kit  
**Role:** Artificial Intelligence Engineer

---

## 📌 Overview

A deterministic, rule‑based chatbot that responds to predefined user inputs using dictionary mapping and fallback logic. This project demonstrates **white‑box AI** – every response is hard‑coded, traceable, and free from hallucinations.

---

## 🎯 Learning Objectives

- Implement control flow using **if‑else** and **hash maps**
- Understand the **IPO model** (Input → Process → Output)
- Build an **infinite loop** with a clean exit strategy
- Distinguish **deterministic** (rule‑based) from **probabilistic** AI
- Create a professional **Streamlit UI** and a **CLI version**

---

## 🧠 How It Works

| Phase | Description |
|-------|-------------|
| **Input** | User types a message |
| **Sanitization** | Lowercase, strip whitespace |
| **Processing** | Lookup in dictionary (O(1) hash map) |
| **Fallback** | Default response for unknown inputs |
| **Output** | Bot reply in chat |

---

-rule_based_chatbot/
     - app.py
    - chatbot_cli.py
    - requirements.txt
    - README.md

---

## 🚀 Setup & Execution

### Prerequisites
- Python 3.7+

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Web UI (recommended)
```bash
streamlit run app.py
```
### 4. Run the CLI version (optional)
```bash
python chatbot_cli.py
```
### 💬 Built‑in Intents

| User says (examples)                | Bot responds                                                |
|-------------------------------------|-------------------------------------------------------------|
| hello, hi, hey                      | Hello! How can I help you today?                           |
| how are you                         | I'm just a bunch of rules, but I'm functioning perfectly!  |
| what is your name, name             | I'm RuleBot, your deterministic AI assistant.              |
| help, commands                      | Lists all understood commands                              |
| bye, exit, quit                     | Goodbye! Have a great day.                                 |
| thanks, thank you                   | You're welcome! / My pleasure.                             |
| (anything else)                     | I don't understand that yet. Type 'help'.                  |

### 📊 Why This Matters
Even large language models (GPT‑4, Claude) use rule‑based guardrails on top of their probabilistic cores – to block harmful outputs, enforce policies, and ensure safety. Project 1 builds that foundational skill.

---

### ✅ Completion Badge
Earned: Rule‑Based Logic | Deterministic Control Flow | White‑Box AI
