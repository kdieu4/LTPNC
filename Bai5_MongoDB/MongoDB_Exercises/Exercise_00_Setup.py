from db import get_collection
from data import STUDENTS


def setup_students():
    client, collection = get_collection()
    try:
        collection.drop()  # Chỉ dùng trên collection demo
        collection.create_index("student_id", unique=True)
        result = collection.insert_many(STUDENTS)
        print(f"Đã khởi tạo {len(result.inserted_ids)} sinh viên mẫu")
    finally:
        client.close()


if __name__ == "__main__":
    setup_students()
