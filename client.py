from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tistoryApi
import getpass

secretKey = ""


tistory = tistoryApi.Tistory(client_id="d420680d548dc8d2c63b91010c017ecd", client_secret=secretKey, redirect_uri="http://boycoding.tistory.com/category")

while tistory.state != "login":
    blogId = input("아이디를 입력해주세요: ")
    blogPw = input("비밀번호를 입력해주세요: ")
    tistory.login(id=blogId, pw=blogPw)

print("로그인 성공")

while 1:
    print("----------------------------")
    print("1. 블로그 정보")
    print("2. 카테고리 목록")
    print("3. 글 목록")
    print("4, 글 읽기")
    print("5. 방명록")
    print("----------------------------")

    command = int(input("명령어를 선택해주세요: "))

    if command is  1:
        print(tistory.info())

    elif command is 2:
        print(tistory.categoryList())

    elif command is 3:
        data = tistory.post_list()
        count = data["totalCount"]
        posts = data["posts"]

        print("총 게시물 개수:", count)

        for post in posts:
            print("ID:", post["id"], "제목:", post["title"])

    elif command is 4:
        id = int(input("읽을 글의 ID를 입력해주세요: "))

        post = tistory.post_read(id)

        print("글 제목 : ", post["title"])
        print("글 등록 일 : ", post["date"])
        print("글 내용 : ")
        print(post["content"])

    elif command is 5:
        print(tistory.guestBook_list())




