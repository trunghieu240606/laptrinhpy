import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()
cua_so.title("May Tinh")
cua_so.geometry("260x320")
cua_so.resizable(False, False)

bieu_thuc = ""
bien_hien_thi = tk.StringVar(value="0")

def bam_phim(ky_tu):
    global bieu_thuc
    if bien_hien_thi.get() == "Loi":
        bieu_thuc = ""
    bieu_thuc += str(ky_tu)
    bien_hien_thi.set(bieu_thuc)

def xoa_het():
    global bieu_thuc
    bieu_thuc = ""
    bien_hien_thi.set("0")

def xoa_lui():
    global bieu_thuc
    bieu_thuc = bieu_thuc[:-1]
    bien_hien_thi.set(bieu_thuc if bieu_thuc != "" else "0")

def tinh_ket_qua():
    global bieu_thuc
    try:
        ket_qua = eval(bieu_thuc)
        if isinstance(ket_qua, float) and ket_qua.is_integer():
            ket_qua = int(ket_qua)
        bien_hien_thi.set(str(ket_qua))
        bieu_thuc = str(ket_qua)
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0")
        bieu_thuc = ""
        bien_hien_thi.set("Loi")
    except Exception:
        bien_hien_thi.set("Loi")
        bieu_thuc = ""

man_hinh = tk.Entry(cua_so, textvariable=bien_hien_thi, font=("Arial", 16), justify="right", bd=5)
man_hinh.grid(row=0, column=0, columnspan=4, padx=5, pady=8, sticky="nsew")

cac_phim = [
    ("C", 1, 0, xoa_het),
    ("DEL", 1, 1, xoa_lui),
    ("/", 1, 2, lambda: bam_phim("/")),
    ("*", 1, 3, lambda: bam_phim("*")),

    ("7", 2, 0, lambda: bam_phim("7")),
    ("8", 2, 1, lambda: bam_phim("8")),
    ("9", 2, 2, lambda: bam_phim("9")),
    ("-", 2, 3, lambda: bam_phim("-")),

    ("4", 3, 0, lambda: bam_phim("4")),
    ("5", 3, 1, lambda: bam_phim("5")),
    ("6", 3, 2, lambda: bam_phim("6")),
    ("+", 3, 3, lambda: bam_phim("+")),

    ("1", 4, 0, lambda: bam_phim("1")),
    ("2", 4, 1, lambda: bam_phim("2")),
    ("3", 4, 2, lambda: bam_phim("3")),
    ("=", 4, 3, tinh_ket_qua),

    ("0", 5, 0, lambda: bam_phim("0")),
    (".", 5, 1, lambda: bam_phim(".")),
]


for ky_tu, hang, cot, lenh in cac_phim:
    span = 2 if ky_tu == "0" else 1
    cot_hien_tai = cot if ky_tu != "." else 2
    
    nut = tk.Button(cua_so, text=ky_tu, font=("Arial", 11), command=lenh)
    nut.grid(row=hang, column=cot_hien_tai, columnspan=span, sticky="nsew", padx=2, pady=2)

for r in range(1, 6):
    cua_so.rowconfigure(r, weight=1)
for c in range(4):
    cua_so.columnconfigure(c, weight=1)

cua_so.mainloop()