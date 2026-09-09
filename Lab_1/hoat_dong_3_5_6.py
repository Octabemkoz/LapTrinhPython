
print("========== HOẠT ĐỘNG 3 ==========")
print("----- Bài tập 3.1 -----")

print("1diem: KHONG HOP LE - khong duoc bat dau bang so")
print("gia-tri: KHONG HOP LE - khong duoc dung dau '-'")
print("_tam_thoi: HOP LE")
print("Diem_TB: HOP LE")
print("class: KHONG HOP LE - la tu khoa cua Python")
print("so luong: KHONG HOP LE - khong duoc co khoang trang")
print("MAX_SPEED: HOP LE")
print("2024_data: KHONG HOP LE - khong duoc bat dau bang so")
print("tong$: KHONG HOP LE - ky tu '$' khong hop le")
print("sinhVien1: HOP LE - PEP8 nen dung sinh_vien1")
print("diemTB: HOP LE - PEP8 nen dung diem_tb")


print("\n----- Bài tập 3.2 -----")

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUCLUONG_TOI_THIEU = 5000000

print("Ten:", ten)
print("Diem Toan:", diem_toan)
print("Diem Van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUCLUONG_TOI_THIEU)



print("\n========== HOẠT ĐỘNG 5 ==========")
print("----- Bài tập 5.1: Toán tử số học -----")

a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)


print("\n----- Bài tập 5.2: Toán tử so sánh và logic -----")

diem = 6.5
tuoi = 20

la_kha = diem >= 6.5 and diem < 8.0
tuoi_chua_du_18_hoac_tren_60 = tuoi < 18 or tuoi > 60

print("Diem co dat loai Kha khong?", la_kha)
print("Tuoi chua du 18 hoac tren 60?",
      tuoi_chua_du_18_hoac_tren_60)
print("Phu dinh dieu kien Kha:", not la_kha)


print("\n----- Bài tập 5.3: Toán tử gán -----")

x = 10

x += 5
print("Sau += 5:", x)

x -= 3
print("Sau -= 3:", x)

x *= 2
print("Sau *= 2:", x)

x /= 4
print("Sau /= 4:", x)

x //= 4
print("Sau //= 4:", x)

x **= 2
print("Sau **= 2:", x)


print("\n----- Bài tập 5.3: Toán tử in -----")

danh_sach = [1, 2, 3, "python"]

print("3 co trong danh sach khong?", 3 in danh_sach)


print("\n----- Bài tập 5.3: Toán tử is -----")

danh_sach_1 = [1, 2, 3, "python"]
danh_sach_2 = danh_sach_1

print("Hai bien co cung tham chieu khong?",
      danh_sach_1 is danh_sach_2)


print("\n----- Bài tập 5.4: Độ ưu tiên toán tử -----")

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)




print("\n========== HOẠT ĐỘNG 6 ==========")
print("----- Bài tập 6.1: Dynamic Typing -----")

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))


print("\n----- Bài tập 6.2: Mini bài toán tổng hợp -----")

ho_ten = "Nguyen Van A"

diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi:", la_gioi)
print("Dat loai Kha:", la_kha)
print("Dat loai Trung binh:", la_trung_binh)
print("Dat loai Yeu:", la_yeu)