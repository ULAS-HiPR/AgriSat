import os
import unittest
from handlers.CSVHandler import CSVHandler


class TestCSVHandler(unittest.TestCase):
    def setUp(self):
        self.filename = "test_csv"
        self.headers = ["Name", "Age", "Location"]
        self.handler = CSVHandler(self.filename, self.headers)

        if not os.path.exists("records"):
            os.makedirs("records")

    def tearDown(self):
        # Clean up after tests by removing the CSV file
        path = "records/" + self.filename + ".csv"
        if os.path.exists(path):
            os.remove(path)

    def test_initialization(self):
        # Test if the CSV file is created with correct headers
        path = "records/" + self.filename + ".csv"
        self.assertTrue(os.path.exists(path))

        with open(path, "r") as f:
            header_line = f.readline().strip()
            self.assertEqual(header_line, ",".join(self.headers))

    def test_write(self):
        # Test if rows are correctly appended to the CSV file
        row = ["John", "30", "New York"]
        self.handler.write(row)

        path = "records/" + self.filename + ".csv"
        with open(path, "r") as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 2)  # First line is header, second line is data
            self.assertEqual(lines[1].strip(), ",".join(row))

    def test_write_incorrect_row(self):
        # Test if ValueError is raised when row has incorrect number of elements
        incorrect_row = ["John", "30"]
        with self.assertRaises(ValueError):
            self.handler.write(incorrect_row)
