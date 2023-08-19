import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_messages = f"Error Occured in Python Script name {file_name} line number {line_number} error message {str(error)} "

    return error_messages

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_messsage = error_message_detail(error_message, error_detail)
    def __str__(self):
        return self.error_messsage




# if __name__ == "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         raise CustomException(e,sys)
#         logging.info("division by zero")


