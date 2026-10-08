from db import get_collection


def level_1(collection):
    print("\nLEVEL 1 - find_one theo student_id")
    student = collection.find_one({"student_id": "SV001"})
    print(
        student
        if student is not None
        else "Không tìm thấy sinh viên nào khớp điều kiện"
    )


def level_2(collection):
    print("\nLEVEL 2 - IT, GPA > 3.0, top 2")
    query = {"major": "IT", "gpa": {"$gt": 3.0}}
    cursor = collection.find(query).sort("gpa", -1).limit(2)
    found = False
    for student in cursor:
        found = True
        print(f"Sinh viên: {student['name']} - Điểm GPA: {student['gpa']}")
    if not found:
        print("Không tìm thấy sinh viên nào khớp điều kiện")


def level_3(collection):
    print("\nLEVEL 3 - $or + $in + Projection")
    query = {
        "$or": [{"major": "IT"}, {"major": "Data"}],
        "skills": {"$in": ["Python", "Java"]},
    }
    projection = {"_id": 0, "name": 1, "skills": 1}
    found = False
    for student in collection.find(query, projection):
        found = True
        print(f"Sinh viên: {student['name']} - Kỹ năng: {', '.join(student['skills'])}")
    if not found:
        print("Không tìm thấy sinh viên nào khớp điều kiện")


def run(collection):
    level_1(collection)
    level_2(collection)
    level_3(collection)


if __name__ == "__main__":
    client, collection = get_collection()
    try:
        run(collection)
    finally:
        client.close()
