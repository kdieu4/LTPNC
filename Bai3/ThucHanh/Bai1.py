import os
import tkinter as tk
os.system('clear')

def handle_login(entry_username, entry_password, label_result):
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    
    if username == "" or password == "":
        label_result.config(text="Tên đăng nhập hoặc mật khẩu không được để trống!")
    elif username != "admin" or password != "password123":
        label_result.config(text="Sai tên đăng nhập hoặc mật khẩu!")
    else:
        label_result.config(text="Đăng nhập thành công!")

def main():
    root = tk.Tk()
    root.title("Đăng nhập")
    root.geometry("350x250")
    
    form_frame = tk.Frame(root)
    form_frame.pack(pady=30)
    
    tk.Label(form_frame, text="Tên đăng nhập").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_username = tk.Entry(form_frame)
    entry_username.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(form_frame, text="Mật khẩu").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_password = tk.Entry(form_frame, show="*")
    entry_password.grid(row=1, column=1, padx=5, pady=5)
    
    label_result = tk.Label(root, text="")
    label_result.pack(pady=10)
    
    tk.Button(root, text="Đăng nhập", command=lambda : handle_login(entry_username, entry_password, label_result), width=20).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()