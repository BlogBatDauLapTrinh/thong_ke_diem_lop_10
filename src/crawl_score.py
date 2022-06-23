import argparse
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
BASE_URL = "https://binhduong.edu.vn/tra-cuu-diem-tuyen-sinh-lop-10.html?ky-thi=ts10_22_23&tu-khoa="

class Student():
    def __init__(self,student_code,name,old_school,nv1,nv2,additional_score,literature_score,english_score,math_score,total_score):
        self.name = name
        self.student_code = student_code
        self.old_school = old_school
        self.nv1 = nv1
        self.nv2 = nv2
        self.additional_score = additional_score
        self.literature_score = literature_score
        self.english_score = english_score
        self.math_score = math_score
        self.total_score = total_score

    def __str__(self) -> str:
        return f"{self.name},{self.student_code},{self.old_school},{self.nv1},{self.nv2},{self.additional_score},{self.literature_score},{self.english_score},{self.math_score},{self.total_score}"

class GETSCOREOFSCHOOL():
    def __init__(self,school_index) -> None:
        if school_index < 10:
            self.school_index = "0" + str(school_index)
        else:
            self.school_index = str(school_index)
        self.url = BASE_URL
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=op)
    
    def crawl_all(self):
        for student_idx in range(FIRST_STUDENT_INDEX,LAST_STUDENT_INDEX):
            student_data = self.get_student_data(student_idx)
            with open(f'data_csv/data_{self.school_index}.csv','a') as f:
                f.writelines(str(student_data)+"\n")
        self.driver.quit()

    def get_student_data(self,student_idx):
        html = self.get_html_student_score(student_idx)
        return self.extract_data_from_html(html)

    def get_html_student_score(self,student_index):
        if int(student_index) < 10:
            student_index = f"000{student_index}"
        elif int(student_index) < 100:
            student_index = f"00{student_index}"
        elif int(student_index) < 1000:
            student_index = f"0{student_index}"
        self.driver.get(self.url)
        input_element = self.driver.find_element(by=By.NAME,value="tu-khoa")
        input_element.send_keys(f"{self.school_index}{student_index}")
        input_element = self.driver.find_element(by=By.CLASS_NAME,value="ml-md-3").click()
        while not self.is_page_ready(student_index):
            sleep(1)
        with open('html.html','w') as f:
            f.writelines(f"{self.driver.page_source}")
        sub_url = f"sbd"
        wait = WebDriverWait(self.driver, 10) 
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, f'{self.school_index}{student_index}'))).click()
        url_to_detail = self.driver.find_element_by_xpath('//a[contains(@href, "%s")]' % sub_url)
        print(url_to_detail.text)
        actions = ActionChains(self.driver)
        sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()
        return self.driver.page_source

    def extract_data_from_html(self,html):
        soup = BeautifulSoup(html)
        row = soup.find("div", {"class":"row"})
        name = row.find("h3", {"class":"font-xlarge font-weight-bold text-center text-uppercase text-danger mb-4"}).get_text().strip().replace("\n","")
        student_code = row.find("div", {"class":"col-md-5 col-lg-6"}).find("div",{"class":"d-flex"}).get_text().strip().replace("\n","")[12:19]
        old_school = row.find_all("div",{"class":"d-flex mt-2"})[3].get_text().strip()[14:].replace("\n","")
        nv1 = row.find("div", {"class":"col-md-7 col-lg-6"}).find_all("span")[0].get_text().strip().replace("\n","")
        nv2 = row.find("div", {"class":"col-md-7 col-lg-6"}).find_all("span")[1].get_text().strip().replace("\n","")
        additional_score = row.find("div", {"class":"col-md-7 col-lg-6"}).find_all("span")[4].get_text().strip().replace("\n","")
        result = soup.find("table",{"class":"table table-striped table-hover table-bordered mb-0"})
        literature_score = result.find_all("td")[0].get_text().strip().replace("\n","")
        english_score = result.find_all("td")[1].get_text().strip().replace("\n","")
        math_score = result.find_all("td")[2].get_text().strip().replace("\n","")
        total_score = result.find_all("td")[5].find_all("p")[0].get_text().strip().replace("\n","")[14:]
        return Student(student_code,name,old_school,nv1,nv2,additional_score,literature_score,english_score,math_score,total_score)

    def is_page_ready(self,student_index):
        return student_index in str(self.driver.page_source)

##################################MAIN HERE####################################################################################################################
parser = argparse.ArgumentParser()
parser.add_argument("-si", "--schoolindex", help="School index", type=int)
parser.add_argument("-lsi", "--laststudentindex", help="Student index", type=int)
parser.add_argument("-fsi", "--firststudentindex", help="Student index", type=int)
args = parser.parse_args()

SCHOOL_INDEX = args.schoolindex
LAST_STUDENT_INDEX = args.laststudentindex
FIRST_STUDENT_INDEX = args.firststudentindex

print(SCHOOL_INDEX,LAST_STUDENT_INDEX)
get_score_object = GETSCOREOFSCHOOL(SCHOOL_INDEX)
get_score_object.crawl_all()
print(SCHOOL_INDEX,LAST_STUDENT_INDEX)