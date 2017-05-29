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
            "comment.write": "https://www.tistory.com/apis/comment/write",
            "comment.modify": "https://www.tistory.com/apis/comment/modify",
            "comment.newest": "https://www.tistory.com/apis/comment/newest",
            "comment.delete": "https://www.tistory.com/apis/comment/delete",

            "guestbook.write": "https://www.tistory.com/apis/guestbook/write",
            "guestbook.modify": "https://www.tistory.com/apis/guestbook/modify",
            "guestbook.list": "https://www.tistory.com/apis/guestbook/list",
            "guestbook.delete": "https://www.tistory.com/apis/guestbook/delete",
        }


    def __init__(self, client_id, redirect_uri, client_secret, response_type="code", state="someValue"):
        self._client_id     = client_id
        self._client_secret = client_secret
        self._redirect_uri  = redirect_uri
        self._response_type = response_type
        self._state         = state

        self.state = "logout"
        self._blogName = "boycoding"
        params = \
            {
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

        driver.find_element_by_id("loginId").send_keys(self._id)
        driver.find_element_by_id("loginPw").send_keys(self._pw)
        driver.find_element_by_class_name("btn_login").click()

        try:
            driver.find_element_by_class_name("confirm").click()
        except :
            driver.quit()
            print("아이디 또는 비밀번호가 틀렸습니다.")
            return False


        url = driver.current_url
        parsed = urlparse.urlparse(url)
        self._code = str(urlparse.parse_qs(parsed.query)["code"][0])

        driver.quit()

        params = \
            {
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

        data = urlopen(self.URL["info"] + "?output=json&"  + self._token).read().decode()

        return self._toJsonItem(data)


    def categoryList(self):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"blogName":self._blogName}, "utf-8")

        data = urlopen(self.URL["category"] + "?" + params + "&output=json&" + self._token).read().decode()

        return self._toJsonItem(data)


    def post_list(self, page=1, count=30, categoryId="", sort="id"):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"page": page, "count": count, "categoryId": categoryId, "sort": sort, "blogName":self._blogName}, "utf-8")

        data = urlopen(self.URL["post.list"] + "?" + params + "&output=json&" + self._token).read().decode()

        return self._toJsonItem(data)


    def post_read(self, postId):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"postId": postId, "blogName":self._blogName}, "utf-8")

        data = urlopen(self.URL["post.read"] + "?" + params + "&output=json&" + self._token).read().decode()

        return self._toJsonItem(data)


    def guestBook_list(self):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"blogName":self._blogName}, "utf-8")

        data = urlopen(self.URL["guestbook.list"] + "?" + params + "&output=json&" + self._token).read().decode()

        return self._toJsonItem(data)

    def _toJsonItem(self, data):
        return json.loads(data)["tistory"]["item"]


