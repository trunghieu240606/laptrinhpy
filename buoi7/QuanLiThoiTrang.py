danhSachSanPham = [
    {"maSP": "SP01", "tenSP": "Giay Sneaker Nam", "loaiSP": "Giay", "donGia": 450000, "soLuongTon": 15},
    {"maSP": "SP02", "tenSP": "Dep Quai Ngang", "loaiSP": "Dep", "donGia": 120000, "soLuongTon": 30},
    {"maSP": "SP03", "tenSP": "Quan Jean Slimfit", "loaiSP": "Quan", "donGia": 320000, "soLuongTon": 20},
    {"maSP": "SP04", "tenSP": "Ao Polo Classic", "loaiSP": "Ao", "donGia": 220000, "soLuongTon": 25},
    {"maSP": "SP05", "tenSP": "Vay Hoa Nhi Vintage", "loaiSP": "Vay", "donGia": 380000, "soLuongTon": 10}
]

lichSuBanHang = []

def nhapSoNguyenDuong(loiNhac):
    while True:
        try:
            giaTri = int(input(loiNhac))
            if giaTri > 0:
                return giaTri
            print("-> Vui long nhap mot so nguyen duong lon hon 0.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")

def timSanPhamTheoMa(maSP):
    for sp in danhSachSanPham:
        if sp["maSP"].upper() == maSP.upper():
            return sp
    return None

def hienThiDanhSachSanPham():
    print("\n" + "=" * 78)
    print(f"{'Ma SP':<10}{'Ten San Pham':<25}{'Phan Loai':<12}{'Don Gia':<15}{'Ton Kho':<10}")
    print("-" * 78)
    for sp in danhSachSanPham:
        giaStr = f"{sp['donGia']:,} VND"
        print(f"{sp['maSP']:<10}{sp['tenSP']:<25}{sp['loaiSP']:<12}{giaStr:<15}{sp['soLuongTon']:<10}")
    print("=" * 78)

def xemSanPhamTheoLoai():
    loaiCanXem = input("Nhap loai can loc (Giay/Dep/Quan/Ao/Vay): ").strip().title()
    danhSachLoc = [sp for sp in danhSachSanPham if sp["loaiSP"].lower() == loaiCanXem.lower()]
    
    if len(danhSachLoc) == 0:
        print(f"-> Khong co san pham nao thuoc loai '{loaiCanXem}'.")
        return
        
    print(f"\nDANH SACH SAN PHAM THUOC LOAI: {loaiCanXem.upper()}")
    print("-" * 65)
    for sp in danhSachLoc:
        print(f"  {sp['maSP']} - {sp['tenSP']} | Gia: {sp['donGia']:,} VND | Con: {sp['soLuongTon']}")

def themSanPhamMoi():
    maSP = input("Nhap ma san pham moi (VD: SP06): ").strip().upper()
    if timSanPhamTheoMa(maSP) is not None:
        print(f"-> Ma san pham {maSP} da ton tai, khong the them!")
        return

    tenSP = input("Nhap ten san pham: ").strip().title()
    loaiSP = input("Nhap loai san pham (Giay/Dep/Quan/Ao/Vay): ").strip().title()
    donGia = nhapSoNguyenDuong("Nhap don gia: ")
    soLuongTon = nhapSoNguyenDuong("Nhap so luong ton ban dau: ")

    danhSachSanPham.append({
        "maSP": maSP,
        "tenSP": tenSP,
        "loaiSP": loaiSP,
        "donGia": donGia,
        "soLuongTon": soLuongTon
    })
    print(f"-> Da them san pham '{tenSP}' (Ma: {maSP}) thanh cong!")

def nhapHang():
    maSP = input("Nhap ma san pham muon nhap them: ").strip().upper()
    sp = timSanPhamTheoMa(maSP)
    if sp is None:
        print(f"-> Khong tim thay san pham co ma {maSP}.")
        return

    soLuongThem = nhapSoNguyenDuong(f"Nhap so luong can them cho '{sp['tenSP']}': ")
    sp["soLuongTon"] += soLuongThem
    print(f"-> Da nhap thanh cong! Ton kho hien tai cua {sp['maSP']}: {sp['soLuongTon']}")

def banHang():
    maSP = input("Nhap ma san pham khach mua: ").strip().upper()
    sp = timSanPhamTheoMa(maSP)
    if sp is None:
        print(f"-> Khong tim thay san pham co ma {maSP}.")
        return

    if sp["soLuongTon"] == 0:
        print(f"-> San pham '{sp['tenSP']}' da het hang.")
        return

    print(f"-> San pham: {sp['tenSP']} | Gia: {sp['donGia']:,} VND | Hien con: {sp['soLuongTon']}")
    soLuongMua = nhapSoNguyenDuong("Nhap so luong can mua: ")

    if soLuongMua > sp["soLuongTon"]:
        print(f"-> Kho chi con {sp['soLuongTon']} san pham, khong du dap ung.")
        return

    thanhTien = soLuongMua * sp["donGia"]
    sp["soLuongTon"] -= soLuongMua

    lichSuBanHang.append({
        "maSP": maSP,
        "tenSP": sp["tenSP"],
        "soLuong": soLuongMua,
        "thanhTien": thanhTien
    })

    print(f"-> Giao dich thanh cong!")
    print(f"-> Tong tien phai thanh toan: {thanhTien:,} VND")
    print(f"-> So luong con lai trong kho: {sp['soLuongTon']}")

