import tkinter as tk

class EasyFrame(tk.Tk):
    def __init__(self, title="Simple Frame", width=300, height=150):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")

    # Corrected addLabel with columnspan support
    def addLabel(self, text, row, column, columnspan=1):
        label = tk.Label(self, text=text)
        label.grid(row=row, column=column, columnspan=columnspan)
        return label

    # Add an integer field (simple Entry widget)
    def addIntegerField(self, default, row, column):
        entry = tk.Entry(self)
        entry.insert(0, str(default))
        entry.grid(row=row, column=column)
        return entry
    
    # Add a button
    def addButton(self, text, command, row, column, columnspan=1):
        button = tk.Button(self, text=text, command=command)
        button.grid(row=row, column=column, columnspan=columnspan)
        return button
