import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QGridLayout
from PyQt5.QtCore import Qt

class MayTinhBoTui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("May tinh bo tui - PyQt")
        self.setFixedSize(320, 420)
        self.khoi_tao_giao_dien()

    def khoi_tao_giao_dien(self):
        # Màn hình hiển thị kết quả
        self.man_hinh = QLineEdit()
        self.man_hinh.setReadOnly(True)
        self.man_hinh.setAlignment(Qt.AlignRight)
        self.man_hinh.setStyleSheet("font-size: 24px; padding: 10px; background-color: #f0f0f0; border: 1px solid #ccc;")

        # Bố cục lưới cho các nút bấm
        luoi_nut = QGridLayout()
        luoi_nut.setSpacing(8)

        # Danh sách các nút: (Nhãn nút, Dòng, Cột, Số hàng chiếm, Số cột chiếm)
        danh_sach_nut = [
            ("C", 0, 0, 1, 1), ("(", 0, 1, 1, 1), (")", 0, 2, 1, 1), ("/", 0, 3, 1, 1),
            ("7", 1, 0, 1, 1), ("8", 1, 1, 1, 1), ("9", 1, 2, 1, 1), ("*", 1, 3, 1, 1),
            ("4", 2, 0, 1, 1), ("5", 2, 1, 1, 1), ("6", 2, 2, 1, 1), ("-", 2, 3, 1, 1),
            ("1", 3, 0, 1, 1), ("2", 3, 1, 1, 1), ("3", 3, 2, 1, 1), ("+", 3, 3, 1, 1),
            ("0", 4, 0, 1, 1), (".", 4, 1, 1, 1), ("=", 4, 2, 1, 2)
        ]

        for text, hang, cot, row_span, col_span in danh_sach_nut:
            nut = QPushButton(text)
            nut.setFixedHeight(50)
            nut.setStyleSheet("font-size: 16px; font-weight: arial;")
            
            
            nut.clicked.connect(self.xu_ly_bam_nut)
            luoi_nut.addWidget(nut, hang, cot, row_span, col_span)

        # Layout tổng thể
        layout_chinh = QVBoxLayout()
        layout_chinh.addWidget(self.man_hinh)
        layout_chinh.addLayout(luoi_nut)
        self.setLayout(layout_chinh)

    def xu_ly_bam_nut(self):
        nut_duoc_bam = self.sender().text()
        noi_dung_hien_tai = self.man_hinh.text()

        if nut_duoc_bam == "C":
            self.man_hinh.clear()
        elif nut_duoc_bam == "=":
            try:
                # Đổi dấu x sang * nếu có và tính toán kết quả
                bieu_thuc = noi_dung_hien_tai
                ket_qua = str(eval(bieu_thuc))
                self.man_hinh.setText(ket_qua)
            except ZeroDivisionError:
                self.man_hinh.setText("Loi: Chia cho 0")
            except Exception:
                self.man_hinh.setText("Loi bieu thuc")
        else:
            # Nếu màn hình đang báo lỗi thì bấm số mới sẽ xóa trắng trước
            if "Loi" in noi_dung_hien_tai:
                noi_dung_hien_tai = ""
            self.man_hinh.setText(noi_dung_hien_tai + nut_duoc_bam)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = MayTinhBoTui()
    cua_so.show()
    sys.exit(app.exec_())