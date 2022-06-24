import os
import glob
import pandas as pd

def remove_all_excel_files():
    for csvfile in glob.glob(os.path.join('data_excel', '*.xlsx')):
        os.system(f'rm {csvfile}')

def convert_all_csv_files_to_excel():
    for csvfile in glob.glob(os.path.join('data_csv', '*.csv')):
        df = rank_student_by_total_score(csvfile)
        save_file_as_excel(csvfile,df)

def rank_student_by_total_score(csvfile):
    df = pd.read_csv(csvfile)
    df["Tổng"].replace({"Vắng": "0"}, inplace=True)
    df['Tổng'] = df['Tổng'].astype(float) 
    df = df.sort_values(by=['Tổng'], ascending=False)
    df.insert(10, 'Xếp hạng', range(1,len(df)+1))
    return df

def save_file_as_excel(csvfile,df):
    pure_file_name = csvfile[9:-4]
    output_excel_name = f'data_excel/{pure_file_name}.xlsx'
    df.to_excel(output_excel_name, index=None, header=True)

remove_all_excel_files()
convert_all_csv_files_to_excel()