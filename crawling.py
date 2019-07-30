from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib
import argparse

def crawling(names, n, path_exe = 'chromedriver.exe'):    
    for i in names:
        url = "https://www.google.co.in/search?q="+i+"&source=lnms&tbm=isch"
        browser = webdriver.Chrome(executable_path= path_exe)

        browser.get(url)
        header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

        if not os.path.exists(i):
            os.mkdir(i)

        for _ in range(n):
            browser.execute_script("window.scrollBy(0,10000)")

        for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
            img = json.loads(x.get_attribute('innerHTML'))["ou"]
            imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
            try:
                req = urllib.request.Request(img, headers=header)
                raw_img = urllib.request.urlopen(req).read()
                File = open(os.path.join(i , i + "_" + str(counter) + "." + imgtype), 'wb')
                File.write(raw_img)
                File.close()
            except:
                continue
        browser.close()

def sorting(names, path, formats='jpg'):
    for name in names:
    filepath= os.oath.join(path, name)
    for file in os.scandir(filepath):
        if '.jpg' not in file.name:
            os.remove(file.path)
    