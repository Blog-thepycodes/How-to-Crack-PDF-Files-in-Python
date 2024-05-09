import tkinter as tk
from tkinter import filedialog, messagebox
import pikepdf
 
 
def browse_pdf():
   pdf_path = filedialog.askopenfilename(title="Choose PDF", filetypes=[("PDF Documents", "*.pdf")])
   if pdf_path:
       pdf_entry.delete(0, tk.END)
       pdf_entry.insert(0, pdf_path)
 
 
def browse_wordlist():
   wordlist_path = filedialog.askopenfilename(title="Password List", filetypes=[("Text Files", "*.txt")])
   if wordlist_path:
       wordlist_entry.delete(0, tk.END)
       wordlist_entry.insert(0, wordlist_path)
 
 
def unlock_pdf():
   pdf_path = pdf_entry.get()
   wordlist_path = wordlist_entry.get()
 
 
   if not pdf_path:
       messagebox.showwarning("Warning", "Please select a PDF file.")
       return
   if not wordlist_path:
       messagebox.showwarning("Warning", "Please select a wordlist file.")
       return
 
 
   with open(wordlist_path, 'r') as wordlist_file:
       passwords = [line.strip() for line in wordlist_file]
 
 
   for pwd in passwords:
       try:
           with pikepdf.open(pdf_path, password=pwd):
               messagebox.showinfo("Success", f"Correct Password: {pwd}")
               return
       except pikepdf._core.PasswordError:
           continue
 
 
   messagebox.showinfo("Attempt Over", "No matching password found.")
 
 
# Create main window
root = tk.Tk()
root.title("Unlock PDF Password - The Pycodes")
 
 
# PDF Entry Field
pdf_label = tk.Label(root, text="PDF File:")
pdf_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
 
 
pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=10, pady=5)
 
 
pdf_browse_btn = tk.Button(root, text="Browse", command=browse_pdf)
pdf_browse_btn.grid(row=0, column=2, padx=5, pady=5)
 
 
# Wordlist Entry Field
wordlist_label = tk.Label(root, text="Wordlist File:")
wordlist_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
 
 
wordlist_entry = tk.Entry(root, width=50)
wordlist_entry.grid(row=1, column=1, padx=10, pady=5)
 
 
wordlist_browse_btn = tk.Button(root, text="Browse", command=browse_wordlist)
wordlist_browse_btn.grid(row=1, column=2, padx=5, pady=5)
 
 
# Unlock PDF Button
unlock_pdf_btn = tk.Button(root, text="Unlock PDF", command=unlock_pdf)
unlock_pdf_btn.grid(row=2, column=1, pady=20)
 
 
root.mainloop()
