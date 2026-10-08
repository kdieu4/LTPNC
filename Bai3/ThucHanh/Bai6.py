import tkinter as tk
import json
import os


def handle_summit(root, read_book_var, listen_to_music_var, travel_var):
    current_data = []
    if read_book_var.get():
        current_data.append("Đọc sách")
    if listen_to_music_var.get():
        current_data.append("Nghe nhạc")
    if travel_var.get():
        current_data.append("Du lịch")

    with open("hobbies.json", "w", encoding="utf-8") as file:
        json.dump(current_data, file, indent=4, ensure_ascii=False)

    root.destroy()
    main()


def exists_data():
    file_path = "hobbies.json"  # Tên file JSON của bạn
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        return []


def main():
    root = tk.Tk()
    root.title("Checkbutton")
    root.geometry("300x300")

    saved_data = exists_data()
    if saved_data:
        res = "\n".join(saved_data)
        tk.Label(root, text=f"Sở thích của bạn là: \n{res}", font=("Arial", 12)).pack(pady=50)

        def reset_data():
            if os.path.exists("hobbies.json"):
                os.remove("hobbies.json")
            root.destroy()
            main()

        tk.Button(root, text="Nhập lại sở thích", command=reset_data).pack(pady=10)
    else:
        read_book_var = tk.BooleanVar()
        listen_to_music_var = tk.BooleanVar()
        travel_var = tk.BooleanVar()
        frame = tk.Frame(root)
        frame.pack(pady=50)

        tk.Label(frame, text="Chọn sở thích").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Checkbutton(frame, text="Đọc sách", variable=read_book_var).grid(row=1, column=0, padx=5, pady=5)
        tk.Checkbutton(frame, text="Nghe nhạc", variable=listen_to_music_var).grid(row=1, column=1, padx=5, pady=5)
        tk.Checkbutton(frame, text="Du lịch", variable=travel_var).grid(row=1, column=2, padx=5, pady=5)

        tk.Button(frame, text="Submit",
                  command=lambda: handle_summit(root, read_book_var, listen_to_music_var, travel_var),
                  padx=5, pady=5).grid(row=2, column=2, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
