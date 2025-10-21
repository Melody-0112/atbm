import tkinter as tk
from tkinter import ttk, messagebox

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher - Mã hóa & Giải mã")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Cấu hình style
        self.setup_ui()
    
    def setup_ui(self):
        # Frame chính
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Tiêu đề
        title_label = ttk.Label(main_frame, text="CAESAR CIPHER", 
                               font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Nhập văn bản
        text_label = ttk.Label(main_frame, text="Nhập văn bản:", 
                              font=("Arial", 11))
        text_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        self.text_input = tk.Text(main_frame, height=6, width=50, 
                                 font=("Arial", 10), wrap=tk.WORD)
        self.text_input.grid(row=2, column=0, columnspan=2, pady=(0, 15))
        
        # Nhập khóa
        key_label = ttk.Label(main_frame, text="Nhập khóa (Key):", 
                             font=("Arial", 11))
        key_label.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        
        self.key_input = ttk.Entry(main_frame, font=("Arial", 11), width=20)
        self.key_input.grid(row=4, column=0, columnspan=2, pady=(0, 20))
        self.key_input.insert(0, "7")  # Giá trị mặc định
        
        # Các nút chức năng
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=2, pady=(0, 15))
        
        encrypt_btn = ttk.Button(button_frame, text="Mã hóa (Encrypt)", 
                                command=self.encrypt, width=20)
        encrypt_btn.grid(row=0, column=0, padx=5)
        
        decrypt_btn = ttk.Button(button_frame, text="Giải mã (Decrypt)", 
                                command=self.decrypt, width=20)
        decrypt_btn.grid(row=0, column=1, padx=5)
        
        clear_btn = ttk.Button(button_frame, text="Xóa", 
                              command=self.clear_all, width=12)
        clear_btn.grid(row=0, column=2, padx=5)
        
        # Kết quả
        result_label = ttk.Label(main_frame, text="Kết quả:", 
                                font=("Arial", 11, "bold"))
        result_label.grid(row=6, column=0, sticky=tk.W, pady=(0, 5))
        
        self.result_text = tk.Text(main_frame, height=6, width=50, 
                                  font=("Arial", 10), wrap=tk.WORD,
                                  bg="#f0f0f0", state=tk.DISABLED)
        self.result_text.grid(row=7, column=0, columnspan=2)
    
    def caesar_cipher(self, text, key, mode='encrypt'):
        """
        Thực hiện mã hóa hoặc giải mã Caesar Cipher
        mode: 'encrypt' hoặc 'decrypt'
        """
        result = ""
        
        # Nếu giải mã, đảo ngược khóa
        if mode == 'decrypt':
            key = -key
        
        for char in text:
            if char.isalpha():
                # Xác định ASCII offset (A=65 cho chữ hoa, a=97 cho chữ thường)
                ascii_offset = 65 if char.isupper() else 97
                
                # Mã hóa/giải mã ký tự
                shifted = (ord(char) - ascii_offset + key) % 26
                result += chr(shifted + ascii_offset)
            else:
                # Giữ nguyên ký tự không phải chữ cái
                result += char
        
        return result
    
    def encrypt(self):
        """Mã hóa văn bản"""
        try:
            # Lấy dữ liệu đầu vào
            plaintext = self.text_input.get("1.0", tk.END).strip()
            key = int(self.key_input.get())
            
            if not plaintext:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản!")
                return
            
            # Thực hiện mã hóa
            encrypted_text = self.caesar_cipher(plaintext, key, mode='encrypt')
            
            # Hiển thị kết quả
            self.display_result(encrypted_text)
            
        except ValueError:
            messagebox.showerror("Lỗi", "Khóa phải là một số nguyên!")
    
    def decrypt(self):
        """Giải mã văn bản"""
        try:
            # Lấy dữ liệu đầu vào
            ciphertext = self.text_input.get("1.0", tk.END).strip()
            key = int(self.key_input.get())
            
            if not ciphertext:
                messagebox.showwarning("Cảnh báo", "Vui lòng nhập văn bản!")
                return
            
            # Thực hiện giải mã
            decrypted_text = self.caesar_cipher(ciphertext, key, mode='decrypt')
            
            # Hiển thị kết quả
            self.display_result(decrypted_text)
            
        except ValueError:
            messagebox.showerror("Lỗi", "Khóa phải là một số nguyên!")
    
    def display_result(self, text):
        """Hiển thị kết quả lên Text widget"""
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert("1.0", text)
        self.result_text.config(state=tk.DISABLED)
    
    def clear_all(self):
        """Xóa tất cả dữ liệu"""
        self.text_input.delete("1.0", tk.END)
        self.key_input.delete(0, tk.END)
        self.key_input.insert(0, "7")
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state=tk.DISABLED)

# Chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()