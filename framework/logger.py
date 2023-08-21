import logging

# Configure appium_logger
appium_logger = logging.getLogger("appium_logger")
appium_logger.setLevel(logging.INFO)
appium_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
appium_file_handler = logging.FileHandler("appium.log")
appium_file_handler.setFormatter(appium_formatter)
appium_logger.addHandler(appium_file_handler)

# Configure tests_logger
tests_logger = logging.getLogger("tests_logger")
tests_logger.setLevel(logging.INFO)
tests_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
tests_file_handler = logging.FileHandler("tests.log")
tests_file_handler.setFormatter(tests_formatter)
tests_logger.addHandler(tests_file_handler)