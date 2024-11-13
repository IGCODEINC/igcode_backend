import os
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# Configuração do logging
logging.basicConfig(
    level=logging.WARNING,  # Ajuste o nível para WARNING para reduzir logs
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log"),
    ],
)

load_dotenv()

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_PARAMS = os.getenv("MONGO_PARAMS")

MONGO_URI = (
    f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_CLUSTER}/{MONGO_DB}?{MONGO_PARAMS}"
)

def get_database():
    try:
        logging.debug("Tentando conectar ao MongoDB...")  # Alterado para DEBUG, vai aparecer apenas no log detalhado
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        db = client[MONGO_DB]
        client.admin.command("ping")
        logging.info(f"Conexão bem-sucedida ao banco de dados {MONGO_DB}")
        return db
    except ServerSelectionTimeoutError as e:
        logging.error(f"Erro na conexão ao MongoDB: {e}")
        return None
