import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('binhphu.xlsx')
worksheet = workbook.add_worksheet()
# Pass in the database path, db.s3db or test.sqlite
conn=sqlite3.connect('/home/thanh/Documents/crawl_score/thong ke diem lop 10/catinh.db')
c=conn.cursor()
mysel = c.execute("select * from diem_binhphu")
for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i, j, value)
workbook.close()