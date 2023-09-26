from loguru import logger
from settings import RETRY_COUNT
from utils.sleeping import sleep


def retry(func):
    def wrapper(*args, **kwargs):
        retries = 0
        while retries <= RETRY_COUNT:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"Error | {e}")
                sleep(10, 20)
                retries += 1
    return wrapper
