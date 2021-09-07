from flask import Flask, request, redirect

app = Flask(__name__)


@app.route('/static.js')
def static_file():
    return "static file"


@app.route('/admin')
def admin():
    return "admin"


@app.route('/login')
def login():
    return "you need login"


def isadmin():
    print("request.root_url: %s" % request.root_url)
    print("request.base_url: %s" % request.base_url)
    print("request.url: %s" % request.url)
    print("request.full_path: %s" % request.full_path)
    print("request.path: %s" % request.path)
    if not request.full_path.endswith(".js?"):  # 静态文件跳过
        if not request.full_path.startswith("/login"):  # 登录界面跳过
            return redirect("login")


if __name__ == "__main__":
    app.before_request(isadmin)
    app.run(host="0.0.0.0", port=80)
