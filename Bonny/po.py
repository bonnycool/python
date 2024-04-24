import tkinter as tk
import math

def compute_sqrt():
    try:
        num = int(float_entry.get())
        result.set(f"Square root of {num}: {math.sqrt(num):.2f}")
    except ValueError:
        result.set("Invalid Input")

root = tk.Tk()
root.title("Square Root Calculator")

tk.Label(root, text="Square Root", font=("Helvetica", 16, "bold")).pack()

float_frame = tk.Frame(root)
float_frame.pack()

tk.Label(float_frame, text="Number:").grid(row=0, column=0)
float_entry = tk.Entry(float_frame)
float_entry.grid(row=0, column=1)

tk.Button(root, text="Compute", command=compute_sqrt).pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()