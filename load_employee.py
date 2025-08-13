from pymongo import AsyncMongoClient
from loguru import logger
from dotenv import load_dotenv,find_dotenv
from validity import*
import os
async def get_next_empId(db):
  counter = await db.counters.find_one_and_update({"_id": "emp_id"}, {"$inc": {"sequence_value": 1}},  
      upsert=True,   # Create the counter if it doesn't exist 
      return_document=True,  ) # Return the updated document        
  return counter["sequence_value"]
async def get_db(db_name="employee_db"):
  try:
    load_dotenv(find_dotenv())
    password=os.environ.get("MongoDB_password")
    connection_string=f"mongodb+srv://durba028:{password}@tuitorial.s0vgcnr.mongodb.net/"
    client = AsyncMongoClient(connection_string)
    db = client[db_name]
    await db.employee.create_index([("emp_id",1)],unique=True)
    logger.info("Connected to MongoDB")
    return db,client
  except Exception as e:
    logger.error(f"Error connecting to MongoDB: {e}")
    return None
