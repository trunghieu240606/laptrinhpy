#list box
import tkinter as tk
from tkinter import ttk
cua_so = tk.Tk()
cua_so.title("Vi du Listbox")
cua_so.geometry("400x550")

listbox_monhoc = tk.Listbox(cua_so, selectmode="single")
for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_monhoc.insert(tk.END, mon)
listbox_monhoc.pack(pady=10)

nhan_ket_qua = tk.Label(cua_so, text="")
def xemMonHocDachon():
    lua_chon = listbox_monhoc.curselection()
    
    if lua_chon:
        nhan_ket_qua.config(text=f"Mon da chon: {listbox_monhoc.get(lua_chon[0])}")
        
tk.Button(cua_so, text="Xem mon da chon", command=xemMonHocDachon).pack(pady=5)

#bai 3.2
tk.Label(cua_so, text="Chon thanh pho:").pack(pady=10)
combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"])
combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)
nhan_ket_qua = tk.Label(cua_so, text="")
def xem_thanh_pho():
    nhan_ket_qua.config(text=f"Ban chon: {combobox_thanh_pho.get()}")
    
tk.Button(cua_so, text="Xac nhan", command=xem_thanh_pho).pack(pady=10)

nhan_ket_qua.pack()
cua_so.mainloop()