import logging
import os


class CustomLogger:
    def __init__(self, name: str, log_file: str, log_dir: str = "logs", level: int = logging.INFO):
        """
        :param name: Logger name
        :param log_file: Filename
        :param log_dir: Logs directory
        :param level: Loglevel
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_path = os.path.join(log_dir, log_file)

        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger
