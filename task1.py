import tkinter as tk
import time
import random

class SimpleChatbot:
    def __init__(self, window):
        # Set up window title and size
        window.title("Friendly Chatbot")
        window.geometry("500x500")

        # Text area to show chat messages
        self.chat_area = tk.Text(window, wrap=tk.WORD, state='disabled')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Frame for input and button
        input_frame = tk.Frame(window)
        input_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

        # Input box for user text
        self.user_input = tk.Entry(input_frame)
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.user_input.bind("<Return>", self.handle_input)

        # Send button
        tk.Button(input_frame, text="Send", command=self.handle_input).pack(side=tk.RIGHT)

        # Store reference to main window for later
        self.window = window

        # Welcome message from the bot
        self.display_message("Bot", "Hi there! You can ask me about time, date, or type 'help' for ideas.")

    def display_message(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def generate_reply(self, message):
        msg = message.lower().strip()

        # Matching user message to bot replies
        if not msg:
            return "Please type something so we can chat!"
        elif "hello" in msg or "hi" in msg:
            return random.choice(["Hello!", "Hi there!", "Hey!"])
        elif "how are you" in msg:
            return "I'm doing great! How about you?"
        elif "fine" in msg or "good" in msg:
            return "Awesome! 😊 Let me know if you need anything."
        elif "your name" in msg or "who are you" in msg:
            return "I'm a simple chatbot built with Python!"
        elif "time" in msg:
            return "Current time is: " + time.strftime('%H:%M:%S')
        elif "date" in msg:
            return "Today's date is: " + time.strftime('%Y-%m-%d')
        elif "weather" in msg:
            return "I can't check weather now, but you can ask me other stuff!"
        elif "help" in msg:
            return "You can try saying: hi, time, date, joke, bye"
        elif "thank" in msg:
            return "You're welcome! 😊"
        elif "joke" in msg:
            return random.choice([
                "Why did the computer get cold? Because it left its Windows open!",
                "Why don't scientists trust atoms? Because they make up everything!"
            ])
        elif "bye" in msg or "exit" in msg:
            return "Goodbye! See you next time 😊"

        return "Hmm... I didn't get that. Try typing 'help' to see what I can do!"

    def handle_input(self, event=None):
        user_text = self.user_input.get()
        if not user_text:
            return

        self.display_message("You", user_text)
        self.user_input.delete(0, tk.END)

        bot_reply = self.generate_reply(user_text)
        self.display_message("Bot", bot_reply)

        # Close the app after saying goodbye
        if "bye" in user_text.lower() or "exit" in user_text.lower():
            self.window.after(2000, self.window.destroy)

# Start the chatbot app
if __name__ == "__main__":
    root = tk.Tk()
    chatbot = SimpleChatbot(root)
    root.mainloop()
