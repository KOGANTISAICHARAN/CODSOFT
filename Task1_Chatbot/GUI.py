# chatbot_gui.py
import tkinter as tk
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hey there! 👋 I'm your CodSoft AI Assistant. How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! How about you? 😊"

    elif "fine" in user_input or "good" in user_input:
        return "That's awesome to hear! 😄"

    elif "what's up" in user_input or "whatsup" in user_input:
        return "Just chatting with awesome people like you 😎 What’s up with you?"

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day ahead 😊"
    

    # =========================
    # 🔹 Information & Utility
    # =========================
    elif "who are you" in user_input:
        return "I'm a simple chatbot built by Sai Charan for the CodSoft AI Internship 😎"

    elif "who made you" in user_input or "your creator" in user_input:
        return "I was created by Sai Charan during the CodSoft AI Internship 💻"

    elif "codsoft" in user_input:
        return "CodSoft is a platform that offers internships and projects to help students gain real-world experience! 🚀"

    elif "help" in user_input or "what can you do" in user_input:
        return "I can answer basic questions, tell you the time, share info about CodSoft, or just chat with you! 😊"

    elif "weather" in user_input:
        return "I can’t check the weather right now, but you can try searching 'weather in Hyderabad' on Google ☀️"

    elif "time" in user_input:
        now = datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')} ⏰"

    elif "date" in user_input:
        today = datetime.now()
        return f"Today's date is {today.strftime('%B %d, %Y')} 📅"


    # =========================
    # 🔹 Fun & Entertainment
    # =========================
    elif "joke" in user_input:
        return "Why did the computer show up at work late? Because it had a hard drive! 🤣"

    elif "fun fact" in user_input:
        return "Did you know? The first computer bug was an actual moth found in a Harvard computer in 1947! 🐛💻"

    elif "quote" in user_input:
        return "“The best way to predict the future is to invent it.” — Alan Kay 🌟"


    # =========================
    # 🔹 Motivation & Support
    # =========================
    elif "motivate" in user_input or "motivation" in user_input:
        return "Keep pushing forward! Every expert was once a beginner. 💪✨"

    elif "thank" in user_input:
        return "You're most welcome! 😊 Happy to help."


    # =========================
    # 🔹 Tech & Coding
    # =========================
    elif "python" in user_input or "coding" in user_input:
        return "Python is one of my favorite languages! 🐍 It's great for AI, web apps, and automation."


    # =========================
    # 🔹 Compliments & Feedback
    # =========================
    elif "you are smart" in user_input or "you are good" in user_input:
        return "Aww, thank you! You’re pretty cool yourself 😄"


    # =========================
    # 🔹 Default & Unknown Input
    # =========================
    elif "?" in user_input:
        return "Hmm, I’ll try to understand that better soon. Could you tell me more? 🤔"
    
    else:
        return "I'm not sure I understand. Could you please rephrase that?"
    


def send_message():
    user_msg = entry_box.get()
    chat_window.insert(tk.END, f"You: {user_msg}\n")
    response = chatbot_response(user_msg)
    chat_window.insert(tk.END, f"Bot: {response}\n\n")
    entry_box.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("CodSoft Chatbot 🤖")

chat_window = tk.Text(root, bg="#1e1e1e", fg="#00ffcc", width=50, height=20)
chat_window.pack(padx=10, pady=10)

entry_box = tk.Entry(root, width=40, bg="#333333", fg="white")
entry_box.pack(side=tk.LEFT, padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message, bg="#00ffcc")
send_button.pack(side=tk.LEFT)

root.mainloop()

