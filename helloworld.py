import tkinter as tk
from PIL import Image, ImageTk

# Define a function to add the two numbers entered by the user
def add_numbers():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Addition Calculator")
root.geometry("900x900")
image = Image.open("amongus.png")
photo = ImageTk.PhotoImage(image)

# Create a label to display the background image
bg_label = tk.Label(root, image=photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create the entry fields for the two numbers
entry1 = tk.Entry(root)
entry1.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

# Create a button to perform the addition
add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()