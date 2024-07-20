import logging
import os
class LogGen:
   @staticmethod
   def loggen():
       path = (os.path.abspath(
       os.getcwd()) + "\\logs\\automation.log")
       logger = logging.getLogger(__name__)  # Create or get a logger with the name of the current module.
       logger.setLevel(logging.DEBUG)
       formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                     datefmt='%m/%d/%Y %I:%M:%S %p')
       file_handler = logging.FileHandler(path)  # Create a file handler to write log messages.
       file_handler.setFormatter(formatter)  # Set the formatter for the file handler.
       logger.addHandler(file_handler)  # Add the file handler to the logger.
       return logger  # Return the configured logger.