import tkinter as tk
from tkinter import messagebox

class ModalDialog:
    def __init__(self, root, title, message):
        self.root = root
        self.title = title
        self.message = message
        self.backdrop = tk.Frame(self.root, bg="gray", width=400, height=200)
        self.backdrop.pack(fill="both", expand=True)
        self.dialog = tk.Frame(self.root, bg="white", width=400, height=200)
        self.dialog.pack(fill="both", expand=True)
        self.close_button = tk.Button(self.dialog, text="Close", command=self.close_dialog)
        self.close_button.pack(side="right")
        self.label = tk.Label(self.dialog, text=self.message, wraplength=350)
        self.label.pack(side="left", padx=10, pady=10)
        self.root.title(self.title)

    def close_dialog(self):
        self.backdrop.destroy()
        self.dialog.destroy()

def create_modal_dialog(root, title, message):
    modal_dialog = ModalDialog(root, title, message)
    root.mainloop()

root = tk.Tk()
create_modal_dialog(root, "Modal Dialog", "This is a modal dialog with a close button.")
