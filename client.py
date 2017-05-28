from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tistoryApi
import os


secretKey = "test"
blogId = "test@daum.net"
blogPw = "test"

tistory = tistoryApi.Tistory(client_id="d420680d548dc8d2c63b91010c017ecd", client_secret=secretKey, redirect_uri="http://boycoding.tistory.com/category")
tistory.login(id=blogId, pw=blogPw)
print(tistory.info())
print(tistory.categoryList())
#os.environ["webdriver.chrome.dirver"] = chromeDriver


