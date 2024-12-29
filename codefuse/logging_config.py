import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

def configure_logging(log_level: str = "INFO", log_to_file: Optional[str] = None):
    """
    Configures the logging settings for the application.

    Args:
        log_level (str): The logging level as a string (e.g., 'DEBUG', 'INFO').
        log_to_file (Optional[str]): If provided, logs will also be written to the specified file.
    """
    # Convert log level string to numeric level
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Create a root logger
    logger = logging.getLogger()
    logger.setLevel(numeric_level)

    # Define log message format
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(numeric_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler with rotation (if log_to_file is specified)
    if log_to_file:
        file_handler = RotatingFileHandler(
            log_to_file, maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
        )
        file_handler.setLevel(numeric_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)