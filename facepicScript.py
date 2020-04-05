# python3
# Script aiming to web scrap the content of 

import time
import os
import requests
import getpass

# email = input("What is your facebook email account ? : ")
# pwd = getpass.getpass(prompt='What is your facebook password ? : ', stream=None)
# url = input("What's the url of the first pic ? : ")

email = "clementinecc@gmail.com"
pwd = "cr1n0l1ne"
url = "https://www.facebook.com/photo.php?fbid=10162357974705576&set=pb.653320575.-2207520000..&type=3&theater"

# with selenium
from selenium import webdriver
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.manager.showWhenStarting", False)
mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
fp.set_preference("pdfjs.disabled", True)
browser = webdriver.Firefox(firefox_profile=fp)

# open the Iris website from the local server
browser.get('https://www.facebook.com/')

# log in
browser.find_element_by_css_selector('#email').send_keys(email)
browser.find_element_by_css_selector('#pass').send_keys(pwd)
browser.find_element_by_css_selector('.uiButtonConfirm').click()


browser.get(url)


time.sleep(3)

for i in range(0,100000):
    # get the image source
    imgElem = browser.find_element_by_css_selector('.spotlight')
    src = imgElem.get_attribute('src')
    img = requests.get(src)
    imageFile = open(os.path.join('pics_album', os.path.basename("FB_tagged_{}.jpg".format(str(i+1)))), 'wb')
    for chunk in img.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # download the image
    browser.find_element_by_css_selector('.snowliftPager.next').click()
