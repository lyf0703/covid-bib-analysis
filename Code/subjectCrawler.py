import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor

username = 'YourUserName'
password = 'YourPassword'

def login(driver):
    driver.get('https://www.scopus.com/search/form.uri?display=basic#basic')
    driver.refresh()
    driver.get('https://www.scopus.com/signin.uri?origin=&zone=TopNavBar')
    driver.find_element(By.ID, 'bdd-email').send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, 'bdd-elsPrimaryBtn').click()
    time.sleep(1)
    driver.find_element(By.ID, 'bdd-password').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, 'bdd-elsPrimaryBtn').click()
    time.sleep(5)

bibData = pd.read_csv('2020.csv', header=0)
bibDOI = bibData['DOI'].tolist()
bibTitle = bibData['标题'].tolist()
bibLen = len(bibDOI)

def crawl_thread(start, end):
    driver = webdriver.Firefox()
    login(driver)
    for i in range(start, end):
        print('Crawling artile ' + str(i) + ' DOI:')

        print(bibDOI[i])
        try:
            DOI = bibDOI[i].replace('/', '%2f').replace('(', '%28').replace(')', '%29')
            link = 'https://www.scopus.com/results/results.uri?src=s&st1=' + DOI + '&sot=b&sdt=b&s=DOI%28' + DOI + '%29'
            print(link)
            while True:
                try:
                    driver.get(link)
                    time.sleep(5)
                    break
                except:
                    print('网络异常，30s后重试')
                    time.sleep(30)
        except:
            print('没有DOI，尝试以标题进行检索')
            print(bibTitle[i])
            title = bibTitle[i].replace('/', '%2f').replace('(', '%28').replace(')', '%29').replace(',', '%2c').replace('|','%7c').replace(' ','+').replace('`','%60')
            link = 'https://www.scopus.com/results/results.uri?sort=plf-f&src=s&st1='+ title +'&sot=b&sdt=b&sl=86&s=TITLE%28'+ title +'%29'
            print(link)
            while True:
                try:
                    driver.get(link)
                    time.sleep(5)
                    break
                except:
                    print('网络异常，30s后重试')
                    time.sleep(30)

        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        facet_area = soup.find('div', {'data-testid': 'facet-group-学科类别'})
        subject_elements = facet_area.find_all('div', {'class': 'title sc-els-facet'})

        subjects = [subject.get_text().replace(",", "，") for subject in subject_elements]
        subject = ",".join(subjects)

        print(subject)

        with open('2020subject_' + str(start) + '-' + str(end) + '.csv', 'a') as f:
            f.write(str(i)+','+str(subject))
            f.write('\r')

        time.sleep(2)
        print(' ')
    driver.quit()

if __name__ == "__main__":
    # 并发的最大线程数
    CONCURRENT_MAX = 1
    # 创建线程池
    with ThreadPoolExecutor(max_workers=CONCURRENT_MAX) as executor:
        num_per_thread = 100
        for i in range(0, bibLen, num_per_thread):
            executor.submit(crawl_thread, i, min(i + num_per_thread, bibLen))