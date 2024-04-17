import os
import unittest
from handlers.LogHandler import LogHandler
import logging


class TestLogHandler(unittest.TestCase):
    def setUp(self):
        self.log_file = "logs/test.log"

        if not os.path.exists("logs"):
            os.makedirs("logs")

        self.handler = LogHandler(log_file=self.log_file)

    def tearDown(self):
        # Clean up after tests by removing the log file
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_initialization(self):
        self.assertIsNotNone(self.handler)

    def test_log_output(self):
        message = "Test log message"
        self.handler.debug(message)
        self.handler.info(message)
        self.handler.warning(message)
        self.handler.error(message)
        self.handler.critical(message)

        # Verify that log file is created and contains log messages
        self.assertTrue(os.path.exists(self.log_file))
        with open(self.log_file, "r") as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 5)  # 5 log messages were written

    def test_log_levels(self):
        # Test if log messages of different levels are written
        self.handler.debug("Debug message")
        self.handler.info("Info message")
        self.handler.warning("Warning message")
        self.handler.error("Error message")
        self.handler.critical("Critical message")

        log_levels = [
            logging.DEBUG,
            logging.INFO,
            logging.WARNING,
            logging.ERROR,
            logging.CRITICAL,
        ]
        with open(self.log_file, "r") as f:
            lines = f.readlines()
            for level, line in zip(log_levels, lines):
                self.assertIn(logging.getLevelName(level), line)

    def test_log_format(self):
        # Test if log messages are formatted correctly
        message = "Test log message"
        self.handler.info(message)
        with open(self.log_file, "r") as f:
            line = f.readline()
            self.assertRegex(
                line,
                r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} \[INFO\] Test log message",
            )

    def test_handler_setup(self):
        expected_handler_types = [
            logging.handlers.RotatingFileHandler,
            logging.StreamHandler,
        ]
        actual_handler_types = [
            type(handler) for handler in self.handler.logger.handlers
        ]
        for handler_type in expected_handler_types:
            self.assertIn(handler_type, actual_handler_types)
