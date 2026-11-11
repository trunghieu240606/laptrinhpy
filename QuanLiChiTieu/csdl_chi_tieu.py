import sqlite3
import os

# Cố định đường dẫn file CSDL nằm ngay cùng thư mục với code
THU_MUC_HIEN_TAI = os.path.dirname(os.path.abspath(__file__))
TEN_FILE_CSDL = os.path.join(THU_MUC_HIEN_TAI, "chi_tieu.db")

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS chi_tieu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            noi_dung TEXT NOT NULL,
            so_tien INTEGER NOT NULL,
            danh_muc TEXT NOT NULL,
            ngay_chi TEXT NOT NULL
        )
    """)
    ket_noi.commit()
    ket_noi.close()

# ----------------- HÀM THÊM MỚI -----------------
def them_khoan_chi(noi_dung, so_tien, danh_muc, ngay_chi):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO chi_tieu (noi_dung, so_tien, danh_muc, ngay_chi) VALUES (?, ?, ?, ?)",
        (noi_dung, so_tien, danh_muc, ngay_chi)
    )
    ket_noi.commit()
    ket_noi.close()

# ----------------- HÀM HIỂN THỊ (LẤY DỮ LIỆU) -----------------
def lay_toan_bo_chi_tieu():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, noi_dung, so_tien, danh_muc, ngay_chi FROM chi_tieu ORDER BY id DESC")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

# ----------------- HÀM XÓA -----------------
def xoa_khoan_chi(id_chi_tieu):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM chi_tieu WHERE id = ?", (id_chi_tieu,))
    ket_noi.commit()
    ket_noi.close()

# ----------------- HÀM THỐNG KÊ -----------------
def thong_ke_theo_danh_muc():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT danh_muc, SUM(so_tien) FROM chi_tieu GROUP BY danh_muc")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua