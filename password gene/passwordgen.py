import random
import string
import tkinter as tk

def generate_password(length):
    # Define the characters to be used.
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the random password.
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Create the GUI.
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250") # Set the size of the window.
root.configure(bg="#f2f2f2") # Set the background color.

# Define the label and entry widgets.
length_label = tk.Label(root, text="Password Length:", bg="#f2f2f2", font=("Arial", 12))
length_entry = tk.Entry(root, font=("Arial", 12))
password_label = tk.Label(root, text="Generated Password:", bg="#f2f2f2", font=("Arial", 12))
password_entry = tk.Entry(root, font=("Arial", 14))

# Define the function to generate the password.
def generate():
    length = int(length_entry.get())
    password = generate_password(length)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Define the button widget.
generate_button = tk.Button(root, text="Generate Password", command=generate, font=("Arial", 12), bg="blue", fg="white")

# Pack the widgets into the window.
length_label.pack(pady=10)
length_entry.pack(pady=5)
password_label.pack(pady=10)
password_entry.pack(pady=5)
generate_button.pack(pady=20)

# Start the GUI event loop.
root.mainloop()