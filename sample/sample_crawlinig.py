import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import csv

exchanges = ['korbit', 'upbit', 'coinone', 'bithumb', 'gopax']

for exchange in exchanges:
    url = 'https://nomics.com/exchanges/{0}/history'.format(exchange)
    datas = []

    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    time.sleep(3)

    total_page_num = driver.find_element(By.XPATH, r'//*[@id="__next"]/div[1]/div[4]/div/section/div/div[2]/div/div[2]/div[2]/div/ul/li[8]/a').text
    total_page_num = int(total_page_num)

    for j in range(total_page_num):
        for i in range(100):
            try:
                date = driver.find_element(By.XPATH, r'//*[@id="currency-markets-table"]/tbody/tr[%d]/td[2]/div' %(i+1)).text
                data = driver.find_element(By.XPATH, r'//*[@id="currency-markets-table"]/tbody/tr[%d]/td[3]/div/div/span' %(i+1)).text

                if data == "—":
                    datas.append([date, 0])
                else:
                    transed_data = data.replace(",", "")
                    datas.append([date, int(float(transed_data[1:]))])
            except:
                print("no data")
                pass

        if j <= (total_page_num - 2):
            driver.get(r'https://nomics.com/exchanges/{0}/history/{1}'.format(exchange, j+2))
            time.sleep(3)

    with open("csv_data_{0}".format(exchange), "w") as file:
        writer = csv.writer(file)
        writer.writerows(datas)