import os
import importlib
import pyttsx3

# Initialize Text-to-Speech engine
tts_engine = pyttsx3.init()

# path to language files
LANGUAGES_DIR = "languages"


# Function to load languages
def load_languages():
    languages = {}
    for file in os.listdir(LANGUAGES_DIR):
        if file.endswith(".py") and file != "__init__.py":  # Ensure only Python files are processed
            lang_name = file.split(".")[0]  # Use file name as language name
            module = importlib.import_module(f"{LANGUAGES_DIR}.{lang_name}")
            if hasattr(module, 'dictionary'):
                languages[lang_name] = module.dictionary
            else:
                print(f"Warning: {lang_name} does not have a 'dictionary' attribute.")
    return languages


# Function to display and interact with the dictionary
def display_menu(languages):
    print("Available languages:")
    for i, lang in enumerate(languages.keys(), start=1):
        print(f"{i}. {lang.capitalize()}")

    choice = int(input("Choose a language by number: "))
    selected_lang = list(languages.keys())[choice - 1]

    print(f"\nYou selected: {selected_lang.capitalize()}")
    print("Available words:")
    for word, translation in languages[selected_lang].items():
        print(f"{word} -> {translation}")

    # Pronunciation option
    word_to_pronounce = input("\nEnter a word to pronounce (case-sensitive): ")
    if word_to_pronounce in languages[selected_lang]:
        speak(word_to_pronounce)
    else:
        print("Word not found in the dictionary.")


# Function for Text-to-Speech
def speak(word):
    print(f"Pronouncing '{word}'...")
    tts_engine.setProperty("rate", 150)  # Set speech speed
    tts_engine.say(word)
    tts_engine.runAndWait()


# Main program
if __name__ == "__main__":
    language = load_languages()
    display_menu(language)

