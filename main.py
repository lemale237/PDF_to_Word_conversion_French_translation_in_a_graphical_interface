import PyPDF2
from docx import Document
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog, Text

# Créez la fenêtre principale et ses widgets
window = tk.Tk()
window.title("Convertisseur PDF en Word")

label = tk.Label(text="Sélectionnez un fichier PDF à convertir :")
label.pack(padx=10, pady=10)

file_label = tk.Label(text="Aucun fichier sélectionné")
file_label.pack(padx=10, pady=10)

def select_file():
    file = filedialog.askopenfilename()
    file_label.config(text=file)

select_button = tk.Button(text="Sélectionner un fichier", command=select_file)
select_button.pack(padx=10, pady=10)

def convert():
    # Ouvrez le fichier PDF et créez un objet "lecteur"
    with open(file_label['text'], 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)

    # Créez un nouveau document Word
    document = Document()

    # Créez un objet "traducteur"
    translator = Translator()

    # Pour chaque page du PDF, extraire le texte, le traduire et l'ajouter au document Word
    for page in range(reader.getNumPages()):
        text = reader.getPage(page).extractText()
        translation = translator.translate(text, dest='fr').text
        document.add_paragraph(translation)

    # Enregistrez le document Word
    document.save('mon_document.docx')

convert_button = tk.Button(text="Convertir en Word", command=convert)
convert_button.pack(padx=10, pady=10)

window.mainloop()
