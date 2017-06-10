from __future__ import print_function
import time
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import send_from_directory
from flask import jsonify
import tistoryApi


secretKey = "d420680d548dc8d2c63b91010c017ecd6fff6ac0ec56a319c1f6055dd49956d72b03ca07"
tistory = tistoryApi.Tistory(client_id="d420680d548dc8d2c63b91010c017ecd", client_secret=secretKey, redirect_uri="http://oppacoding.dothome.co.kr/ac.php")

app = Flask(__name__)
#app.static_folder = 'static'

print('sdfsd')




@app.route("/api/info", methods=["GET"])
def info2():
    print(tistory.info())
    return jsonify(tistory.info())

@app.route("/login")
def login():
    return redirect(tistory.URL["login"])

@app.route("/tab")
def maint():
    return "1"

@app.route("/code", methods=['GET'])
def code():
    tistory.getToken(request.args.get('code'))
    return redirect("/")

@app.route("/static/<path:path>")
def static2(path):
    return send_from_directory('static', path)



@app.route("/")
def main():
    return render_template('index.html')






if __name__ == "__main__":
    print('oh hello2')
    app.run(host='127.0.0.1', port=7711)