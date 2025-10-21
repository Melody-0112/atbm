def ma_hoa_vigenere(plaintext, key):
    """
    Mã hóa văn bản sử dụng Vigenère cipher
    Công thức: Ci = (Pi + Ki) mod 26
    """
    ciphertext = ""
    key = key.upper()
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Xác định base (A hoặc a)
            base = ord('A') if char.isupper() else ord('a')
            
            # Chuyển ký tự thành số (0-25)
            Pi = ord(char.upper()) - ord('A')
            Ki = ord(key[key_index % len(key)]) - ord('A')
            
            # Áp dụng công thức mã hóa
            Ci = (Pi + Ki) % 26
            
            # Chuyển số về ký tự
            encrypted_char = chr(Ci + base)
            ciphertext += encrypted_char
            
            # Tăng key_index chỉ khi mã hóa chữ cái
            key_index += 1
        else:
            # Giữ nguyên ký tự không phải chữ cái
            ciphertext += char
    
    return ciphertext


def giai_ma_vigenere(ciphertext, key):
    """
    Giải mã văn bản sử dụng Vigenère cipher
    Công thức: Pi = (Ci - Ki + 26) mod 26
    """
    plaintext = ""
    key = key.upper()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Xác định base (A hoặc a)
            base = ord('A') if char.isupper() else ord('a')
            
            # Chuyển ký tự thành số (0-25)
            Ci = ord(char.upper()) - ord('A')
            Ki = ord(key[key_index % len(key)]) - ord('A')
            
            # Áp dụng công thức giải mã
            Pi = (Ci - Ki + 26) % 26
            
            # Chuyển số về ký tự
            decrypted_char = chr(Pi + base)
            plaintext += decrypted_char
            
            # Tăng key_index chỉ khi giải mã chữ cái
            key_index += 1
        else:
            # Giữ nguyên ký tự không phải chữ cái
            plaintext += char
    
    return plaintext


def main():
    print("=" * 50)
    print("CHƯƠNG TRÌNH MÃ HÓA VÀ GIẢI MÃ VIGENÈRE")
    print("=" * 50)
    
    # Nhập dữ liệu
    plaintext = input("\nNhập văn bản gốc (plaintext): ")
    key = input("Nhập khóa (key): ")
    
    # Kiểm tra key có hợp lệ không
    if not key.isalpha():
        print("Lỗi: Khóa phải chỉ chứa chữ cái!")
        return
    
    # Mã hóa
    ciphertext = ma_hoa_vigenere(plaintext, key)
    print("\n" + "-" * 50)
    print(f"Bản mã (ciphertext): {ciphertext}")
    
    # Giải mã
    decrypted_text = giai_ma_vigenere(ciphertext, key)
    print(f"Giải mã lại: {decrypted_text}")
    print("-" * 50)
    
    # Xác nhận kết quả
    if plaintext.upper() == decrypted_text.upper():
        print("✓ Mã hóa và giải mã thành công!")
    else:
        print("✗ Có lỗi xảy ra trong quá trình mã hóa/giải mã!")


if __name__ == "__main__":
    main()
    
    # Ví dụ demo
    print("\n" + "=" * 50)
    print("VÍ DỤ DEMO:")
    print("=" * 50)
    demo_plain = "HELLO WORLD"
    demo_key = "KEY"
    demo_cipher = ma_hoa_vigenere(demo_plain, demo_key)
    demo_decrypt = giai_ma_vigenere(demo_cipher, demo_key)
    
    print(f"Plaintext: {demo_plain}")
    print(f"Key: {demo_key}")
    print(f"Ciphertext: {demo_cipher}")
    print(f"Decrypted: {demo_decrypt}")