import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

_client = MongoClient(
    os.getenv("MONGO_URI"),
    serverSelectionTimeoutMS=5000,
)

def get_db():
    return _client[os.getenv("MONGO_DB")]

def testar_conexao():
    _client.admin.command("ping")
    print("Conectado ao MongoDB!")



testar_conexao()