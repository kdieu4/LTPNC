import os
import tkinter as tk
os.system('clear')

def show_selection(drink_var, food_var, result_label):
    selected_drink = drink_var.get()
    selected_food = food_var.get()
    result_label.config(text=f"Bạn đã chọn:\nĐồ uống: {selected_drink}\nĐồ ăn: {selected_food}")
    
def main():
    root = tk.Tk()
    root.title("Sử dụng Entry và Text")

    drink_frame = tk.Frame(root, relief="groove", borderwidth=2, padx=10, pady=10)
    drink_frame.pack()
    
    drink_var = tk.StringVar(value="Cà phê")
    tk.Label(drink_frame, text="Đặt đồ uống: ").pack()
    tk.Radiobutton(root, text="Cà phê", variable=drink_var, value="Cà phê").pack()
    tk.Radiobutton(root, text="Trà", variable=drink_var, value="Trà").pack()
    
    food_frame = tk.Frame(root, relief="groove", borderwidth=2, padx=10, pady=10)
    food_frame.pack()
    
    food_var = tk.StringVar(value = "Bánh mỳ")
    tk.Radiobutton(food_frame, text="Bánh mỳ", variable=food_var, value="Bánh mỳ").pack()
    tk.Radiobutton(food_frame, text="Pizza", variable=food_var, value="Pizza").pack()

    confirm_button = tk.Button(root, text="Xác nhận")
    confirm_button.pack()
    
    result_label = tk.Label(root, text="")
    result_label.pack()
    
    confirm_button.config(command=lambda : show_selection(drink_var, food_var, result_label))
    root.mainloop()
    

if __name__ == '__main__':
    main()