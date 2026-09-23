
# HOẠT ĐỘNG 3: VÒNG LẶP FOR – RANGE() & DUYỆT LIST/TUPLE/DICT/STRING


print("=== FOR VỚI RANGE() ===")
for i in range(1, 6):
    print(i)


print("\n=== FOR DUYỆT LIST ===")
diem_so = [8.5, 7.0, 9.2, 6.5]
for diem in diem_so:
    print("Diem:", diem)

print("\n=== FOR DUYỆT TUPLE ===")
toa_do = (3, 5)
for gia_tri in toa_do:
    print(gia_tri)

print("\n=== FOR DUYỆT DICTIONARY ===")
diem_mon = {"Toan": 8.0, "Ly": 7.5}
for mon, diem in diem_mon.items():
    print(mon, "-", diem)

print("\n=== FOR DUYỆT STRING ===")
ten = "Python"
for ky_tu in ten:
    print(ky_tu)

print("\n=== BÀI TẬP VẬN DỤNG - BẢNG CỬU CHƯƠNG ===")
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")



# HOẠT ĐỘNG 4: VÒNG LẶP WHILE

# --- Bài tập 4.1 – Tính giai thừa của n ---[cite: 5]
print("\n=== BÀI TẬP 4.1 ===")
n = 5
giai_thua = 1
i = 1

while i <= n:
    giai_thua = giai_thua * i
    i += 1

print(f"{n}! = {giai_thua}")

# --- Bài tập 4.2 – Tính tổng các chữ số của một số ---[cite: 5]
print("\n=== BÀI TẬP 4.2 ===")
so = 4527
so_tam = so
tong_chu_so = 0

while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10

print(f"Tong cac chu so cua {so} la: {tong_chu_so}")