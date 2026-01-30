import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y&%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[  %(asctime)s  ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# import logging
# import os
# import sys
# from datetime import datetime


# class ColoredFormatter(logging.Formatter):
#     """Custom Formatter to add colors based on the log level"""

#     # ANSI escape sequences for colors
#     grey = "\x1b[38;20m"
#     yellow = "\x1b[33;20m"
#     red = "\x1b[31;20m"
#     bold_red = "\x1b[31;1m"
#     cyan = "\x1b[36;20m"
#     reset = "\x1b[0m"

#     # Format string
#     fmt = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s"

#     FORMATS = {
#         logging.DEBUG: grey + fmt + reset,
#         logging.INFO: cyan + fmt + reset,
#         logging.WARNING: yellow + fmt + reset,
#         logging.ERROR: red + fmt + reset,
#         logging.CRITICAL: bold_red + fmt + reset,
#     }

#     def format(self, record):
#         log_fmt = self.FORMATS.get(record.levelno)
#         formatter = logging.Formatter(log_fmt)
#         return formatter.format(record)


# def setup_logger():
#     # File setup
#     log_file = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
#     logs_dir = os.path.join(os.getcwd(), "logs")
#     os.makedirs(logs_dir, exist_ok=True)
#     log_file_path = os.path.join(logs_dir, log_file)

#     # 1. Create a Logger
#     logger = logging.getLogger("MyProject")
#     logger.setLevel(logging.INFO)

#     # 2. Console Handler (With Colors)
#     stdout_handler = logging.StreamHandler(sys.stdout)
#     stdout_handler.setFormatter(ColoredFormatter())

#     # 3. File Handler (Clean text, no colors)
#     file_handler = logging.FileHandler(log_file_path)
#     file_handler.setFormatter(
#         logging.Formatter("[ %(asctime)s ] %(levelname)s - %(message)s")
#     )

#     # Add handlers to logger
#     logger.addHandler(stdout_handler)
#     logger.addHandler(file_handler)

#     return logger


# # Initialize
# logger = setup_logger()
