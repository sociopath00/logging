import logging
from logging.handlers import TimedRotatingFileHandler


LOGFILE = "main.log"

logger = logging.getLogger("dailylogs")

# set logging level : INFO, DEBUG, WARNING or ERROR
logger.setLevel(logging.DEBUG)


# Create TimedRotatingFileHandler with log file name
# It will create a new log file each day at midnight('m' stands for midnight)
handler = TimedRotatingFileHandler(LOGFILE, when="m", interval=1)

# This is the format in which logs will be displayed in log file
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# assign the formatter and suffix to file_handler object
# suffix will be added to each file
handler.setFormatter(formatter)
handler.suffix = "%Y%m%d"


# add the handler to logger
logger.addHandler(handler)