import os
import tkinter as tk
os.system('clear')

data = []
def add_to_text(notice_label, entry, text_widget):
    notice_label.config(text="")
    input_text = entry.get().strip()
    if not input_text:
        notice_label.config(text="Cần nhập nội dung!")
    elif input_text in data:
        notice_label.config(text="Dữ liệu đã tồn tại!")
    else:
        data.append(input_text)
        text_widget.insert(tk.END, input_text + "\n")
        entry.delete(0, tk.END)    
    
def clear_text(text_widget):
    data.clear()
    text_widget.delete('1.0', tk.END)
    
    
def main():
    print("Start System...")
    window = tk.Tk()
    window.title("Sử dụng Entry và Text")
    # window.geometry("300x150")
    
    entry = tk.Entry(window, width=20)
    entry.pack(pady=5)
    
    text_widget = tk.Text(window, height=5, width=20)
    text_widget.pack()
    
    notice_label = tk.Label(window, text="")
    notice_label.pack()
    
    tk.Button(window, text="Thêm", command=lambda: add_to_text(notice_label, entry, text_widget), width=20).pack()
    tk.Button(window, text="Xóa", command=lambda: clear_text(text_widget), width=20).pack()
    
    window.mainloop()
    

if __name__ == '__main__':
    main()