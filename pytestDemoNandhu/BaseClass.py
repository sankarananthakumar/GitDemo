import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggername= inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler('logfile.log')
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(format)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        logger.debug("A debug statement is executed")
        logger.info("Information statement")
        logger.warning("Something is in warning mode")
        logger.error("A major error has happened")
        logger.critical("Critical Issue")
        return logger
