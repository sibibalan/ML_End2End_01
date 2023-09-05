import logging
import os
from datetime import datetime

# name of the log file:datetime as name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# path of the log_file
# logs_path = os.path.join(os.path.dirname(os.getcwd()),"logs",LOG_FILE)
main_dir_path = 'D:\\ML_Projects'
logs_path = os.path.join(main_dir_path,"logs",LOG_FILE)
# print(__name__)
# print(__file__)


#  create the "logs" directory
os.makedirs(logs_path, exist_ok=True)

# the complete path to the log file.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
# print(LOG_FILE_PATH)

# creates and writes the log file inside the
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = '[ %(asctime)s ] %(lineno)d %(name)s - %(name)s - %(levelname)s -%(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")

