import tkinter as tk 
import math 

def  compute():
    try:
        num=int(float_entry.get())
        text_box.delete("1.0",tk.END)#clear any previous content in the output  box
        text_box.insert(tk.END,f"Square root of{num}={math.sqrt(num):.2f}")
    except ValueError:
        text_box.delete("1.0",tk.END)
        text_box.insert(tk.END,"Invalid  input")

root=tk.Tk()
root.title("Square root")

tk.Label(root,text="Sq root cal").pack(paddy=10)

frame_entry=tk.Frame(root)
