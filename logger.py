import logging

logging.basicConfig(
    filename="urllog.log",
    filemode="w",
    level=logging.INFO,
    format='%(asctime)s\n\n%(message)s\n\n',
)

def log_change(change_description):
    logging.info(f'Website Change Detected:\n{change_description}')
