import csv
import datetime
from os import makedirs
from os.path import dirname, abspath, join, exists
from pathlib import Path, PureWindowsPath


class CSV_Logging:
    def __init__(self):
        self.file_name = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")+'.csv'
        self.delimeter = "\n"
        #creating 'myproject/logs' if does not exists
        self.folder = join(dirname(dirname(abspath(__file__))), 'logs')
        if not exists(self.folder):
            makedirs(self.folder)

    def run(self, list_input):
        """writes list to csv"""
        with open(join(self.folder, self.file_name), 'w') as fp:
            writer = csv.writer(fp, delimiter =self.delimeter)
            writer.writerow(list_input)