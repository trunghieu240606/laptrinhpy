ma_tran = [ 
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9] 
] 
 
for hang in ma_tran: 
    print(hang) 
 

for hang in ma_tran: 
    for phan_tu in hang: 
        print(phan_tu, end=" ") 
    print() 

tong = 0  
for hang in ma_tran:
    for phan_tu in hang:
      tong += phan_tu
    print()
    
print("tong: ", tong)
