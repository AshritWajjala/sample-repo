import sys
from src.logger import logging


class CustomException(Exception):
    def __init__(self, error_message, error_detail=sys):
        """
        :param error_message: String message describing the error
        :param error_detail: The sys module to extract traceback (defaults to sys)
        """
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(
            error_message, error_detail
        )

    @staticmethod
    def get_detailed_error_message(error, error_detail: sys):
        # Extracting the traceback object
        _, _, exc_tb = error_detail.exc_info()

        # If there is no active exception, we can't extract details
        if exc_tb is not None:
            file_name = exc_tb.tb_frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return (
                "\n======================================================================================"
                f"\nError occurred in script: [{file_name}]"
                f"\nLine number: [{line_number}] "
                f"\nError Message: [{str(error)}]"
                "\n======================================================================================"
            )
        return str(error)

    def __str__(self):
        return self.error_message
