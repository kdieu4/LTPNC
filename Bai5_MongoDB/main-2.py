import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")


# print(client.list_database_names())

my_db = client["mydatabase"]
my_col = my_db["students"]

print(my_db.list_collection_names())

col_list = my_db.list_collection_names()
if "students" in col_list:
    print("The collection exists")

my_dict = {"name": "Nguyen Van A", "age": 20, "gender": "Nam"}

x = my_col.insert_one(my_dict)
print(my_db.list_collection_names())

mylist = [
    {"name": "Nguyễn Văn An", "age": 25, "gender": "Nam"},
    {"name": "Trần Thị Hồng", "age": 22, "gender": "Nữ"},
    {"name": "Phạm Minh Đức", "age": 30, "gender": "Nam"},
    {"name": "Lê Văn Sơn", "age": 27, "gender": "Nam"},
    {"name": "Hoàng Thu Hoa", "age": 24, "gender": "Nữ"},
]

x = my_col.insert_many(mylist)
print(x.inserted_ids)
