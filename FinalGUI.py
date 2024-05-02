import customtkinter as ctk
from tkinter import filedialog
from tkinter import *
import random
import string

##########################
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def build_markov_model(words):
    model = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in model:
            model[current_word].append(next_word)
        else:
            model[current_word] = [next_word]
    return model

def generate_text():
    text_corpus = textbox.get("1.0", "end")
    words = preprocess_text(text_corpus)
    model = build_markov_model(words)

    seed_word = textbox4.get()
    generated_texts = []
    for _ in range(10):
        generated_text = generate_text_from_model(model, seed_word)
        generated_texts.append(generated_text)
    textbox2.delete("1.0", "end")
    textbox2.insert("1.0", "\n\n".join(generated_texts))

def generate_text_from_model(model, seed_word):
    text = [seed_word]
    current_word = seed_word
    max_length=int(slider.get())
    for _ in range(max_length):
        if current_word in model:
            next_word_candidates = model[current_word]
            # Calculate probabilities for each candidate word
            probabilities = [model[current_word].count(w) / len(model[current_word]) for w in next_word_candidates]
            # Choose next word based on probabilities
            next_word = random.choices(next_word_candidates, weights=probabilities)[0]
            text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(text)
def showlimit(value):
    textbox3.delete("1.0", "end")  
    textbox3.insert("1.0", int(value))


#############################
def generate_text1(model, seed_word, max_length):
    text = [seed_word]
    current_word = seed_word
    for _ in range(max_length):
        if current_word in model:
            next_word_candidates = model[current_word]
            # Calculate probabilities for each candidate word
            probabilities = [model[current_word].count(w) / len(model[current_word]) for w in next_word_candidates]
            # Choose next word based on probabilities
            next_word = random.choices(next_word_candidates, weights=probabilities)[0]
            # next_word = random.choice(model[current_word])
            text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(text)
def open_file():
    filename=filedialog.askopenfilename(initialdir="C:\Desktop",title="Select")
    with open(filename, 'r') as file:
        text = file.read()
        input_textbox.delete("1.0", "end")  # Clear previous text
        input_textbox.insert("1.0", text)  # Insert file content into the input textbox

def generate():
    text = input_textbox.get("1.0", "end")
    words = preprocess_text(text)
    model = build_markov_model(words)
    seed_word = seed_word_entry.get()  # Get seed word from entry box
    max_length = int(max_limit_entry.get())  # Get max limit from entry box
    
    generated_texts = []  # List to store generated texts
    for _ in range(10):  # Generate 10 different texts
        generated_text = generate_text1(model, seed_word, max_length)
        generated_texts.append(generated_text)  # Append each generated text to the list
    
    output_textbox.delete("1.0", "end")  # Clear previous text
    output_textbox.insert("1.0", "\n\n".join(generated_texts))  # Insert all generated texts into the output textbox


###########  GUI  ##################
app = ctk.CTk()
app.title("Text Generator using Markov")
app.geometry("1200x700")

def change_theme():
    if switch.get() == 0:
        ctk.set_appearance_mode("light")
        switch.border_color="#ffffff"
    else:
        ctk.set_appearance_mode("dark")  # Light theme

tabview = ctk.CTkTabview(master=app,width=1180,height=680)
tabview.place(x=10,y=10)

tabview.add("Type Text")  # add tab at the end
tabview.add("Choose a file")  # add tab at the end
tabview.set("Type Text")  # set currently visible tab

##########  1st Tab  ################
label = ctk.CTkLabel(master=tabview.tab("Type Text"), text="Enter Word Limit", fg_color="transparent",font=("arial",20))
label.place(x=10,y=565)

switch = ctk.CTkSwitch(app, text="Dark Mode", font=("Arial", 12), command=change_theme)
switch.place(x=1050,y=10)

textbox = ctk.CTkTextbox(master=tabview.tab("Type Text"), border_width=2, width=570, height=550,wrap="word")
textbox.place(x=10, y=10)
textbox.insert("1.0", "Enter Corpus Text")

textbox2 = ctk.CTkTextbox(master=tabview.tab("Type Text"), border_width=2, width=570, height=550,wrap="word")
textbox2.place(x=585, y=10)


textbox3 = ctk.CTkTextbox(master=tabview.tab("Type Text"), border_width=2, width=50, height=30,wrap="word",activate_scrollbars=False)
textbox3.place(x=390, y=565)


textbox4 = ctk.CTkEntry(master=tabview.tab("Type Text"), placeholder_text="Enter Seed Word",border_width=2, width=200, height=30)
textbox4.place(x=460, y=565)

slider = ctk.CTkSlider(master=tabview.tab("Type Text"), from_=20, to=100,command=showlimit)
slider.place(x=170, y=572)

button = ctk.CTkButton(master=tabview.tab("Type Text"), text="Generate Text", command=generate_text, width=100, height=30)
button.place(x=10, y=600)

##########  2nd Tab  ############

label_seed = ctk.CTkLabel(master=tabview.tab("Choose a file"), text="Enter Seed Word:", fg_color="transparent", font=("arial", 14))
label_seed.place(x=10, y=568)

seed_word_entry = ctk.CTkEntry(master=tabview.tab("Choose a file"))
seed_word_entry.place(x=150, y=568)

label_limit = ctk.CTkLabel(master=tabview.tab("Choose a file"), text="Enter Max Limit:", fg_color="transparent", font=("arial", 14))
label_limit.place(x=10, y=600)

max_limit_entry = ctk.CTkEntry(master=tabview.tab("Choose a file"))
max_limit_entry.place(x=150, y=600)

open_file_button = ctk.CTkButton(master=tabview.tab("Choose a file"), text="Open File", command=open_file, width=100, height=30)
open_file_button.place(x=460, y=580)

generate_button = ctk.CTkButton(master=tabview.tab("Choose a file"), text="Generate Text", command=generate, width=100, height=30)
generate_button.place(x=620, y=580)

input_textbox = ctk.CTkTextbox(master=tabview.tab("Choose a file"), border_width=2, width=570, height=550)
input_textbox.place(x=10, y=10)

output_textbox = ctk.CTkTextbox(master=tabview.tab("Choose a file"), border_width=2, width=570, height=550)
output_textbox.place(x=585, y=10)

ctk.set_appearance_mode("light")
##########################################
app.mainloop()