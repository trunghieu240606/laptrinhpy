# Danh sach phong ban dau
danhSachPhong = [
    {"maPhong": "P101", "loaiPhong": "Don", "gia": 300000, "trangThai": "Trong", "tenKhach": ""},
    {"maPhong": "P102", "loaiPhong": "Doi", "gia": 500000, "trangThai": "Trong", "tenKhach": ""},
    {"maPhong": "P103", "loaiPhong": "VIP", "gia": 900000, "trangThai": "Trong", "tenKhach": ""},
    {"maPhong": "P104", "loaiPhong": "Signature", "gia": 1500000, "trangThai": "Trong", "tenKhach": ""}
]

lichSuDoanhThu = []

def hienThiDanhSachPhong():
    print("\n" + "=" * 65)
    print(f"{'Ma Phong':<10} {'Loai Phong':<15} {'Gia/dem':<15} {'Trang Thai':<12} {'Ten Khach':<15}")
    print("-" * 65)
    for phong in danhSachPhong:
        giaStr = f"{phong['gia']:,} VND"
        print(f"{phong['maPhong']:<10} {phong['loaiPhong']:<15} {giaStr:<15} {phong['trangThai']:<12} {phong['tenKhach']:<15}")
    print("=" * 65)

def timPhongTheoMa(maPhong):
    for phong in danhSachPhong:
        if phong["maPhong"] == maPhong:
            return phong
    return None

def xemPhongTrong():
    phongTrong = [phong for phong in danhSachPhong if phong["trangThai"] == "Trong"]
    if len(phongTrong) == 0:
        print("-> Hien khong con phong trong nao.")
        return
    print("\nCAC PHONG DANG TRONG:")
    for phong in phongTrong:
        print(f"  {phong['maPhong']} - {phong['loaiPhong']} - {phong['gia']:,} VND/dem")

def themPhong(maPhong, loaiPhong, gia):
    if timPhongTheoMa(maPhong) is not None:
        print(f"-> Ma phong {maPhong} da ton tai, khong the them.")
        return
    danhSachPhong.append({
        "maPhong": maPhong,
        "loaiPhong": loaiPhong,
        "gia": gia,
        "trangThai": "Trong",
        "tenKhach": ""
    })
    print(f"-> Da them phong {maPhong} thanh cong.")

def datPhong(maPhong, tenKhach):
    phong = timPhongTheoMa(maPhong)
    if phong is None:
        print(f"-> Khong tim thay phong {maPhong}.")
        return
    if phong["trangThai"] == "Da dat":
        print(f"-> Phong {maPhong} da co khach, khong the dat.")
        return
    phong["trangThai"] = "Da dat"
    phong["tenKhach"] = tenKhach
    print(f"-> Dat phong {maPhong} cho khach {tenKhach} thanh cong.")

def traPhong(maPhong, soDem):
    phong = timPhongTheoMa(maPhong)
    if phong is None:
        print(f"-> Khong tim thay phong {maPhong}.")
        return
    if phong["trangThai"] == "Trong":
        print(f"-> Phong {maPhong} dang trong, khong co khach de tra phong.")
        return
    
    thanhTien = phong["gia"] * soDem
    lichSuDoanhThu.append({
        "maPhong": maPhong,
        "tenKhach": phong["tenKhach"],
        "soDem": soDem,
        "thanhTien": thanhTien
    })
    print(f"-> Khach {phong['tenKhach']} tra phong {maPhong} sau {soDem} dem.")
    print(f"-> Tong tien phai thanh toan: {thanhTien:,} VND")
    phong["trangThai"] = "Trong"
    phong["tenKhach"] = ""

def thongKeDoanhThu():
    if len(lichSuDoanhThu) == 0:
        print("-> Chua co giao dich tra phong nao.")
        return
    tongDoanhThu = 0
    print("\nLICH SU GIAO DICH:")
    for giaoDich in lichSuDoanhThu:
        print(f"  {giaoDich['maPhong']} | {giaoDich['tenKhach']} | {giaoDich['soDem']} dem | {giaoDich['thanhTien']:,} VND")
        tongDoanhThu += giaoDich["thanhTien"]
    print(f"\n>>> TONG DOANH THU: {tongDoanhThu:,} VND")

def nhapSoNguyen(loiNhac):
    while True:
        try:
            giaTri = int(input(loiNhac))
            if giaTri > 0:
                return giaTri
            print("-> Vui long nhap mot so nguyen duong (lon hon 0).")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so nguyen.")

def hienThiMenu():
    print("\n===== QUAN LY DAT PHONG KHACH SAN MINI =====")
    print("1. Hien thi danh sach tat ca phong")
    print("2. Xem cac phong dang trong")
    print("3. Them phong moi")
    print("4. Dat phong cho khach")
    print("5. Tra phong / Thanh toan")
    print("6. Thong ke doanh thu")
    print("0. Thoat chuong trinh")

def chayChuongTrinh():
    while True:
        hienThiMenu()
        luaChon = input("Nhap lua chon cua ban: ").strip()
        if luaChon == "1":
            hienThiDanhSachPhong()
        elif luaChon == "2":
            xemPhongTrong()
        elif luaChon == "3":
            maPhong = input("Nhap ma phong moi: ").strip().upper()
            loaiPhong = input("Nhap loai phong (Don/Doi/VIP): ").strip().title()
            gia = nhapSoNguyen("Nhap gia phong/dem: ")
            themPhong(maPhong, loaiPhong, gia)
        elif luaChon == "4":
            maPhong = input("Nhap ma phong can dat: ").strip().upper()
            tenKhach = input("Nhap ten khach: ").strip().title()
            datPhong(maPhong, tenKhach)
        elif luaChon == "5":
            maPhong = input("Nhap ma phong can tra: ").strip().upper()
            soDem = nhapSoNguyen("Nhap so dem da o: ")
            traPhong(maPhong, soDem)
        elif luaChon == "6":
            thongKeDoanhThu()
        elif luaChon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chayChuongTrinh()