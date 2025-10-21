# chatbot.py
# CODSOFT Internship - Task 1: Rule-Based Chatbot
# Author: Sai Charan Koganti

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greeting responses
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! 👋 I'm your CodSoft AI Assistant. How can I help you today?"
    
    # Asking about bot
    elif "who are you" in user_input:
        return "I'm a simple chatbot built by Sai Charan for the CodSoft AI Internship 😎"
    
    # Asking about weather
    elif "weather" in user_input:
        return "I can’t check the weather right now, but you can try searching 'weather in Hyderabad' on Google ☀️"
    
    # Asking about time
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')} ⏰"
    
    # Saying goodbye
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day ahead 😊"
    
    # Default fallback
    else:
        return "I'm not sure I understand. Could you please rephrase that?"

# --- Chat loop ---
print("🤖 CodSoft Chatbot Online!")
print("Type 'bye' or 'exit' to end the chat.\n")

while True:
    user_text = input("You: ")
    response = chatbot_response(user_text)
    print("Bot:", response)
    
    if "bye" in user_text.lower() or "exit" in user_text.lower():
        break
