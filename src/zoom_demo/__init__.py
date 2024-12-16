import logging.config
from dotenv import load_dotenv
import concurrent_log_handler  # noqa: F401

load_dotenv(verbose=True)
logging.config.fileConfig("./log.conf", disable_existing_loggers=False)
