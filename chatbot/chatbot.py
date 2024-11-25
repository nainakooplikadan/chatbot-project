import tkinter as tk

from tkinter import scrolledtext
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.chat.util import Chat, reflections

# Ensure necessary nltk data files are downloaded
import nltk
nltk.download('punkt_tab') 

# Define pairs for chatbot interaction
pairs = [
    (r'Hi|Hello|Hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'How are you?', ['I am good, thank you!', 'I am doing well!']),
    (r'(.*) your name?', ['I am a chatbot created by Naina!']),
    (r'quit', ['Goodbye!'])
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Initialize the stemmer
stemmer = PorterStemmer()

# Define function to preprocess input (tokenization + stemming)
def preprocess_input(user_input):
    # Tokenize input
    tokens = word_tokenize(user_input)
    # Stem tokens
    return [stemmer.stem(word) for word in tokens]

# Create a GUI window
window = tk.Tk()
window.title("Chatbot")

# Create a ScrolledText widget to display the conversation
chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_area.grid(row=0, column=0, padx=10, pady=10)

# Function to handle user input and chatbot response
def get_response():
    user_input = user_entry.get()
    
    if user_input.lower() == 'quit':  # Check if the user types 'quit'
        chat_area.insert(tk.END, "Chatbot: Goodbye!\n")
        window.quit()  # Close the window and end the conversation
    
    # Preprocess input and get response
    preprocessed_input = preprocess_input(user_input)
    response = chatbot.respond(" ".join(preprocessed_input)) if preprocessed_input else "Sorry, I didn't understand that."
    
    # Display user input and bot response
    chat_area.insert(tk.END, f"You: {user_input}\n")
    chat_area.insert(tk.END, f"Chatbot: {response}\n")
    chat_area.yview(tk.END)  # Scroll to the bottom
    user_entry.delete(0, tk.END)  # Clear the input field

# Create a text entry box to type user input
user_entry = tk.Entry(window, width=40, font=("Arial", 12))
user_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a button to send the message
send_button = tk.Button(window, text="Send", command=get_response, font=("Arial", 12))
send_button.grid(row=2, column=0, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
import nltk
print(nltk.data.path)

