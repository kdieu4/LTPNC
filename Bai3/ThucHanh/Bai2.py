import os
import tkinter as tk
os.system('clear')

def get_value(entry_soA, entry_soB, label_result):
    val_A = entry_soA.get().strip()
    val_B = entry_soB.get().strip()
        
    if val_A == "" or val_B == "":
        label_result.config(text="Không được để trống!")
        return None, None
    try: 
        soA = float(val_A)
        soB = float(val_B)
        
        return soA, soB
        
    except ValueError:
        label_result.config(text="Lỗi, vui lòng nhập số nguyên hợp lệ!")
        return False
    

def handle_add(entry_soA, entry_soB, label_result):
    soA, soB = get_value(entry_soA, entry_soB, label_result)
    if soA is not None and soB is not None:
        res = soA + soB
        print(res)
        label_result.config(text=f"{soA:.2f} + {soB:.2f} = {res:.2f}")

def handle_subtract(entry_soA, entry_soB, label_result):
    soA, soB = get_value(entry_soA, entry_soB, label_result)
    if soA is not None and soB is not None:
        res = soA - soB
        print(res)
        label_result.config(text=f"{soA:.2f} - {soB:.2f} = {res:.2f}")

def main():
    root = tk.Tk()
    root.title("Tính toán cộng trừ")
    root.geometry("350x300")
    
    form_frame = tk.Frame(root)
    form_frame.pack(pady=30)
    
    tk.Label(form_frame, text="Nhập số A: ").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_soA = tk.Entry(form_frame)
    entry_soA.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(form_frame, text="Nhập số B:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_soB = tk.Entry(form_frame)
    entry_soB.grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(form_frame, text="Kết quả: ").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    label_result = tk.Label(form_frame, text="")
    label_result.grid(row=3, column=1, padx=5, pady=5)
    
    tk.Button(root, text="Cộng", command=lambda : handle_add(entry_soA, entry_soB, label_result), width=20).pack(pady=10)
    tk.Button(root, text="Trừ", command=lambda : handle_subtract(entry_soA, entry_soB, label_result), width=20).pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()