import tkinter as tk
from tkinter import ttk, messagebox
import os
from datetime import datetime
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_chi_tieu as db

DANH_SACH_DANH_MUC = [
    "An uong",
    "Di chuyen",
    "Mua sam",
    "Tien nha - Dien nuoc",
    "Giai tri",
    "Khac"
]

class UngDungChiTieu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Chi tieu ca nhan")
        self.geometry("580x520")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()

        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Noi dung:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_noi_dung = tk.Entry(khung_nhap, width=32)
        self.o_nhap_noi_dung.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="So tien (VND):").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_so_tien = tk.Entry(khung_nhap, width=32)
        self.o_nhap_so_tien.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Danh muc:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_danh_muc = ttk.Combobox(khung_nhap, values=DANH_SACH_DANH_MUC, width=29, state="readonly")
        self.chon_danh_muc.current(0)
        self.chon_danh_muc.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them khoan chi", command=self.xu_ly_them_khoan_chi).grid(
            row=3, column=0, columnspan=2, pady=10
        )

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_chi_tieu = tk.Listbox(khung_danh_sach, width=75, height=14)
        self.listbox_chi_tieu.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_chi_tieu.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_chi_tieu.config(yscrollcommand=thanh_cuon.set)

        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button(khung_nut_thao_tac, text="Xoa khoan chi", command=self.xu_ly_xoa_khoan_chi).grid(
            row=0, column=0, padx=10
        )
        tk.Button(khung_nut_thao_tac, text="Thong ke chi tieu", command=self.xu_ly_thong_ke).grid(
            row=0, column=1, padx=10
        )

    def tai_lai_danh_sach(self):
        self.listbox_chi_tieu.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_chi_tieu()
        for item in self.danh_sach_hien_tai:
            id_ct, noi_dung, so_tien, danh_muc, ngay_chi = item
            so_tien_dinh_dang = f"{so_tien:,.0f} VND"
            self.listbox_chi_tieu.insert(
                tk.END, f"[{ngay_chi}] {noi_dung} - {so_tien_dinh_dang} ({danh_muc})"
            )

    def xu_ly_them_khoan_chi(self):
        noi_dung = self.o_nhap_noi_dung.get().strip()
        so_tien_str = self.o_nhap_so_tien.get().strip()
        danh_muc = self.chon_danh_muc.get()

        if noi_dung == "" or so_tien_str == "":
            messagebox.showerror("Loi", "Vui long nhap day du noi dung va so tien.")
            return

        try:
            so_tien = int(so_tien_str.replace(",", "").replace(".", ""))
            if so_tien <= 0:
                messagebox.showerror("Loi", "So tien phai lon hon 0.")
                return
        except ValueError:
            messagebox.showerror("Loi", "So tien phai la so nguyen hop le.")
            return

        ngay_chi = datetime.now().strftime("%d/%m/%Y")

        db.them_khoan_chi(noi_dung, so_tien, danh_muc, ngay_chi)
        
        self.o_nhap_noi_dung.delete(0, tk.END)
        self.o_nhap_so_tien.delete(0, tk.END)

        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", f"Da them: {noi_dung} ({so_tien:,.0f} VND)")

    def xu_ly_xoa_khoan_chi(self):
        lua_chon = self.listbox_chi_tieu.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon mot khoan chi trong danh sach de xoa.")
            return

        xac_nhan = messagebox.askyesno("Xac nhan", "Ban co chac chan muon xoa khoan chi nay?")
        if not xac_nhan:
            return

        id_ct = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_khoan_chi(id_ct)
        
        self.tai_lai_danh_sach()

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_danh_muc()
        if not du_lieu_thong_ke:
            messagebox.showinfo("Thong bao", "Chua co du lieu chi tieu de thong ke.")
            return

        cac_danh_muc = [dong[0] for dong in du_lieu_thong_ke]
        tong_tien = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(7, 5))
        plt.bar(cac_danh_muc, tong_tien, color="cornflowerblue")
        plt.title("Thong ke chi tieu theo danh muc")
        plt.xlabel("Danh muc")
        plt.ylabel("Tong so tien (VND)")
        plt.xticks(rotation=15)
        plt.tight_layout()

        thu_muc_hien_tai = os.path.dirname(os.path.abspath(__file__))
        duong_dan_anh = os.path.join(thu_muc_hien_tai, "thong_ke_chi_tieu.png")
        plt.savefig(duong_dan_anh)

        plt.show()

if __name__ == "__main__":
    ung_dung = UngDungChiTieu()
    ung_dung.mainloop()