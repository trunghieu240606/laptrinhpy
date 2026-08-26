cau = "Lap trinh Python rat thu vi"
print(cau[0]) 
print(cau[-1]) 
print(cau[4:10]) 
print(cau[:8])
print(cau[11:]) 
print(cau[::-1]) 

check = cau == cau[::-1]
print("Co phai palindrome khong:", check)