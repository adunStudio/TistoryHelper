from urllib.request import urlopen
from urllib.parse import urlencode
import urllib.parse as urlparse
import time
import json




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

    def getToken(self, code):
        self._code = code
        params = \
            {
                "client_id": self._client_id,
                "client_secret": self._client_secret,
                "redirect_uri": self._redirect_uri,
                "code": code,
                "grant_type": "authorization_code"
            }

        self.URL["access"] += "?" + urlencode(params, 'utf-8')
        self._token = urlopen(self.URL["access"]).read().decode('utf-8')

        return self._token



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

    def post_write(self, title, content, visibility=0, published="", category=0, slogan="", tag=""):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"title": title, "content": content, "visibility": visibility, "published": published,
                            "category": category, "slogan": slogan, "tag": tag, "blogName":self._blogName,
                            "output": "json", "access_token": self._access_token}).encode("utf-8")

        data = urlopen(self.URL["post.write"], data=params).read().decode()

        return self._toJsonItem(data)

    def post_modify(self, title, content, postId, visibility=0, published="", category=0, slogan="", tag=""):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"title": title, "content": content, "postId": postId, "visibility": visibility, "published": published,
                            "category": category, "slogan": slogan, "tag": tag, "blogName":self._blogName,
                            "output": "json", "access_token": self._access_token}).encode("utf-8")

        data = urlopen(self.URL["post.modify"], data=params).read().decode()

        return self._toJsonItem(data)

    def post_delete(self, postId):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"postId": postId, "blogName": self._blogName, "output": "json", "access_token": self._access_token}).encode("utf-8")

        data = urlopen(self.URL["post.delete"], data=params).read().decode()

        return self._toJsonItem(data)

    def guestBook_list(self):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"blogName":self._blogName}, "utf-8")

        data = urlopen(self.URL["guestbook.list"] + "?" + params + "&output=json&" + self._token).read().decode()

        return self._toJsonItem(data)

    def comment_newest(self, page=1, count=10):

        if not self.isLogin():
            print("로그인상태가 아닙니다.")
            return False

        params = urlencode({"page": page, "count": count, "blogName":self._blogName}, "utf-8")

        data = urlopen(self.URL["comment.newest"] + "?" + params + "&output=json&" + self._token).read().decode()

        return self._toJsonItem(data)

    def _toJsonItem(self, data):
        try:
            return json.loads(data)["tistory"]["item"]
        except:
            try:
                return json.loads(data)["tistory"]
            except:
                print("삭제권한이 없습니다.")



