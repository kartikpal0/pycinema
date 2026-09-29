import logging
import os


def get_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("pycinema")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("logs/pycinema.log")
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)
    return logger
