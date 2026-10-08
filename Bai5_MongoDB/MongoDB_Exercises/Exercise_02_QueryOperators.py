from db import get_collection


def show(collection, title, query):
    print(f"\n{title}: {query}")
    found = False
    for doc in collection.find(query, {"_id": 0}):
        found = True
        print(doc)
    if not found:
        print("Không tìm thấy sinh viên nào khớp điều kiện")


def run(collection):
    show(collection, "Tuổi = 22", {"age": 22})
    show(collection, "Tuổi > 25", {"age": {"$gt": 25}})
    show(collection, "Tuổi > 20", {"age": {"$gt": 20}})
    show(collection, "Tuổi thuộc [22,25,30]", {"age": {"$in": [22, 25, 30]}})
    show(
        collection,
        "Tên chứa An (không phân biệt hoa/thường)",
        {"name": {"$regex": "An", "$options": "i"}},
    )
    show(collection, "Nam và tuổi > 20", {"gender": "Nam", "age": {"$gt": 20}})
    show(
        collection,
        "Nam và (tuổi 25 hoặc 30)",
        {"gender": "Nam", "$or": [{"age": 25}, {"age": 30}]},
    )
    show(
        collection, "Kỹ năng Python hoặc Java", {"skills": {"$in": ["Python", "Java"]}}
    )


if __name__ == "__main__":
    client, collection = get_collection()
    try:
        run(collection)
    finally:
        client.close()
