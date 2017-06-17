# TistoryHelper
Tistory Helper with Python

and Python 3 Libray for interacting with the Tistory RESTful API.

[Tistory API documentation](http://www.tistory.com/guide/api/index)

### Dependencies

[Flask](http://flask.pocoo.org/)

	pip3 install flask


### Example API usage
```python
blog = Tistory(client_id="", client_secret="", redirect_uri="")
blog.login(id="", pw="")

print(blog.info())
print(blog.categoryList())

posts = blog.post("list")

for post in posts:
    print(post["title"])

blog.post_write(title="", content="", published="", tag="")
blog.post_modify(postId="", title="", content="", published="", tag="")
blog.post_delete(postId="")
```

### Notes
The Tistory API returns JSON.

### Development journal

현재 개발중.

2017.5.28(Sun) : 로그인, 블로그 정보, 카테고리 목록, 최신 글 목록

2017.5.29(Mon) : 글 읽기, 방명록 목록

### Issue

텀프로젝트로 파이썬을 이용해서 데스크탑 GUI 환경에서의 AdunDocs를 만들어 볼려했다.

결과적으로 이렇게 쟛같을 수가 없다.

우선 TistoryAPI Library가 파이썬에는 존재하지 않는다.
(JAVA, PHP, NodeJS 다 있는데 파이썬만 없다.)

정확히는 존재 하지만 1년 전의 metaweblog API를 사용한 방식이다.
(티스토리가 oauth2 방식을 채택하면서 작년까지 제공하던 XMLRPC 방식을 이용한 metaweblog API 제공을 중단해버렸다.)

그래서 텀프로젝트 겸 api클래스를 한번 만들어 보기로 결심했다.

oauth2방식은 웹브라우저 지원 없이 로그인 구현하기가 힘들다.
 
결과적으로 selenium과 chromedriver를 이용해서 원격조정 하는 방식으로 로그인을 구현했다.

이 부분은 추후 적절한 webview를 이용해서 다시 처리해야겠다.

---

flask를 이용해서 웹서버를 가동 후 웹브라우저를 이용하게끔 하였다.
