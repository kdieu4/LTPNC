import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()
uri = os.getenv("MONGODB_URI")
client = MongoClient(uri, server_api=ServerApi("1"))

my_db = client["mydatabase"]
my_col = my_db["students"]
mylist = [
    {"name": "Nguyễn Văn An", "age": 25, "gender": "Nam"},
    {"name": "Trần Thị Hồng", "age": 22, "gender": "Nữ"},
    {"name": "Phạm Minh Đức", "age": 30, "gender": "Nam"},
    {"name": "Lê Văn Sơn", "age": 27, "gender": "Nam"},
    {"name": "Hoàng Thu Hoa", "age": 24, "gender": "Nữ"},
]

x = my_col.insert_many(mylist)
print(uri)
print(x.inserted_ids)

x = my_col.find_one()
print(x)
