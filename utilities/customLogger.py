import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # path = (os.path.abspath(os.getcwd())+"\\logs\\automation.log")
        path = os.path.join(os.path.abspath(os.getcwd()), 'logs', 'automation.log')

        logger = logging.getLogger(name=__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y  %I:%M:%S %p')
        file_handler = logging.FileHandler(path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger