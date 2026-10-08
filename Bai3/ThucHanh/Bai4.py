import os
import tkinter as tk

os.system('clear')


def handle_count_word(text, label_result, filename="notes.txt"):
    if text.get("1.0", tk.END).strip() == "":
        label_result.config(text="Vui lòng nhập văn bản")
        return
    res = len(text.get("1.0", tk.END).strip().split())
    label_result.config(text=f"Kết quả: có {res} từ trong văn bản")

def main():
    root = tk.Tk()
    root.title("Ứng dụng ghi chú")
    root.geometry("800x500")

    tk.Label(root, text="Viết ghi chú: ").pack(pady=10)
    text = tk.Text(root, height=10, width=50)
    text.pack(pady=10)

    tk.Label(root, text="Kết quả: ")
    label_result = tk.Label(root, text="")

    tk.Button(root, text="Đếm từ", command=lambda: handle_count_word(text, label_result), width=20).pack(pady=10)

    label_result.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
