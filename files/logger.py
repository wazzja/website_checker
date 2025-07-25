import logging

logger = logging.getLogger("url_logger")
logger.setLevel(logging.INFO)

logger.propagate = False

file_handler = logging.FileHandler("urllog.log", mode="w")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s\n\n%(message)s\n\n',
                              datefmt='%d-%m-%Y %H:%M:%S'
                              )
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def log_change(change_description):
    logger.info(f'Website Change Detected:\n{change_description}')
