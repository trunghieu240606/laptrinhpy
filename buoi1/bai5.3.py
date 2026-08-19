x = 10
x += 5
print("x += ", x)

x -= 3
print("x -= ", x)

x *= 3
print("x *= ", x)

x /= 2
print("x /= ", x)

x //= 3
print("x //= ", x)

x **= 2
print("x **= ", x)

danh_sach = [1, 2, 3, "python"]
print("3 có trong danh sách không: " , 3 in danh_sach)

danh_sach_a = danh_sach
danh_sach_b = [1,2,3, "python"]

print("danh_sach_a is danh_sach: ", danh_sach_a is danh_sach)
print("danh_sach_b is danh_sach: ", danh_sach_b is danh_sach)
