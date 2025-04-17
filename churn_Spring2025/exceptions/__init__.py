import sys

def error_message_detail(error, error_detail: sys):
    """
    returns the filename, line number, and error message information as a
    string 
    """
    _,_, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occured in python script [{0}] at line [{1}]: " \
        "{2}".format(file_name, exc_tb.tb_lineno, str(error))
    
    return error_message
    
class custom_exception(Exception):
    def __init__(self, error_message, error_detail):
        """
        Initialize the custom exception with:
        - error_message: the original error or string description
        - error_detail: usually 'sys', used to extract traceback info
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail
                                                  =error_detail)
    def __str__(self):
        return self.error_message