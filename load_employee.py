import json
import os
from loguru import logger
def load_employee(file):
    if os.path.exists(file):
        with open(file,"r") as f:
            data=json.load(f)
            logger.info(f"Successfully loaded data from {file}")
            return data
    else:
        return []


        

