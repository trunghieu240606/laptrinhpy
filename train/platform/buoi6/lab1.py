age = int(input("Nhap tuoi: "))
ID = input("Y or N\n") == "Y"

if age >= 18 and ID:
    print("Du dieu kien di tu")
else:
    print("Di trai")