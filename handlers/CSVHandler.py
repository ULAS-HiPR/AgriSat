import os
import csv

class CSVHandler:
    """A simple CSV file handler."""

    def __init__(self, filename, headers):
        """
        Initialize CSVHandler with filename and headers.

        Args:
            filename (str): Name of the CSV file.
            headers (list of str): List of header names.
        """
        self.filename = filename
        self.path = os.path.join("records", filename + ".csv")
        self.headers = headers

        # Create CSV file with headers if it doesn't exist
        if not os.path.exists(self.path):
            self._write_headers()

    def _write_headers(self):
        """Write headers to the CSV file."""
        with open(self.path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)

    def write(self, row):
        """
        Write a row of data to the CSV file.

        Args:
            row (list of str): List of values for a row.

        Raises:
            ValueError: If the length of row doesn't match the number of headers.
        """
        if len(row) != len(self.headers):
            raise ValueError("Row has incorrect number of elements")
        
        with open(self.path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(row)
