import csv
from datetime import datetime
import logging

logging.basicConfig(filename='errors.log')

with open('transactions.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    header = ['CandidateName', 'PeriodBeginning', 'PeriodEnding', 'TransactionID', 'TransactionType',
              'TransactionAmount']

    with open('t_apdorotas.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(header)

        for line in csv_reader:
            if line[1] != 'COH':
                continue

            try:
                pb = datetime.strptime(line[35], '%m/%d/%Y').strftime("%Y-%m-%d")
            except ValueError:
                logging.error("PeriodBeginning has wrong date format")

            try:
                pe = datetime.strptime(line[36], '%m/%d/%Y').strftime("%Y-%m-%d")
            except ValueError:
                logging.error("PeriodEnding has wrong date format")

            csv_writer.writerow((line[6] + " " + line[7], pb, pe, line[44], line[48], line[64]))