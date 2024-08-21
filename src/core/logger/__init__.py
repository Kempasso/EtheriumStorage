import logging

from src.core.logger.custom_logger import CustomLogger

tx_logger = CustomLogger(name='tx_logger', log_file="tx_logger.log", level=logging.ERROR).get_logger()
db_logger = CustomLogger(name='db_logger', log_file="db_logger.log", level=logging.ERROR).get_logger()