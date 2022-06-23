import os
import glob
import csv
from openpyxl import Workbook
import pandas as pd
def convert_to_excel(file_name):
    wb = Workbook()
    ws = wb.active
    with open(file_name, 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    pure_file_name = file_name[16:-4]
    print(pure_file_name)
    wb.save(f'data_excel/{pure_file_name}.xlsx')

def remove_all_excel_files():
    for csvfile in glob.glob(os.path.join('data_excel', '*.xlsx')):
        os.system(f'rm {csvfile}')

def convert_all_to_excel_files():
    for csvfile in glob.glob(os.path.join('output_data_csv', '*.csv')):
        convert_to_excel(csvfile)

def rank_student_by_total_score():
    for csvfile in glob.glob(os.path.join('data_csv', '*.csv')):
        pure_file_name = csvfile[9:-4]
        new_csv_file_path = f"output_data_csv/{pure_file_name}.csv"
        df = pd.read_csv(csvfile)
        df["Tổng"].replace({"Vắng": "0"}, inplace=True)
        df['Tổng'] = df['Tổng'].astype(float) 
        df = df.sort_values(by=['Tổng'], ascending=False)
        df.insert(10, 'Xếp hạng', range(1,len(df)+1))
        # print(df.to_string()) 
        df.to_csv(new_csv_file_path, sep=',',index=False)
rank_student_by_total_score()
remove_all_excel_files()
convert_all_to_excel_files()