import tkinter as tk
import math

def compute_sqrt():
    try:
        num = int(float_entry.get())
        text_box.delete("1.0", tk.END)  # Clear any previous content
        text_box.insert(tk.END, f"Square root of {num}: {math.sqrt(num):.2f}")
    except ValueError:
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, "Invalid Input")

# Set up the main window
root = tk.Tk()
root.title("Square Root")

# Create the header label
tk.Label(root, text="Square Root Calculator" ).pack(pady=10)

# Create a frame for the input
float_frame = tk.Frame(root)
float_frame.pack(pady=10)

# Input field for the number
tk.Label(float_frame, text="Enter a number:").grid(row=0, column=0, padx=5, pady=5)
float_entry = tk.Entry(float_frame, width=20)
float_entry.grid(row=0, column=1, padx=5, pady=5)

# Compute button
compute_button = tk.Button(root, text="Compute", command=compute_sqrt)
compute_button.pack(pady=10)

# Text box for output with a border to resemble a box
text_box = tk.Text(root, height=3, width=40, borderwidth=2, relief="sunken")
text_box.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
