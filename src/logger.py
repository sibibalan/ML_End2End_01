import logging
import os
from datetime import datetime

# name of the log file:datetime as name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# path of the log_file
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

#  create the "logs" directory
os.makedirs(logs_path,exist_ok=True)

# the complete path to the log file.
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# creates and writes the log file inside the
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = '[ %(asctime)s ] %(lineno)d %(name)s - %(name)s - %(levelname)s -%(message)s',
    level=logging.INFO
)

# if __name__ == "__main__":
#     logging.info("Logging has started")

