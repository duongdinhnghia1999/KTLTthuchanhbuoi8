from tkinter import *

tk = Tk()
tk.title("THÔNG TIN SINH VIÊN")

lbFullName = Label(tk, text = "Họ Và Tên: Dương Đình Nghĩa", font=("Times New Roman", 14), fg= "red").pack()
lbNgaySinh = Label(tk, text = "Ngày Sinh: 26/08/1999", font=("Times New Roman", 14), fg= "blue")
lbNgaySinh.pack()
lbMSSV = Label(tk, text = "MSSV: 1755252021600008", font=("Times New Roman", 14), fg= "red")
lbMSSV.pack()
lbNganhHoc = Label(tk, text="Ngành Học: Kỹ thuật ĐK&TĐH", font=("Times New ROman", 14), fg= "blue")
lbNganhHoc.pack()

tk.mainloop()