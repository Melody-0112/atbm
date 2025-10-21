def gcd_extended(a, b):
    """Thuật toán Euclid mở rộng"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def chinese_remainder_theorem(remainders, moduli):
    """
    Giải hệ phương trình đồng dư bằng Định lý Thặng dư Trung Hoa
    
    Input:
        remainders: danh sách các số dư [a1, a2, a3, ...]
        moduli: danh sách các modulo [m1, m2, m3, ...]
    
    Output:
        x: nghiệm của hệ phương trình
    """
    if len(remainders) != len(moduli):
        raise ValueError("Số lượng remainder và moduli phải bằng nhau")
    
    # Tính tích của tất cả các moduli
    M = 1
    for m in moduli:
        M *= m
    
    x = 0
    for i in range(len(moduli)):
        Mi = M // moduli[i]
        # Tìm nghịch đảo modular của Mi theo moduli[i]
        gcd, inv, _ = gcd_extended(Mi, moduli[i])
        if gcd != 1:
            raise ValueError("Các moduli phải nguyên tố cùng nhau")
        
        x += remainders[i] * Mi * inv
    
    return x % M


def modular_power(base, exp, mod):
    """
    Tính lũy thừa modulo: (base^exp) mod m
    
    Input:
        base: cơ số a
        exp: số mũ n
        mod: modulo m
    
    Output:
        Kết quả a^n mod m
    """
    result = 1
    base = base % mod
    
    while exp > 0:
        # Nếu exp lẻ, nhân base vào kết quả
        if exp % 2 == 1:
            result = (result * base) % mod
        
        # exp giờ phải chẵn
        exp = exp >> 1  # Chia 2
        base = (base * base) % mod
    
    return result


# Test Bài 1: Định lý Thặng dư Trung Hoa
print("=" * 60)
print("BÀI 1: HỆ PHƯƠNG TRÌNH ĐỒNG DƯ (Chinese Remainder Theorem)")
print("=" * 60)

# Ví dụ: x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7)
remainders = [2, 3, 2]
moduli = [3, 5, 7]

print(f"Hệ phương trình:")
for i in range(len(remainders)):
    print(f"  x ≡ {remainders[i]} (mod {moduli[i]})")

result = chinese_remainder_theorem(remainders, moduli)
print(f"\nNghiệm: x = {result}")

# Kiểm tra
print(f"\nKiểm tra:")
for i in range(len(moduli)):
    print(f"  {result} mod {moduli[i]} = {result % moduli[i]} (phải bằng {remainders[i]})")

print("\n" + "=" * 60)
print("BÀI 2: LŨY THỪA MODULO (Modular Exponentiation)")
print("=" * 60)

# Ví dụ: Tính 2^1000 mod 13
base = 2
exp = 1000
mod = 13

print(f"Tính: {base}^{exp} mod {mod}")
result = modular_power(base, exp, mod)
print(f"Kết quả: {result}")

# Thêm một vài ví dụ khác
print(f"\nThêm ví dụ:")
print(f"  3^1000000 mod 97 = {modular_power(3, 1000000, 97)}")
print(f"  5^999999 mod 1000000 = {modular_power(5, 999999, 1000000)}")
print(f"  123^456789 mod 1000000007 = {modular_power(123, 456789, 1000000007)}")

print("\n" + "=" * 60)
print("SỬ DỤNG HÀM:")
print("=" * 60)
print("""
# Bài 1: Định lý Thặng dư Trung Hoa
remainders = [a1, a2, a3, ...]  # Các số dư
moduli = [m1, m2, m3, ...]       # Các modulo
x = chinese_remainder_theorem(remainders, moduli)

# Bài 2: Lũy thừa modulo
result = modular_power(base, exp, mod)  # Tính base^exp mod mod
""")