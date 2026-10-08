from db import get_collection


def run(collection):
    print("\n1. find_one() đầu tiên:")
    print(collection.find_one())
    print("\n2. find_one() theo student_id=SV002:")
    print(collection.find_one({"student_id": "SV002"}))
    print("\n3. find() tất cả:")
    for doc in collection.find():
        print(doc)
    print("\n4. Projection name, age:")
    for doc in collection.find({}, {"_id": 0, "name": 1, "age": 1}):
        print(doc)
    print("\n5. Projection loại age:")
    for doc in collection.find({}, {"age": 0}):
        print(doc)
    print("\n6. Kiểu dữ liệu trả về:")
    print(type(collection.find_one()))
    print(type(collection.find()))


if __name__ == "__main__":
    client, collection = get_collection()
    try:
        run(collection)
    finally:
        client.close()
