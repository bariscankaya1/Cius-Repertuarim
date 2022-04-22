# coding=utf-8
from os import lseek
from re import T
import time
from weakref import ref
import firebase_admin
from firebase_admin import db
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
cred_obj = firebase_admin.credentials.Certificate('cius-repertuar-firebase-adminsdk-ot70r-4e57dcded1.json')
default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://cius-repertuar-default-rtdb.firebaseio.com/"
        })
ref=db.reference("/")
browser=webdriver.Chrome("chromedriver.exe")
browser.get("https://www.turkuler.com/sozler/ta.asp")

sozler=browser.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[2]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/font/b/a[2]")
sozler.click()
i=2
id=1

try:
    while True:
        time.sleep(5)
        table=browser.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr["+str(i)+"]")
        turkuAdi=table.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr["+str(i)+"]/td[1]/a/font/b").text
        turkuURL=table.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr["+str(i)+"]/td[1]/a")
        url=turkuURL.get_attribute("href")
        browser.get(url)
        soz=browser.find_element_by_xpath("/html/body/table/tbody/tr/td[1]/table[2]/tbody/tr/td[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[1]/font").text
        soz=soz.split("Paylaş")
        soz=soz[0].split("<br>")
        ref.push(
            {
            "id":id,
            "isim":turkuAdi,
            "soz":soz[0]
            }
        )
        
        i=i+2
        browser.get("https://www.turkuler.com/sozler/ta.asp")

except:
    pass
