diem = 6.5
tuoi = 20
diem_kha = diem >= 6.5 and diem < 8.0
print("Đạt điểm khá: ", diem_kha)

tuoi_t = tuoi < 18 or tuoi > 60
print("Chưa đủ 18 hoặc trên 60 tuổi: ", tuoi_t)

print("Phủ định điểm khá: ", not diem_kha)
print("Phủ định lại tuổi: ", not tuoi_t)

 