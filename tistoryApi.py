from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from urllib.parse import urlencode
import urllib.parse as urlparse
import time
import json


chromeDriver = "/Users/adun/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=chromeDriver)

class Tistory:


    def __init__(self, client_id, redirect_uri, client_secret, response_type="code", state="someValue"):
        self._client_id     = client_id
        self._client_secret = client_secret
        self._redirect_uri  = redirect_uri
        self._response_type = response_type
        self._state         = state

        self.state = "logout"

        params = {
            "client_id": self._client_id,
            "redirect_uri": self._redirect_uri,
            "response_type": self._response_type,
            "state": self._state
            }

        self.URL["login"] += "?" + urlencode(params)



    def login(self, id, pw):
        self._id = id
        self._pw = pw

        driver.get(self.URL["login"])

        #time.sleep(1)
        driver.find_element_by_id("loginId").send_keys(self._id)
        driver.find_element_by_id("loginPw").send_keys(self._pw)
        driver.find_element_by_class_name("btn_login").click()
        #time.sleep(1)

        try:
            driver.find_element_by_class_name("confirm").click()
        except :
            driver.quit()
            print("아이디 또는 비밀번호가 틀렸습니다.")
            return False

        #time.sleep(1)

        url = driver.current_url
        parsed = urlparse.urlparse(url)
        self._code = str(urlparse.parse_qs(parsed.query)["code"][0])

        driver.quit()

        params = {
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "redirect_uri": self._redirect_uri,
            "code": self._code,
            "grant_type": "authorization_code"
        }

        self.URL["access"] += "?" + urlencode(params, 'utf-8')

        self._token = urlopen(self.URL["access"]).read().decode('utf-8')

        self.state = "login"
        return True

    def isLogin(self):
        return self.state == "login"

    def info(self):
        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        return json.loads(urlopen(self.URL["info"] + "?" + self._token + "&output=json").read().decode())

    def categoryList(self):
        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False
        return json.loads(urlopen(self.URL["category"] + "?" + self._token + "&blogName=boycoding&output=json").read().decode())

    def post(self, mode=""):
        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        data = json.loads(urlopen(self.URL["post.list"] + "?" + self._token + "&blogName=boycoding&output=json&count=30").read().decode())

        return data["tistory"]["item"]

    URL = \
        {
            "login": "https://www.tistory.com/oauth/authorize",
            "access": "https://www.tistory.com/oauth/access_token",

            "info": "https://www.tistory.com/apis/blog/info",

            "post.write": "https://www.tistory.com/apis/post/write",
            "post.modify": "https://www.tistory.com/apis/post/modify",
            "post.list": "https://www.tistory.com/apis/post/list",
            "post.read": "https://www.tistory.com/apis/post/read",
            "post.attach": "https://www.tistory.com/apis/post/attach",
            "post.delete": "https://www.tistory.com/apis/post/delete",

            "category": "https://www.tistory.com/apis/category/list",

            "comment.list": "https://www.tistory.com/apis/comment/list",
            "comment.write": "https://www.tistory.com/apis/comment/lis",
            "comment.modify": "https://www.tistory.com/apis/comment/lis",
            "comment.newest": "https://www.tistory.com/apis/comment/lis",
            "comment.delete": "https://www.tistory.com/apis/comment/lis",

            "guestbook.write": "https://www.tistory.com/apis/guestbook/write",
            "guestbook.modify": "https://www.tistory.com/apis/guestbook/write",
            "guestbook.list": "https://www.tistory.com/apis/guestbook/write",
            "guestbook.delete": "https://www.tistory.com/apis/guestbook/write",
        }


