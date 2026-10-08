# MongoDB – Bài thực hành Thành viên 2

Chuyển từ `base_mongodb(4).ipynb` thành các file `.py` theo phong cách bài Exercise: hàm có thể tái sử dụng, ví dụ chạy dưới `if __name__ == "__main__"`.

| File | Nội dung |
| --- | --- |
| `db.py` | Kết nối MongoDB bằng `MONGODB_URI`, kiểm tra ping |
| `data.py` | 5 sinh viên mẫu (giữ nguyên notebook) |
| `Exercise_00_Setup.py` | Reset collection, tạo unique index, insert_many |
| `Exercise_01_Find.py` | find_one, find, Cursor, Projection |
| `Exercise_02_QueryOperators.py` | $gt, $in, regex, AND, OR |
| `Exercise_03_SortLimitCount.py` | sort, limit, count_documents |
| `Exercise_04_ThreeLevels.py` | Demo Dễ – Trung bình – Khó |
| `main.py` | Chạy toàn bộ ví dụ mà không reset dữ liệu |

## Cách chạy trên Ubuntu

```bash
conda activate python-nc
cd MongoDB_Exercises
python -m pip install -r requirements.txt
cp .env.example .env
# Điền URI thật vào .env (không commit file này)
python Exercise_00_Setup.py
python main.py
```

Chạy từng bài bằng `python Exercise_01_Find.py`, ... hoặc `python Exercise_04_ThreeLevels.py`.

**Cảnh báo:** `Exercise_00_Setup.py` sử dụng `collection.drop()` để xóa dữ liệu cũ. Chỉ chạy với collection demo `mydatabase.students`. Nếu Atlas đang lỗi DNS/TLS, cần khắc phục kết nối trước khi chạy.

**Đối chiếu SQL / MongoDB:** `SELECT *` ↔ `find({})`; `WHERE age > 20` ↔ `find({"age": {"$gt": 20}})`; `ORDER BY age DESC LIMIT 5` ↔ `find().sort("age", -1).limit(5)`.
