# - * - coding: UTF - 8 - * -
import logging


def log_handler(logger):
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("analyzer.log")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s: %(lineno)d - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
