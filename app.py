import tkinter as tk
from googletrans import Translator

def translate_text():
    # Get the text from the input field
    text = text_input.get("1.0", "end-1c")
    
    # Create a translator object
    translator = Translator(service_urls=['translate.google.com'])
    
    # Detect the source language
    detection = translator.detect(text)
    source_lang = detection.lang
    
    # Translate the text to the target language
    translation = translator.translate(text, dest=target_lang.get(), src=source_lang)
    
    # Update the output field with the translated text
    text_output.delete("1.0", "end")
    text_output.insert("1.0", translation.text)

# Create the main window
window = tk.Tk()
window.title("Language Translator")

# Create an input label and text area
label_input = tk.Label(window, text="Enter text:")
label_input.pack()
text_input = tk.Text(window, height=10, width=50)
text_input.pack()

# Create a target language selection dropdown
label_target = tk.Label(window, text="Target language:")
label_target.pack()
target_lang = tk.StringVar(window)
target_lang.set("en")  # Default to English
dropdown_target = tk.OptionMenu(window, target_lang, "english", "french", "english", "hindi","telugu")  # Add more languages as needed
dropdown_target.pack()

# Create a translate button
translate_button = tk.Button(window, text="Translate", command=translate_text)
translate_button.pack()

# Create an output label and text area
label_output = tk.Label(window, text="Translated text:")
label_output.pack()
text_output = tk.Text(window, height=10, width=50)
text_output.pack()

# Start the GUI event loop
window.mainloop()

