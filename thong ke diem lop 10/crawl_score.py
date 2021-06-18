import sqlite3
from sqlite3 import Error
from time import sleep
import requests
import json
from bs4 import BeautifulSoup
import requests

def download_data(mshs):
    mshs = '0' + str(mshs)
    url = 'http://sgd2.netvn.vn/tra-cuu-diem-tuyen-sinh-lop-10.html?ky-thi=ts_k10_2021_2022_new&tu-khoa='+ mshs + '&sbd=' + mshs
    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content,  "html.parser")
    # print(soup.prettify()) # print the parsed data of html
    all_span = soup.find_all('span')

    all_span = str(all_span)
    all_span = all_span.replace("<span>","")
    all_span = all_span.replace("</span>","")
    all_span = all_span.split(',')

    print(mshs)
    if len(all_span) < 6:
        return 
    mshs = int(mshs)
    truong_cu = all_span[6]
    nv1 = int(all_span[7].strip())
    if all_span [8] != None and len(all_span [8].strip())>0:
        nv2 = int(all_span [8].strip())
    else:
        nv2 = 0
    if "V" in all_span[12]:
        tong_diem = 0
    else:
        tong_diem = float(all_span[12].strip())

    insertVariableIntoTable(mshs,truong_cu,nv1,nv2,tong_diem)
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def insertVariableIntoTable(mshs,truong_cu,nv1,nv2,tong_diem):
    conn = create_connection('bangdiem.db')
    # conn = sqlite3.connect('bangdiem.db')
    c = conn.cursor()
    sqlite_insert_with_param = """INSERT INTO tranvanon(mshs,truong_cu,nv1,nv2,tong_diem) 
                          VALUES (?, ?, ?, ?, ?);"""
    data_tuple = (mshs,truong_cu,nv1,nv2,tong_diem)
    c.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    conn.close()

for i in range(80001,80934):
    download_data(i)
