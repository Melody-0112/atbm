import random
import math
import os

def gcd(a, b):
    """Tính ước chung lớn nhất"""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(w, m):
    """Tính nghịch đảo modulo của w theo m sử dụng thuật toán Euclid mở rộng"""
    if gcd(w, m) != 1:
        return None
    
    m0, x0, x1 = m, 0, 1
    while w > 1:
        q = w // m
        m, w = w % m, m
        x0, x1 = x1 - q * x0, x0
    
    return x1 + m0 if x1 < 0 else x1

def generate_superincreasing_sequence(n):
    """Sinh vector siêu tăng a' với độ dài n"""
    sequence = []
    current_sum = 0
    
    for i in range(n):
        if i == 0:
            # Phần tử đầu tiên
            next_val = random.randint(2, 10)
        else:
            # Phần tử tiếp theo phải lớn hơn tổng tất cả phần tử trước
            next_val = random.randint(current_sum + 1, current_sum + 20)
        
        sequence.append(next_val)
        current_sum += next_val
    
    return sequence

def generate_keys(n):
    """
    Sinh khóa cho hệ mã hóa Trapdoor Knapsack
    n: độ dài vector khóa
    Trả về: (a_private, a_public, m, w, w_inverse)
    """
    # Sinh vector siêu tăng a'
    a_private = generate_superincreasing_sequence(n)
    
    # Sinh m > sum(a_private)
    sum_private = sum(a_private)
    m = random.randint(sum_private + 1, sum_private + 100)
    
    # Sinh w sao cho gcd(w, m) = 1
    w = random.randint(2, m - 1)
    while gcd(w, m) != 1:
        w = random.randint(2, m - 1)
    
    # Tính nghịch đảo của w theo modulo m
    w_inverse = mod_inverse(w, m)
    
    # Sinh khóa công khai a = w * a' mod m
    a_public = [(w * a_i) % m for a_i in a_private]
    
    return a_private, a_public, m, w, w_inverse

def save_private_key(a_private, m, w, filename="private_key.txt"):
    """Lưu khóa bí mật vào file"""
    with open(filename, 'w') as f:
        f.write(f"Vector siêu tăng a': {a_private}\n")
        f.write(f"m: {m}\n")
        f.write(f"w (omega): {w}\n")
    print(f"Khóa bí mật đã được lưu vào {filename}")

def save_public_key(a_public, filename="public_key.txt"):
    """Lưu khóa công khai vào file"""
    with open(filename, 'w') as f:
        f.write(f"Khóa công khai a: {a_public}\n")
    print(f"Khóa công khai đã được lưu vào {filename}")

def read_plaintext(filename):
    """Đọc bản rõ từ file (chuỗi bit)"""
    with open(filename, 'r') as f:
        plaintext = f.read().strip()
    return plaintext

def encrypt(plaintext_bits, a_public):
    """
    Mã hóa chuỗi bit bằng khóa công khai
    plaintext_bits: chuỗi bit (string)
    a_public: khóa công khai (list)
    """
    n = len(a_public)
    
    # Chia chuỗi bit thành các block có độ dài n
    blocks = []
    for i in range(0, len(plaintext_bits), n):
        block = plaintext_bits[i:i+n]
        # Padding nếu block cuối không đủ độ dài
        if len(block) < n:
            block += '0' * (n - len(block))
        blocks.append(block)
    
    # Mã hóa từng block
    ciphertext = []
    for block in blocks:
        c = sum(int(block[i]) * a_public[i] for i in range(n))
        ciphertext.append(c)
    
    return ciphertext

def save_ciphertext(ciphertext, filename="cipher.txt"):
    """Lưu bản mã vào file"""
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, ciphertext)))
    print(f"Bản mã đã được lưu vào {filename}")

def read_ciphertext(filename):
    """Đọc bản mã từ file"""
    with open(filename, 'r') as f:
        ciphertext = list(map(int, f.read().strip().split()))
    return ciphertext

def load_private_key(filename="private_key.txt"):
    """Đọc khóa bí mật từ file"""
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        # Parse vector a'
        a_private_str = lines[0].split(': ')[1].strip()
        a_private = eval(a_private_str)
        
        # Parse m
        m = int(lines[1].split(': ')[1].strip())
        
        # Parse w
        w = int(lines[2].split(': ')[1].strip())
        
    return a_private, m, w

