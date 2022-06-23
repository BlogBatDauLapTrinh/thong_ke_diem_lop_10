import os
import glob
import csv
from openpyxl import Workbook

def convert_to_excel(file_name):
    wb = Workbook()
    ws = wb.active
    with open(file_name, 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    pure_file_name = file_name[9:-4]
    print(pure_file_name)
    wb.save(f'data_excel/{pure_file_name}.xlsx')

def remove_all_excel_files():
    for csvfile in glob.glob(os.path.join('data_excel', '*.xlsx')):
        os.system(f'rm {csvfile}')

def convert_all_to_excel_files():
    for csvfile in glob.glob(os.path.join('data_csv', '*.csv')):
        convert_to_excel(csvfile)

remove_all_excel_files()
convert_all_to_excel_files()