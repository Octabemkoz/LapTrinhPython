
# ĐỒ ÁN NHỎ: CHƯƠNG TRÌNH QUẢN LÝ THƯ VIỆN SÁCH 

# 1. Khai báo dữ liệu ban đầu
danh_sach_sach = [
    {"ma_sach": "S101", "ten_sach": "Lap trinh Python co ban", "tac_gia": "Nguyen Van A", "nam_xb": 2022, "trang_thai": "San co", "nguoi_muon": ""},
    {"ma_sach": "S102", "ten_sach": "Cua Hang Giay Cu", "tac_gia": "Higashino Keigo", "nam_xb": 2020, "trang_thai": "San co", "nguoi_muon": ""},
    {"ma_sach": "S103", "ten_sach": "Cau Truc Du Lieu & Giai Thuat", "tac_gia": "Tran B", "nam_xb": 2021, "trang_thai": "San co", "nguoi_muon": ""},
    {"ma_sach": "S104", "ten_sach": "Dac Nhan Tam", "tac_gia": "Dale Carnegie", "nam_xb": 2019, "trang_thai": "San co", "nguoi_muon": ""},
]

lich_su_tra_sach = []

# 2. Các hàm hiển thị và tìm kiếm
def hien_thi_danh_sach_sach():
    print("\n" + "=" * 80)
    print(f"{'Ma sach':<10}{'Ten sach':<30}{'Tac gia':<18}{'Nam XB':<10}{'Trang thai':<12}{'Nguoi muon':<15}")
    print("-" * 80)
    for sach in danh_sach_sach:
        print(f"{sach['ma_sach']:<10}{sach['ten_sach']:<30}{sach['tac_gia']:<18}{sach['nam_xb']:<10}{sach['trang_thai']:<12}{sach['nguoi_muon']:<15}")
    print("-" * 80)

def tim_sach_theo_ma(ma_sach):
    for sach in danh_sach_sach:
        if sach["ma_sach"] == ma_sach:
            return sach
    return None

def xem_sach_san_co():
    sach_co = [sach for sach in danh_sach_sach if sach["trang_thai"] == "San co"]
    if len(sach_co) == 0:
        print("-> Hien tai tat ca sach trong thu vien deu da duoc muon.")
        return
    print("\n>>> DANH SÁCH SÁCH ĐANG SẴN CÓ:")
    for sach in sach_co:
        print(f"  [{sach['ma_sach']}] {sach['ten_sach']} - Tac gia: {sach['tac_gia']} ({sach['nam_xb']})")

# 3. Các hàm nghiệp vụ: Thêm, Mượn, Trả
def them_sach(ma_sach, ten_sach, tac_gia, nam_xb):
    if tim_sach_theo_ma(ma_sach) is not None:
        print(f"-> Ma sach {ma_sach} da ton tai trong he thong! Khong the them.")
        return
    danh_sach_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": ten_sach,
        "tac_gia": tac_gia,
        "nam_xb": nam_xb,
        "trang_thai": "San co",
        "nguoi_muon": ""
    })
    print(f"-> Da them sach '{ten_sach}' (Ma: {ma_sach}) vao thu vien thanh cong!")

def muon_sach(ma_sach, nguoi_muon):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay ma sach {ma_sach} trong thu vien.")
        return
    if sach["trang_thai"] == "Da muon":
        print(f"-> Sach {ma_sach} hien da duoc mượn boi '{sach['nguoi_muon']}'.")
        return
    
    sach["trang_thai"] = "Da muon"
    sach["nguoi_muon"] = nguoi_muon
    print(f"-> Cho phat sach '{sach['ten_sach']}' cho doc gia '{nguoi_muon}' thanh cong!")

