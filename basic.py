import logging


LOGFILE = "main.log"

logger = logging.getLogger("basic")

# set logging level : INFO, DEBUG, WARNING or ERROR
logger.setLevel(logging.DEBUG)

# Create FileHandler with log file name
file_handler = logging.FileHandler(LOGFILE)

# This is the format in which logs will be displayed in log file
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# assign the formatter to file_handler object
file_handler.setFormatter(formatter)

# add the handler to logger
logger.addHandler(file_handler)


# Code to test
a = [1,2,3,4]

logger.debug("The value of a: {}".format(a))

for i, j in enumerate(a, start=1):
	logger.debug("value {}: {}".format(i, j))