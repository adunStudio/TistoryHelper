from __future__ import print_function
import time
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import send_from_directory
from flask import jsonify
from flask import make_response

import tistoryApi


secretKey = "cc1dc1840c45306f2703e06cc752c4c3eaf3f200fe1f244a6a5991f9e18d869aa2a08259"
tistory = tistoryApi.Tistory(client_id="cc1dc1840c45306f2703e06cc752c4c3", client_secret=secretKey, redirect_uri="http://localhost:7711/code")

app = Flask(__name__)


@app.route("/api/info")
def info_tistory():
    return tistory.info()

@app.route("/api/category")
def category_tistory():
    return jsonify(tistory.categoryList())

@app.route("/api/post/list", methods=['GET'])
def post_list_tistory():
    categoryId = request.args.get('categoryId')
    return jsonify(tistory.post_list(categoryId=categoryId))

@app.route("/api/post/read", methods=['GET'])
def post_read_tistory():
    postId = request.args.get('postId')
    return jsonify(tistory.post_read(postId=postId))

@app.route("/api/post/backup", methods=["GET"])
def post_backup_tistory():
    postId = request.args.get('postId')
    data = tistory.post_read(postId=postId)
    backup = tistory.post_backup(postId=postId)
    title = data["id"]
    response = make_response(backup)
    response.headers["Content-Disposition"] = "attachment; filename="+str(title)+".xml"
    return response

@app.route("/code", methods=['GET'])
def code2():
    tistory.getToken(request.args.get('code'))
    return redirect("http://localhost:7711/")

@app.route("/login")
def login():
    return redirect(tistory.URL["login"])

@app.route("/static/<path:path>")
def static2(path):
    return send_from_directory('static', path)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    print('oh hello2')
    app.run(host='127.0.0.1', port=7711)