import os
import tkinter as tk

os.system('clear')


def handle_save(text, label_result, filename="notes.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", "end-1c"))
    label_result.config(text="Lưu file thành công")


def handle_delete(text, label_result):
    text.delete("1.0", tk.END)
    label_result.config(text="Xóa thành công")


def main():
    root = tk.Tk()
    root.title("Ứng dụng ghi chú")
    root.geometry("350x500")

    tk.Label(root, text="Viết ghi chú: ").pack(pady=10)
    text = tk.Text(root, height=10, width=20)
    text.pack(pady=10)

    tk.Label(root, text="Kết quả: ").pack(pady=10)
    label_result = tk.Label(root, text="")
    label_result.pack(pady=10)

    tk.Button(root, text="Lưu", command=lambda: handle_save(text, label_result), width=20).pack(pady=10)
    tk.Button(root, text="Xóa", command=lambda: handle_delete(text, label_result), width=20).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
