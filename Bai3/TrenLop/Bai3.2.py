import os
import tkinter as tk
os.system('clear')


def update_date(label, button):
    label.config(text = "Hôm nay là ngày 03/10/2026")
    button.config(state = "disabled")

def main():
    window = tk.Tk()
    window.title("Cập nhật ngày tháng")
    window.geometry("300x150")
    
    label = tk.Label(
        text="Hôm nay là ngày 10/10/2024"
    )
    label.pack()
    
    button = tk.Button(
        text="Cập nhật",
        command=lambda: update_date(label, button)
    )
    button.pack(pady=10)
    
    window.mainloop()
    

if __name__ == '__main__':
    main()