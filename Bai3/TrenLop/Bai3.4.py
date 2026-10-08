import os
import tkinter as tk
os.system('clear')

def show_selection(drink_var, milk_var, sugar_var, size_var, result_label):
    seleted_drink = drink_var.get()
    selected_extras = []
    
    if milk_var:
        selected_extras.append('Sữa')
    if sugar_var:
        selected_extras.append('Đường')
        
    selected_size = size_var.get()
    
    extras = ",".join(selected_extras) if selected_extras else "Không có"
    
    result_label.config(text = f"Bạn đã chọn: {seleted_drink}\nSize: {selected_size}\nThêm: {extras}")
    
def main():
    root = tk.Tk()
    root.title("Sử dụng Entry và Text")
    # root.geometry("300x150")
    
    drink_var = tk.StringVar(value="Cà phê")
    tk.Label(root, text="Chọn loại đồ uống").pack()
    tk.Radiobutton(root, text="Cà phê", variable=drink_var, value="Cà phê").pack()
    tk.Radiobutton(root, text="Trà", variable=drink_var, value="Trà").pack()
    tk.Radiobutton(root, text="Nước ngọt", variable=drink_var, value="Nước ngọt").pack()
    
    milk_var = tk.BooleanVar()
    sugar_var = tk.BooleanVar()
    
    tk.Label(root, text="Chọn thêm: ").pack()
    tk.Checkbutton(root, text="Sữa", variable=milk_var).pack()
    tk.Checkbutton(root, text="Đường", variable=sugar_var).pack()
    
    size_var = tk.StringVar(value = "Nhỏ")
    
    sizes = ["Nhỏ", "Trung bình", "Lớn"]
    tk.Label(root, text="Chọn size: ").pack()
    tk.OptionMenu(root, size_var, *sizes).pack()
    
    # tk.Button(root, text="Xác nhận", command=lambda: show_selection(drink_var, milk_var, sugar_var, size_var, result_label)).pack(pady=10)
    
    result_label = tk.Label(root, text="")
    result_label.pack()
    
    tk.Button(root, text="Xác nhận", command=lambda: show_selection(drink_var, milk_var, sugar_var, size_var, result_label)).pack(pady=10)
    
    root.mainloop()
    

if __name__ == '__main__':
    main()