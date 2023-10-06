import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd



def main():
    bibData = pd.read_csv('2020.csv', header=0)
    bibLink = bibData['链接'].tolist()
    bibLen = len(bibLink)
    #for i in range(0,1000):
    #    print('正在抓取第 ' + str(i) + ' 个')
    #    getSciTopic(bibLink[i])

    chrome = R"/Your/Path/to/Chrome/Driver"  # 初始化ChromeDriver


    driver = webdriver.Chrome(chrome)  # 创建一个浏览器对象

    for i in range(0,1000):
        link = bibLink[i]

        while True:
            try:
                driver.get(link)  # 打开这个链接
                break
            except:
                print('网络错误，准备60s后重试')
                time.sleep(60)
                continue
        time.sleep(1)

        page = driver.page_source  # 保存这个页面
        # print(page)
        soup = BeautifulSoup(page, 'html.parser')

        elements = soup.find_all("div", {"class": "sciTopicsVal displayNone"})  # 抓取sci-topic
        try:
            topic = str(elements).split(':')[2].split(',')[0].strip('"').split(";")
        except:
            topic = ['没有']

        topic = str(topic).strip('[').strip(']').strip("'")

        with open('0-1000.csv', 'a') as f:
            f.write(str(topic))
            f.write('\r')


if __name__ == '__main__':
    main()

