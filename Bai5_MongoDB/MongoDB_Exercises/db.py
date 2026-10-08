import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()


def get_collection():
    uri = os.getenv("MONGODB_URI")
    if not uri:
        raise ValueError(
            "Thiếu MONGODB_URI. Sao chép .env.example thành .env và điền URI."
        )
    client = MongoClient(uri, server_api=ServerApi("1"), serverSelectionTimeoutMS=10000)
    client.admin.command("ping")
    return client, client["mydatabase"]["students"]
