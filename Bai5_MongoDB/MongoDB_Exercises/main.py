"""Chạy các ví dụ truy vấn. Khởi tạo dữ liệu riêng bằng Exercise_00_Setup.py."""
from db import get_collection
from Exercise_01_Find import run as run_find
from Exercise_02_QueryOperators import run as run_operators
from Exercise_03_SortLimitCount import run as run_sort
from Exercise_04_ThreeLevels import run as run_levels

def main():
    client, collection = get_collection()
    try:
        if collection.count_documents({}) == 0:
            print("Collection trống. Chạy: python Exercise_00_Setup.py")
            return
        run_find(collection)
        run_operators(collection)
        run_sort(collection)
        run_levels(collection)
    finally:
        client.close()

if __name__ == "__main__":
    main()
