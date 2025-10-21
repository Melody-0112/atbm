def giai_ma_substitution(ban_ma, khoa):
    """
    Giải mã Substitution Cipher
    
    Args:
        ban_ma: Chuỗi đã được mã hóa (P)
        khoa: Khóa K - bảng mã thay thế 26 chữ cái
    
    Returns:
        Bản rõ đã được giải mã
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ban_ro = ''
    
    for ki_tu in ban_ma.upper():
        if ki_tu in khoa:
            # Tìm vị trí của ký tự trong khóa
            vi_tri = khoa.index(ki_tu)
            # Lấy ký tự tương ứng trong alphabet
            ban_ro += alphabet[vi_tri]
        else:
            # Giữ nguyên ký tự không phải chữ cái (dấu cách, số, ...)
            ban_ro += ki_tu
    
    return ban_ro


def ma_hoa_substitution(ban_ro, khoa):
    """
    Mã hóa Substitution Cipher
    
    Args:
        ban_ro: Chuỗi cần mã hóa
        khoa: Khóa K - bảng mã thay thế 26 chữ cái
    
    Returns:
        Bản mã
    """
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ban_ma = ''
    
    for ki_tu in ban_ro.upper():
        if ki_tu in alphabet:
            # Tìm vị trí của ký tự trong alphabet
            vi_tri = alphabet.index(ki_tu)
            # Lấy ký tự tương ứng trong khóa
            ban_ma += khoa[vi_tri]
        else:
            # Giữ nguyên ký tự không phải chữ cái
            ban_ma += ki_tu
    
    return ban_ma


# Ví dụ sử dụng
if __name__ == "__main__":
    # Khóa K (bảng thay thế 26 chữ cái)
    khoa = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    
    print("=== MÃ HÓA ===")
    ban_ro = "HELLO WORLD"
    ban_ma = ma_hoa_substitution(ban_ro, khoa)
    print(f"Bản rõ: {ban_ro}")
    print(f"Khóa K: {khoa}")
    print(f"Bản mã: {ban_ma}")
    
    print("\n=== GIẢI MÃ ===")
    ban_giai_ma = giai_ma_substitution(ban_ma, khoa)
    print(f"Bản mã: {ban_ma}")
    print(f"Khóa K: {khoa}")
    print(f"Bản rõ: {ban_giai_ma}")
    
    # Ví dụ khác
    print("\n=== VÍ DỤ 2 ===")
    ban_ro_2 = "PYTHON IS FUN"
    ban_ma_2 = ma_hoa_substitution(ban_ro_2, khoa)
    ban_giai_ma_2 = giai_ma_substitution(ban_ma_2, khoa)
    print(f"Bản rõ: {ban_ro_2}")
    print(f"Bản mã: {ban_ma_2}")
    print(f"Giải mã: {ban_giai_ma_2}")