def tra_sach(ma_sach, so_ngay_muon):
    sach = tim_sach_theo_ma(ma_sach)
    if sach is None:
        print(f"-> Khong tim thay ma sach {ma_sach}.")
        return
    if sach["trang_thai"] == "San co":
        print(f"-> Sach {ma_sach} dang co o thu vien, khong co ai muon de tra.")
        return
    
    # Quy định: Tối đa 14 ngày. Quá hạn phạt 5.000 VNĐ / ngày quá hạn
    NGAY_QUY_DINH = 14
    PHI_PHAT_NGAY = 5000
    tien_phat = 0
    
    if so_ngay_muon > NGAY_QUY_DINH:
        ngay_qua_han = so_ngay_muon - NGAY_QUY_DINH
        tien_phat = ngay_qua_han * PHI_PHAT_NGAY
        print(f"-> Sach mượn qua han {ngay_qua_han} ngay! Phi phat: {tien_phat:,} VND")
    else:
        print("-> Tra sach dung han quy dinh (khong co phi phat).")

    lich_su_tra_sach.append({
        "ma_sach": ma_sach,
        "ten_sach": sach["ten_sach"],
        "nguoi_muon": sach["nguoi_muon"],
        "so_ngay": so_ngay_muon,
        "tien_phat": tien_phat
    })

    print(f"-> Da nhan lai sach '{sach['ten_sach']}' tu doc gia '{sach['nguoi_muon']}'.")
    sach["trang_thai"] = "San co"
    sach["nguoi_muon"] = ""

def thong_ke_doanh_thu():
    if len(lich_su_tra_sach) == 0:
        print("-> Chua co giao dich tra sach nao duoc ghi nhận.")
        return
    tong_tien_phat = 0
    print("\n" + "=" * 60)
    print("LICH SU TRA SACH & PHI PHAT:")
    print("-" * 60)
    for gd in lich_su_tra_sach:
        print(f"  + Sach: {gd['ten_sach']} ({gd['ma_sach']}) | Nguoi muon: {gd['nguoi_muon']} | Ngay muon: {gd['so_ngay']} | Phạt: {gd['tien_phat']:,} VND")
        tong_tien_phat += gd["tien_phat"]
    print("-" * 60)
    print(f">>> TONG PHI PHAT THU DUOC: {tong_tien_phat:,} VND")

# 4. Hàm nhập số an toàn với try-except
def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            val = int(input(loi_nhac))
            if val > 0:
                return val
            print("-> Gia tri nhap phai la so nguyen duong (> 0). Vui long nhap lai!")
        except ValueError:
            print("-> Du lieu khong hop le! Vui long nhap mot so nguyen.")

# 5. Menu chính & Vòng lập chương trình
def hien_thi_menu():
    print("\n===== CHUONG TRINH QUAN LY THU VIEN =====")
    print("1. Hien thi danh sach tat ca sach")
    print("2. Xem danh sach sach dang san co")
    print("3. Them sach moi")
    print("4. Muon sach")
    print("5. Tra sach & Tinh phi phat")
    print("6. Thong ke phi phat / Doanh thu")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban (0-6): ").strip()
        
        if lua_chon == "1":
            hien_thi_danh_sach_sach()
        elif lua_chon == "2":
            xem_sach_san_co()
        elif lua_chon == "3":
            ma_sach = input("Nhap ma sach moi (vd: S105): ").strip().upper()
            ten_sach = input("Nhap ten sach: ").strip().title()
            tac_gia = input("Nhap ten tac gia: ").strip().title()
            nam_xb = nhap_so_nguyen("Nhap nam xuat ban: ")
            them_sach(ma_sach, ten_sach, tac_gia, nam_xb)
        elif lua_chon == "4":
            ma_sach = input("Nhap ma sach can muon: ").strip().upper()
            nguoi_muon = input("Nhap ten nguoi muon: ").strip().title()
            muon_sach(ma_sach, nguoi_muon)
        elif lua_chon == "5":
            ma_sach = input("Nhap ma sach can tra: ").strip().upper()
            so_ngay = nhap_so_nguyen("Nhap so ngay da muon: ")
            tra_sach(ma_sach, so_ngay)
        elif lua_chon == "6":
            thong_ke_doanh_thu()
        elif lua_chon == "0":
            print("Cam on ban da su dung chuong trinh quan ly thu vien. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long nhap tu 0 den 6.")

if __name__ == "__main__":
    chay_chuong_trinh()