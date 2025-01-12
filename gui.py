import tkinter as tk
from tkinter import ttk
import pyttsx3

def run_gui(languages):
    engine = pyttsx3.init()

    def search_word():
        words = entry_word.get()
        selected_language = language_var.get()
        result_text.delete(1.0, tk.END)

        if word in languages[selected_language]:
            translation = languages[selected_language][word]
            result_text.insert(tk.END, f"{selected_language.capitalize()}: {translation}\n")
        else:
            result_text.insert(tk.END, "Word not found.\n")

    # Function to pronounce the word
    def pronounce_word():
        word = entry_word.get()
        engine.say(word)
        engine.runAndWait()

    # Create main window
    root = tk.Tk()
    root.title("Multi-Language Dictionary")

    # Language selection
    language_var = tk.StringVar(value="english")
    ttk.Label(root, text="Select Language:").grid(row=0, column=0, padx=10, pady=10)
    language_menu = ttk.Combobox(root, textvariable=language_var, values=list(languages.keys()))
    language_menu.grid(row=0, column=1, padx=10, pady=10)

    # Word entry
    ttk.Label(root, text="Enter Word:").grid(row=1, column=0, padx=10, pady=10)
    entry_word = ttk.Entry(root, width=20)
    entry_word.grid(row=1, column=1, padx=10, pady=10)

    # Buttons
    search_button = ttk.Button(root, text="Search", command=search_word)
    search_button.grid(row=2, column=0, padx=10, pady=10)

    pronounce_button = ttk.Button(root, text="Pronounce", command=pronounce_word)
    pronounce_button.grid(row=2, column=1, padx=10, pady=10)

    # Result display
    result_text = tk.Text(root, height=10, width=40)
    result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Run the app
    root.mainloop()