def thongKeDoanhThu():
    if len(lichSuBanHang) == 0:
        print("-> Chua co giao dich ban hang nao duoc ghi nhan.")
        return

    tongTien = 0
    print("\nLICH SU BAN HANG CHI TIET:")
    print("-" * 65)
    for gd in lichSuBanHang:
        print(f"  {gd['maSP']} | {gd['tenSP']} | So luong: {gd['soLuong']} | {gd['thanhTien']:,} VND")
        tongTien += gd["thanhTien"]
    print("-" * 65)
    print(f">>> TONG DOANH THU BAN HANG: {tongTien:,} VND")

def hienThiMenu():
    print("\n" + "=" * 18 + " QUAN LY SHOP THOI TRANG " + "=" * 18)
    print("1. Hien thi danh sach tat ca san pham")
    print("2. Xem san pham theo loai (Giay/Dep/Quan/Ao/Vay)")
    print("3. Them san pham moi")
    print("4. Nhap them hang vao kho")
    print("5. Ban hang / Tao hoa don")
    print("6. Thong ke doanh thu & lich su ban hang")
    print("0. Thoat chuong trinh")

def chayChuongTrinh():
    while True:
        hienThiMenu()
        luaChon = input("Nhap lua chon cua ban (0-6): ").strip()
        if luaChon == "1":
            hienThiDanhSachSanPham()
        elif luaChon == "2":
            xemSanPhamTheoLoai()
        elif luaChon == "3":
            themSanPhamMoi()
        elif luaChon == "4":
            nhapHang()
        elif luaChon == "5":
            banHang()
        elif luaChon == "6":
            thongKeDoanhThu()
        elif luaChon == "0":
            print("Cam on ban da su dung phan mem quan ly shop. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long nhap tu 0 den 6.")

if __name__ == "__main__":
    chayChuongTrinh()
danhSachSanPham = [
    {"maSP": "SP01", "tenSP": "Giay Sneaker Nam", "loaiSP": "Giay", "donGia": 450000, "soLuongTon": 15},
    {"maSP": "SP02", "tenSP": "Dep Quai Ngang", "loaiSP": "Dep", "donGia": 120000, "soLuongTon": 30},
    {"maSP": "SP03", "tenSP": "Quan Jean Slimfit", "loaiSP": "Quan", "donGia": 320000, "soLuongTon": 20},
    {"maSP": "SP04", "tenSP": "Ao Polo Classic", "loaiSP": "Ao", "donGia": 220000, "soLuongTon": 25},
    {"maSP": "SP05", "tenSP": "Vay Hoa Nhi Vintage", "loaiSP": "Vay", "donGia": 380000, "soLuongTon": 10}
]

lichSuBanHang = []


def nhapSoNguyenDuong(loiNhac):
    while True:
        try:
            giaTri = int(input(loiNhac))
            if giaTri > 0:
                return giaTri
            print("-> Vui long nhap mot so nguyen duong lon hon 0")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen")

def timSanPhamTheoMa(maSP):
    for sp in danhSachSanPham:
        if sp["maSP"].upper() == maSP.upper():
            return sp
    return None

def hienThiDanhSachSanPham():
    print("\n" + "=" * 78)
    print(f"{'Ma SP':<10}{'Ten San Pham':<25}{'Phan Loai':<12}{'Don Gia':<15}{'Ton Kho':<10}")
    print("-" * 78)
    for sp in danhSachSanPham:
        giaStr = f"{sp['donGia']:,} VND"
        print(f"{sp['maSP']:<10}{sp['tenSP']:<25}{sp['loaiSP']:<12}{giaStr:<15}{sp['soLuongTon']:<10}")
    print("=" * 78)

def xemSanPhamTheoLoai():
    loaiCanXem = input("Nhap loai can loc (giay/dep/quan/ao/vay): ").strip().title()
    danhSachLoc = [sp for sp in danhSachSanPham if sp["loaiSP"].lower() == loaiCanXem.lower()]
    
    if len(danhSachLoc) == 0:
        print(f"-> Khong co san pham nao thuoc loai '{loaiCanXem}'")
        return
        
    print(f"\nDANH SACH SAN PHAM THUOC LOAI: {loaiCanXem.upper()}")
    print("-" * 65)
    for sp in danhSachLoc:
        print(f"  {sp['maSP']} - {sp['tenSP']} | Gia: {sp['donGia']:,} VND | Con: {sp['soLuongTon']}")

