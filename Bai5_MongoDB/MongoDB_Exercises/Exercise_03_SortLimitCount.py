from db import get_collection


def run(collection):
    print("\nSắp xếp tuổi tăng dần:")
    for doc in collection.find({}, {"_id": 0}).sort("age", 1):
        print(doc)
    print("\nLấy 2 sinh viên đầu tiên:")
    for doc in collection.find({}, {"_id": 0}).limit(2):
        print(doc)
    print("\nTop 5 tuổi cao nhất:")
    for doc in collection.find({}, {"_id": 0}).sort("age", -1).limit(5):
        print(doc)
    print(f"\nSố sinh viên 30 tuổi: {collection.count_documents({'age': 30})}")


if __name__ == "__main__":
    client, collection = get_collection()
    try:
        run(collection)
    finally:
        client.close()
