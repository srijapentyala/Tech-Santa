import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "hackathon_db"

class Database:
    client: MongoClient = None

    def connect(self):
        try:
            # Configure connection based on environment
            client_kwargs = {}
            # Check if using MongoDB Atlas or similar requiring specific TLS settings
            if "mongodb+srv" in MONGO_URI:
                client_kwargs['tlsCAFile'] = certifi.where()
                client_kwargs['tlsAllowInvalidCertificates'] = True
            
            self.client = MongoClient(MONGO_URI, **client_kwargs)
            
            # Force a connection check immediately
            self.client.admin.command('ping')
            print("✅ Connected to MongoDB successfully!")
        except Exception as e:
            print(f"❌ MongoDB Connection Failed: {e}")

    def get_db(self):
        if self.client:
            return self.client[DB_NAME]
        return None

    def close(self):
        if self.client:
            self.client.close()

db = Database()
