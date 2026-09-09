import math


print("--- Bài 3.1 ---")
so_nguyen = 15
so_thuc = 4.2
so_phuc = 3 + 4j

print(type(so_nguyen), type(so_thuc), type(so_phuc))
print(float(so_nguyen))  
print(int(so_thuc))      


print("\n--- Bài 3.2 ---")
a = -7
b = 2.6789
c, d = 17, 5

print(abs(a))           
print(round(b))         
print(round(b, 2))      
print(pow(c, 2))        
print(divmod(c, d))    


print("\n--- Bài 3.3 ---")
a, b, c = 1, -3, 2
delta = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")


print("\n--- Bài 4.1 ---")
cau = "Lap trinh Python rat thu vi"

print(cau[0])         
print(cau[-1])        
print(cau[4:10])      
print(cau[:8])        
print(cau[11:])       
print(cau[::-1])     


is_palindrome = cau == cau[::-1]
print(f"Chuoi '{cau}' co phai la Palindrome khong? {is_palindrome}")


print("\n--- Bài 4.2 ---")
ten = "Nam"
ten_moi = "T" + ten[1:]
print(ten_moi)


print("\n--- Bài 4.3 ---")
cau_xuly = "  Toi dang HOC Python rat vui  "

print(cau_xuly.strip())                             
print(cau_xuly.strip().upper())                     
print(cau_xuly.strip().lower())                     
print(cau_xuly.strip().replace("HOC", "hoc"))       
print(cau_xuly.strip().split())                     
print(len(cau_xuly.strip().split()))                
print(cau_xuly.count("o"))                          
print(cau_xuly.find("Python"))                      
print(cau_xuly.strip().startswith("Toi"))           
print(cau_xuly.strip().endswith("vui"))             
print("-".join(["Python", "that", "thu", "vi"]))     


print("\n--- Bài 4.4 ---")
ho_ten_tho = "   nguyễn    văn   an  "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print(f"Ho ten sau chuan hoa: '{ho_ten_sach}'")