from tkinter import *
from googletrans import Translator

def translate_word():
    word = entry.get()
    translator = Translator()
    translation = translator.translate(word, dest='vi').text
    result_label.config(text=translation)

root = Tk()
root.title("Từ điển mini")
entry = Entry(root, width=40)
entry.pack(pady=10)
Button(root, text="Dịch sang Tiếng Việt", command=translate_word).pack()
result_label = Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)
root.mainloop() 

