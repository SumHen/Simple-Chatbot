import tkinter as tk
from tkinter import messagebox
import random

def get_bot_response(user_input):
    responses = {
        "hi": "Hello there! 👋",
        "hello": "Hey hey! 😄",
        "bye": "Goodbye! 👋",
        "how are you": "I'm just a code, but I'm doing great! 🤖✨",
        "": "You didn’t type anything 🙃",
        "what are you doing?": "answering you😊",
    }
    return responses.get(user_input.lower(), "I don't understand that 😅")

def update_text():
    user_text = entry.get()
    response = get_bot_response(user_text)
    label.config(text = "you said:  " + user_text + "\nBot says:  " + response)

def clear_text():
    entry.delete(0, tk.END)
    label.config(text = "say something")

def copy_to_clipboard():
    user_text = entry.get()
    window.clipboard_clear()
    window.clipboard_append(user_text)
    messagebox.showinfo("Copied!", "Copied to clipboard! 📋")

window = tk.Tk()
window.title("message app")
window.geometry("400x300")
window.config(bg="#f0f8ff")

label = tk.Label(
    window,
    text="say something",
    font=("Helvetica", 14),
    bg="#f0f8ff",
    fg="#333"
)
label.pack(pady = 10)

entry = tk.Entry(window, font=("Helvetica", 12), width= 30)
entry.pack(pady= 5)

button_frame = tk.Frame(window, bg="#f0f8ff")
button_frame.pack(pady=10)

submit_btn = tk.Button(button_frame, text="submit", command=update_text)
submit_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_text)
clear_btn.grid(row=0, column=1, padx=5)

copy_btn = tk.Button(button_frame, text="Copy", command=copy_to_clipboard)
copy_btn.grid(row=0, column=2, padx=5)

window.mainloop()