def themSanPhamMoi():
    maSP = input("Nhap ma san pham moi (VD: SP06): ").strip().upper()
    if timSanPhamTheoMa(maSP) is not None:
        print(f"-> Ma san pham {maSP} da ton tai, khong the them")
        return

    tenSP = input("Nhap ten san pham: ").strip().title()
    loaiSP = input("Nhap loai san pham (giay/dep/quan/ao/vay): ").strip().title()
    donGia = nhapSoNguyenDuong("Nhap don gia: ")
    soLuongTon = nhapSoNguyenDuong("Nhap so luong ton ban dau: ")

    danhSachSanPham.append({
        "maSP": maSP,
        "tenSP": tenSP,
        "loaiSP": loaiSP,
        "donGia": donGia,
        "soLuongTon": soLuongTon
    })
    print(f"-> Da them san pham '{tenSP}' (Ma: {maSP}) thanh cong!")

def nhapHang():
    maSP = input("Nhap ma san pham muon nhap them: ").strip().upper()
    sp = timSanPhamTheoMa(maSP)
    if sp is None:
        print(f"-> Khong tim thay san pham co ma {maSP}.")
        return

    soLuongThem = nhapSoNguyenDuong(f"Nhap so luong can them cho '{sp['tenSP']}': ")
    sp["soLuongTon"] += soLuongThem
    print(f"-> Da nhap thanh cong! Ton kho hien tai cua {sp['maSP']}: {sp['soLuongTon']}")

def banHang():
    maSP = input("Nhap ma san pham khach mua: ").strip().upper()
    sp = timSanPhamTheoMa(maSP)
    if sp is None:
        print(f"-> Khong tim thay san pham co ma {maSP}.")
        return

    if sp["soLuongTon"] == 0:
        print(f"-> San pham '{sp['tenSP']}' da het hang.")
        return

    print(f"-> San pham: {sp['tenSP']} | Gia: {sp['donGia']:,} VND | Hien con: {sp['soLuongTon']}")
    soLuongMua = nhapSoNguyenDuong("Nhap so luong can mua: ")

    if soLuongMua > sp["soLuongTon"]:
        print(f"-> Kho chi con {sp['soLuongTon']} san pham, khong du dap ung")
        return

    thanhTien = soLuongMua * sp["donGia"]
    sp["soLuongTon"] -= soLuongMua

    lichSuBanHang.append({
        "maSP": maSP,
        "tenSP": sp["tenSP"],
        "soLuong": soLuongMua,
        "thanhTien": thanhTien
    })

    print(f"-> Giao dich thanh cong!")
    print(f"-> Tong tien phai thanh toan: {thanhTien:,} VND")
    print(f"-> So luong con lai trong kho: {sp['soLuongTon']}")

def thongKeDoanhThu():
    if len(lichSuBanHang) == 0:
        print("-> Chua co giao dich ban hang nao duoc ghi nhan")
        return

    tongTien = 0
    print("\nLICH SU BAN HANG CHI TIET:")
    print("-" * 65)
    for gd in lichSuBanHang:
        print(f"  {gd['maSP']} | {gd['tenSP']} | So luong: {gd['soLuong']} | {gd['thanhTien']:,} VND")
        tongTien += gd["thanhTien"]
    print("-" * 65)
    print(f">>> TONG DOANH THU BAN HANG: {tongTien:,} VND")

def hienThiMenu():
    print("\n" + "=" * 18 + " QUAN LY SHOP THOI TRANG " + "=" * 18)
    print("1. Hien thi danh sach tat ca san pham")
    print("2. Xem san pham theo loai (Giay/Dep/Quan/Ao/Vay)")
    print("3. Them san pham moi")
    print("4. Nhap them hang vao kho")
    print("5. Ban hang / Tao hoa don")
    print("6. Thong ke doanh thu & lich su ban hang")
    print("0. Thoat chuong trinh")

def chayChuongTrinh():
    while True:
        hienThiMenu()
        luaChon = input("Nhap lua chon cua ban (0-6): ").strip()
        if luaChon == "1":
            hienThiDanhSachSanPham()
        elif luaChon == "2":
            xemSanPhamTheoLoai()
        elif luaChon == "3":
            themSanPhamMoi()
        elif luaChon == "4":
            nhapHang()
        elif luaChon == "5":
            banHang()
        elif luaChon == "6":
            thongKeDoanhThu()
        elif luaChon == "0":
            print("Cam on ban da su dung phan mem quan ly")
            break
        else:
            print("-> Lua chon khong hop le, vui long nhap tu 0 den 6")

if __name__ == "__main__":
    chayChuongTrinh()