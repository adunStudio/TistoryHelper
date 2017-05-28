from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tistoryApi


secretKey = ""


tistory = tistoryApi.Tistory(client_id="d420680d548dc8d2c63b91010c017ecd", client_secret=secretKey, redirect_uri="http://boycoding.tistory.com/category")

while tistory.state != "login":
    blogId = input("아이디를 입력해주세요: ")
    blogPw = input("비밀번호를 입력해주세요:")
    tistory.login(id=blogId, pw=blogPw)

print("로그인 성공")

while 1:
    print("----------------------------")
    print("1. 블로그 정보")
    print("2. 카테고리 목록")
    print("3. 글 목록")
    print("----------------------------")

    command = int(input("명령어를 선택해주세요: "))

    if command is  1:
        print(tistory.info())

    elif command is 2:
        print(tistory.categoryList())

    elif command is 3:
        data = tistory.post()
        count = data["totalCount"]
        posts = data["posts"]

        print("총 게시물 개수:", count)

        for post in posts:
            print(post["title"])




