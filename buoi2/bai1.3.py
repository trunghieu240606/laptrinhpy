ho_ten = input("Nhap ho ten: ")
nam_sinh = int (input("Nhap nam sinh: "))
diem_tb = float(input("Nhap diem trung binh: "))

print(f"Ho va ten: {ho_ten} - Nam sinh: {nam_sinh} - DTB: {diem_tb:.2f}")

print("Ho va ten: {} - Nam sinh {} - DTB: {:.2f}".format(ho_ten, nam_sinh, diem_tb))

print("Ho va ten: %s - Nam sinh: %d _ DTB: %.2f" %(ho_ten, nam_sinh, diem_tb) )