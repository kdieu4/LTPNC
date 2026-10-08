import json
import os
import tkinter
import tkinter as tk
from tkinter import messagebox

FILEPATH = "delivery.json"


def read_json(filepath=FILEPATH):
    if not os.path.exists(filepath):
        return []
    with open(filepath) as json_file:
        data = json.load(json_file)
        return data


def write_json(data, filepath=FILEPATH):
    with open(filepath, 'w', encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


def main():
    root = tk.Tk()
    root.title("Raidobutton")
    root.geometry("450x300")

    saved_data = read_json()

    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Mã đơn hàng: ").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    entry_id = tk.Entry(frame, width=20)
    entry_id.grid(row=0, column=1)

    tkinter.Label(frame, text="Phương thức vận chuyển: ").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    delivery_var = tk.StringVar()
    tk.Radiobutton(frame, text="Giao hàng thường", variable=delivery_var, value="Giao hàng thường").grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=5, pady=5,
                                                                                                         sticky=tk.W)
    tk.Radiobutton(frame, text="Giao hàng nhanh", variable=delivery_var, value="Giao hàng nhanh").grid(row=2, column=1,
                                                                                                       padx=5, pady=5,
                                                                                                       sticky=tk.W)

    def handel_submit():
        order_id = entry_id.get().strip()
        delivery_method = delivery_var.get().strip()

        # Kiểm tra nhập liệu trống
        if not order_id:
            messagebox.showerror("Lỗi", "Mã đơn hàng không được để trống!")
            return
        if not delivery_method:
            messagebox.showerror("Lỗi", "Vui lòng chọn phương thức vận chuyển!")
            return

        for item in saved_data:
            if item.get("id") == order_id:
                messagebox.showerror("Lỗi", "Đơn hàng đã tồn tại!")
                return
        new_order = {
            "id": order_id,
            "delivery": delivery_method
        }
        saved_data.append(new_order)

        write_json(saved_data)

        messagebox.showinfo("Thành công", "Lưu đơn hàng thành công!")

        # Reset lại giao diện hoặc làm sạch ô nhập
        entry_id.delete(0, tk.END)
        delivery_var.set("")

    tk.Button(root, text="Submit", command=handel_submit, width=20).pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
