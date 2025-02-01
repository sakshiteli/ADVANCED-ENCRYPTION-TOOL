import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import encrypt_file, decrypt_file

# Function to handle file encryption
def encrypt_action():
    key = key_entry.get().encode()
    if len(key) != 32:
        messagebox.showerror("Error", "Key must be 32 bytes (256 bits).")
        return
    
    file_path = filedialog.askopenfilename(title="Select a file to encrypt")
    if not file_path:
        return
    
    encrypt_file(file_path, key)

# Function to handle file decryption
def decrypt_action():
    key = key_entry.get().encode()
    if len(key) != 32:
        messagebox.showerror("Error", "Key must be 32 bytes (256 bits).")
        return
    
    file_path = filedialog.askopenfilename(title="Select a file to decrypt")
    if not file_path:
        return
    
    decrypt_file(file_path, key)

# Create the main window
root = tk.Tk()
root.title("Advanced Encryption Tool")

# Create and place the widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

key_label = tk.Label(frame, text="Enter Key (32 bytes for AES-256):")
key_label.grid(row=0, column=0, padx=5, pady=5)

key_entry = tk.Entry(frame, width=50, show="*")
key_entry.grid(row=0, column=1, padx=5, pady=5)

encrypt_button = tk.Button(frame, text="Encrypt File", command=encrypt_action)
encrypt_button.grid(row=1, column=0, padx=5, pady=5)

decrypt_button = tk.Button(frame, text="Decrypt File", command=decrypt_action)
decrypt_button.grid(row=1, column=1, padx=5, pady=5)

# Run the GUI application
root.mainloop()
