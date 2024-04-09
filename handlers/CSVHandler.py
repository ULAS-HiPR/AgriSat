class CSVHandler:
    def __init__(self, filename, headers):
        self.filename = filename
        self.path = "records/" + filename + ".csv"
        self.headers = headers

        with open(self.path, "w") as f:
            f.write(",".join(headers) + "\n")

    def write(self, row):
        if len(row) != len(self.headers):
            raise ValueError("Row has incorrect number of elements")
        else:
            with open(self.path, "a") as f:
                f.write(",".join(row) + "\n")
