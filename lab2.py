def gcd_mo_rong(a, n):
    """
    Thuật toán Euclid mở rộng
    Trả về: (gcd, x, y) sao cho a*x + n*y = gcd(a, n)
    """
    if n == 0:
        return a, 1, 0
    
    # Lưu giá trị ban đầu
    r_truoc, r_hien = a, n
    x_truoc, x_hien = 1, 0
    y_truoc, y_hien = 0, 1
    
    while r_hien != 0:
        # Tính thương và số dư
        thuong = r_truoc // r_hien
        
        # Cập nhật r
        r_truoc, r_hien = r_hien, r_truoc - thuong * r_hien
        
        # Cập nhật x
        x_truoc, x_hien = x_hien, x_truoc - thuong * x_hien
        
        # Cập nhật y
        y_truoc, y_hien = y_hien, y_truoc - thuong * y_hien
    
    return r_truoc, x_truoc, y_truoc


def tim_nghich_dao(a, n):
    """
    Tìm nghịch đảo của A theo modulo N
    Trả về X sao cho: A*X ≡ 1 (mod N)
    """
    # Tính GCD và hệ số x, y
    gcd, x, y = gcd_mo_rong(a, n)
    
    # Kiểm tra xem có tồn tại nghịch đảo không
    if gcd != 1:
        return None  # Không tồn tại nghịch đảo
    
    # Đảm bảo x là số dương trong khoảng [0, n)
    x = x % n
    
    return x


def main():
    print("=" * 60)
    print("CHƯƠNG TRÌNH TÌM NGHỊCH ĐẢO MODULO")
    print("Thuật toán Euclid Mở Rộng")
    print("=" * 60)
    print()
    
    # Bước 1: Nhập số nguyên A và N
    try:
        a = int(input("Nhập số nguyên A: "))
        n = int(input("Nhập số nguyên N (đại diện cho vành Zₙ): "))
        
        # Kiểm tra điều kiện
        if n <= 0:
            print("\n❌ Lỗi: N phải là số nguyên dương!")
            return
        
        # Chuẩn hóa A về [0, N)
        a = a % n
        
        print("\n" + "-" * 60)
        print(f"Tìm nghịch đảo của A = {a} theo modulo N = {n}")
        print("-" * 60)
        
        # Bước 2: Áp dụng thuật toán Euclid mở rộng
        gcd, x, y = gcd_mo_rong(a, n)
        
        print(f"\nKết quả thuật toán Euclid mở rộng:")
        print(f"  GCD({a}, {n}) = {gcd}")
        print(f"  Hệ số: x = {x}, y = {y}")
        print(f"  Kiểm tra: {a}×({x}) + {n}×({y}) = {a*x + n*y}")
        
        # Bước 3: Kiểm tra điều kiện tồn tại
        if gcd != 1:
            print(f"\n❌ KHÔNG TỒN TẠI NGHỊCH ĐẢO!")
            print(f"   Lý do: GCD({a}, {n}) = {gcd} ≠ 1")
            print(f"   {a} và {n} không nguyên tố cùng nhau.")
        else:
            # Bước 4: Tính nghịch đảo
            nghich_dao = x % n
            
            print(f"\n✓ TỒN TẠI NGHỊCH ĐẢO!")
            print(f"  Nghịch đảo của {a} theo modulo {n} là: X = {nghich_dao}")
            
            # Kiểm tra kết quả
            kiem_tra = (a * nghich_dao) % n
            print(f"\n✓ Kiểm tra:")
            print(f"  {a} × {nghich_dao} ≡ {kiem_tra} (mod {n})")
            
            if kiem_tra == 1:
                print("  ✓ Kết quả đúng! ✓")
            else:
                print("  ✗ Có lỗi trong tính toán!")
        
        print("\n" + "=" * 60)
        
    except ValueError:
        print("\n❌ Lỗi: Vui lòng nhập số nguyên hợp lệ!")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")


if __name__ == "__main__":
    main()
    
    # Hỏi có muốn thử lại không
    while True:
        print()
        tiep_tuc = input("Bạn có muốn tính tiếp không? (c/k): ").strip().lower()
        if tiep_tuc == 'c':
            print("\n")
            main()
        else:
            print("\nCảm ơn bạn đã sử dụng chương trình!")
            break