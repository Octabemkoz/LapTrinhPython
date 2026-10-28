import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()
        # Nạp giao diện trực tiếp từ file form_dang_nhap.ui
        uic.loadUi("form_dang_nhap.ui", self)

        # Kết nối signal - slot cho nút đăng nhập
        self.nut_dang_nhap.clicked.connect(self.xu_ly_dang_nhap)

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text()
        mat_khau = self.o_nhap_mat_khau.text()

        # Kiểm tra nếu người dùng chưa nhập tài khoản hoặc mật khẩu
        if tai_khoan == "" or mat_khau == "":
            QMessageBox.critical(self, "Loi", "Vui long nhap day du tai khoan va mat khau.")
            return

        # Hiển thị thông báo đăng nhập thành công
        QMessageBox.information(self, "Thanh cong", f"Xin chao {tai_khoan}, dang nhap thanh cong!")

app = QApplication(sys.argv)
cua_so = CuaSoDangNhap()
cua_so.show()
sys.exit(app.exec_())