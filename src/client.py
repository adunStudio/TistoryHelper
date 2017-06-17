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
    print("6. 글 쓰기")
    print("7. 글 수정")
    print("8. 글 삭제")
    print("9. 최근 댓글")
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
            if int(post["comments"]) > 0 :
                post["title"] += "[" + post["comments"] + "]"

            print("ID:", post["id"], "제목:", post["title"])

    elif command is 4:
        id = int(input("읽을 글의 ID를 입력해주세요: "))

        post = tistory.post_read(postId=id)

        print("글 제목 : ", post["title"])
        print("글 등록 일 : ", post["date"])
        print("글 내용 : ")
        print(post["content"])

    elif command is 5:
        data = tistory.guestBook_list()
        guestbooks = data["guestbooks"]

        for guestbook in guestbooks:
            print(guestbook["name"], ":", guestbook["comment"])

            if guestbook["replies"] != "":
                replies = guestbook["replies"]["reply"]

                if type(replies) is dict:
                    print("   - ", replies["name"], ":", replies["comment"])
                else:
                    for reply in replies:
                        print("   - ", reply["name"], ":", reply["comment"])



    elif command is 6:
        title = input("제목 : ")
        content = input("내용 : ")
        print(tistory.post_write(title=title, content=content))

    elif command is 7:
        postId = input("수정할 글의 ID를 입력해주세요: ")
        title = input("제목 : ")
        content = input("내용 : ")
        print(tistory.post_modify(postId=postId, title=title, content=content))

    elif command is 8:
        postId = input("삭제할 글의 ID를 입력해주세요: ")
        print(tistory.post_delete(postId=postId))

    elif command is 9:
        data = tistory.comment_newest()
        comments = data["comments"]

        for comment in comments:
            print("ID:", comment["id"], ", 작성자:", comment["name"], ",제목:", comment["comment"])






