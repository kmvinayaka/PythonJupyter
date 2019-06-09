# logging_example.py

import logging
from logging.handlers import TimedRotatingFileHandler
# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file1.log')
#f_handler =  TimedRotatingFileHandler("file.log",when="m",interval=1,backupCount=2)
#f_handler = RotatingFileHandler("file.log", maxBytes=20,backupCount=5)
c_handler.setLevel(logging.CRITICAL)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(lineno)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

#tim


logger.warning('This is a warning')
logger.error('This is an error')
