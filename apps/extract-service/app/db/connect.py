import motor.motor_asyncio 
from os import environ
from dotenv import load_dotenv


load_dotenv(dotenv_path="./../.env")

URI = environ.get("MONGO_URL")

print(URI)
client = motor.motor_asyncio.AsyncIOMotorClient(URI)
print('Connected to MongoDB...')

db = client.test
User_collection  = db.get_collection(name="users")
Email_collection = db.get_collection(name="emails") 



    
