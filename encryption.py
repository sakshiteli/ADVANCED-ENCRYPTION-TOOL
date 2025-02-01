from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Function to generate a random key for AES-256
def generate_key():
    return os.urandom(32)  # AES-256 requires a 32-byte key

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)  # AES block size is 16 bytes
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Padding to make data block size a multiple of 16 bytes
    pad_length = 16 - len(data) % 16
    data += bytes([pad_length]) * pad_length
    
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    
    # Save the encrypted file with IV prepended
    with open(f"{file_path}.enc", 'wb') as enc_file:
        enc_file.write(iv + encrypted_data)
    
    print(f"File encrypted successfully: {file_path}.enc")

# Function to decrypt a file
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as enc_file:
        enc_data = enc_file.read()
    
    # Extract the IV from the encrypted file (first 16 bytes)
    iv = enc_data[:16]
    encrypted_data = enc_data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Remove padding
    pad_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-pad_length]
    
    # Save the decrypted file
    with open(f"{file_path[:-4]}.dec", 'wb') as dec_file:
        dec_file.write(decrypted_data)
    
    print(f"File decrypted successfully: {file_path[:-4]}.dec")
