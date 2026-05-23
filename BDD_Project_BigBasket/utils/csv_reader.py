import csv


class CSVReader:

    @staticmethod
    def get_test_data(path):

        rows = []

        with open(path, newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                rows.append(row)

        return rows