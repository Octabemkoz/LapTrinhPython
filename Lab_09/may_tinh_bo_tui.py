import tkinter as tk
from tkinter import messagebox


def bam_nut(gia_tri):
    
    bieu_thuc_hien_tai = entry_hien_thi.get()

    if gia_tri == "C":
        
        entry_hien_thi.delete(0, tk.END)
    elif gia_tri == "=":
        try:
         
            ket_qua = eval(bieu_thuc_hien_tai)
            entry_hien_thi.delete(0, tk.END)
            entry_hien_thi.insert(tk.END, str(ket_qua))
        except ZeroDivisionError:
            messagebox.showerror("Lỗi", "Không thể chia cho 0!")
            entry_hien_thi.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
            entry_hien_thi.delete(0, tk.END)
    else:
       
        entry_hien_thi.insert(tk.END, gia_tri)


cua_so = tk.Tk()
cua_so.title("Máy tính bỏ túi")
cua_so.geometry("320x400")
cua_so.resizable(False, False)



entry_hien_thi = tk.Entry(
    cua_so, font=("Arial", 18), justify="right", bd=10, relief=tk.SUNKEN
)
entry_hien_thi.grid(
    row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10, sticky="nsew"
)

danh_sach_nut = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("C", 4, 2),
    ("+", 4, 3),
    ("=", 5, 0),
]

for thong_tin in danh_sach_nut:
    text = thong_tin[0]
    hang = thong_tin[1]
    cot = thong_tin[2]

    if text == "=":
        nut = tk.Button(
            cua_so,
            text=text,
            font=("Arial", 14, "bold"),
            bg="#4CAF50",
            fg="white",
            command=lambda t=text: bam_nut(t),
        )
        nut.grid(
            row=hang, column=cot, columnspan=4, padx=5, pady=5, sticky="nsew"
        )
    else:
        nut = tk.Button(
            cua_so,
            text=text,
            font=("Arial", 14),
            command=lambda t=text: bam_nut(t),
        )
        nut.grid(row=hang, column=cot, padx=5, pady=5, sticky="nsew")

for i in range(4):
    cua_so.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    cua_so.grid_rowconfigure(i, weight=1)

if __name__ == "__main__":
    cua_so.mainloop()