import os
import tkinter as tk

os.system('clear')


def get_value(entry_weight, entry_height, label_result):
    val_weight = entry_weight.get().strip()
    val_height = entry_height.get().strip()

    if val_weight == "" or val_height == "":
        label_result.config(text="Không được để trống!")
        return None, None
    try:
        weight = float(val_weight)
        height = float(val_height)

        return weight, height

    except ValueError:
        label_result.config(text="Lỗi, vui lòng nhập dữ liệu hợp lệ!")
        return False


def handle_compute_bmi(entry_weight, entry_height, label_result):
    weight, height = get_value(entry_weight, entry_height, label_result)
    if weight is not None and height is not None:
        res = weight / (height * height)
        label_result.config(text=f"{res:.2f}")


def main():
    root = tk.Tk()
    root.title("Tính BMI")
    root.geometry("350x300")

    form_frame = tk.Frame(root)
    form_frame.pack(pady=30)

    tk.Label(form_frame, text="Nhập cân nặng (kg): ").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_weight = tk.Entry(form_frame)
    entry_weight.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Nhập chiều cao (m):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_height = tk.Entry(form_frame)
    entry_height.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(form_frame, text="Kết quả: ").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    label_result = tk.Label(form_frame, text="")
    label_result.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(root, text="Tính", command=lambda: handle_compute_bmi(entry_weight, entry_height, label_result),
              width=20).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
