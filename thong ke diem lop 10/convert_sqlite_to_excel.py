import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('tpk.xlsx')
worksheet = workbook.add_worksheet()
# Pass in the database path, db.s3db or test.sqlite
conn=sqlite3.connect('/home/thanh/Documents/crawl_score/trinh hoai duc/tpk_tvo_thd.db')
c=conn.cursor()
mysel = c.execute("select * from diem_tanphuockhanh")
for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i, j, value)
workbook.close()