def decrypt(ciphertext, a_private, m, w):
    """
    Giải mã bản mã bằng khóa bí mật
    ciphertext: danh sách các số nguyên
    a_private: vector siêu tăng
    m, w: tham số khóa bí mật
    """
    n = len(a_private)
    w_inverse = mod_inverse(w, m)
    
    plaintext_bits = ""
    
    for c in ciphertext:
        # Tính c' = c * w^(-1) mod m
        c_prime = (c * w_inverse) % m
        
        # Giải bài toán knapsack với vector siêu tăng
        block = ['0'] * n
        remaining = c_prime
        
        # Giải từ cuối về đầu (greedy)
        for i in range(n - 1, -1, -1):
            if remaining >= a_private[i]:
                block[i] = '1'
                remaining -= a_private[i]
        
        plaintext_bits += ''.join(block)
    
    return plaintext_bits

def save_plaintext(plaintext, filename="decrypted.txt"):
    """Lưu bản rõ đã giải mã vào file"""
    with open(filename, 'w') as f:
        f.write(plaintext)
    print(f"Bản rõ đã được lưu vào {filename}")

def main():
    """Chương trình chính"""
    print("=" * 60)
    print("HỆ MÃ HÓA TRAPDOOR KNAPSACK")
    print("=" * 60)
    
    while True:
        print("\nChọn chức năng:")
        print("1. Sinh khóa và mã hóa")
        print("2. Giải mã")
        print("3. Thoát")
        
        choice = input("\nNhập lựa chọn (1/2/3): ").strip()
        
        if choice == '1':
            # Sinh khóa
            print("\n--- SINH KHÓA ---")
            n = int(input("Nhập độ dài vector khóa N: "))
            
            print("\nĐang sinh khóa...")
            a_private, a_public, m, w, w_inverse = generate_keys(n)
            
            print("\n--- KHÓA BÍ MẬT ---")
            print(f"Vector siêu tăng a': {a_private}")
            print(f"m: {m}")
            print(f"w (omega): {w}")
            print(f"w^(-1) mod m: {w_inverse}")
            
            print("\n--- KHÓA CÔNG KHAI ---")
            print(f"a: {a_public}")
            
            # Lưu khóa
            save_private_key(a_private, m, w)
            save_public_key(a_public)
            
            # Mã hóa
            print("\n--- MÃ HÓA ---")
            plaintext_file = input("Nhập tên file bản rõ (chứa chuỗi bit): ").strip()
            
            if not os.path.exists(plaintext_file):
                print(f"File {plaintext_file} không tồn tại!")
                continue
            
            plaintext_bits = read_plaintext(plaintext_file)
            print(f"Bản rõ: {plaintext_bits}")
            print(f"Độ dài: {len(plaintext_bits)} bits")
            
            ciphertext = encrypt(plaintext_bits, a_public)
            print(f"\nBản mã: {ciphertext}")
            
            save_ciphertext(ciphertext)
            
        elif choice == '2':
            # Giải mã
            print("\n--- GIẢI MÃ ---")
            
            # Đọc khóa bí mật
            private_key_file = input("Nhập tên file khóa bí mật (mặc định: private_key.txt): ").strip()
            if not private_key_file:
                private_key_file = "private_key.txt"
            
            if not os.path.exists(private_key_file):
                print(f"File {private_key_file} không tồn tại!")
                continue
            
            a_private, m, w = load_private_key(private_key_file)
            
            print(f"\nĐã đọc khóa bí mật:")
            print(f"a': {a_private}")
            print(f"m: {m}")
            print(f"w: {w}")
            
            # Đọc bản mã
            cipher_file = input("\nNhập tên file bản mã (mặc định: cipher.txt): ").strip()
            if not cipher_file:
                cipher_file = "cipher.txt"
            
            if not os.path.exists(cipher_file):
                print(f"File {cipher_file} không tồn tại!")
                continue
            
            ciphertext = read_ciphertext(cipher_file)
            print(f"\nBản mã: {ciphertext}")
            
            # Giải mã
            plaintext_bits = decrypt(ciphertext, a_private, m, w)
            print(f"\nBản rõ đã giải mã: {plaintext_bits}")
            print(f"Độ dài: {len(plaintext_bits)} bits")
            
            # Lưu bản rõ
            output_file = input("\nNhập tên file lưu bản rõ (mặc định: decrypted.txt): ").strip()
            if not output_file:
                output_file = "decrypted.txt"
            
            save_plaintext(plaintext_bits, output_file)
            
        elif choice == '3':
            print("\nThoát chương trình. Tạm biệt!")
            break
        
        else:
            print("\nLựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()