
#        Copyright (c) 2021 Naxii
#        This code is released under the MIT License, see LICENSE, see LICENSE.
#        This website content is released under the CC BY 4.0 License, see LICENSE.

from flask import Flask, jsonify, render_template, request
import socket, secret
#secretはIPアドレスとドメインのブラックリストを`blacklist`というリスト変数で保存しています。
#secret.pyとその中のblacklist変数がないと動かないよ！

app = Flask(__name__)

def forward_lookup(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "結果なし"
def reverse_lookup(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "結果なし"

@app.route("/")
def index():
    return render_template("index.html", title="nslookup")

@app.route("/forward", methods=["GET", "POST"])
def forward():
    ipadd = request.form.get("ipadd")
    result = ""
    result = str(forward_lookup(ipadd))
    print(result in secret.blacklist)
    if ((result in secret.blacklist) or (ipadd in secret.blacklist)) == True:
        #念には念を入れてということで二重検証(実際POSTされたやつだけ検証しとけばいいけどこっちのほうが確証がありそうなので)
        result = "結果なし"
    return render_template("forward.html", result=result, title="nslookup - 正引き(forward)")

@app.route("/reverse", methods=["GET", "POST"])
def reverse():
    domain = request.form.get("domain")
    result = str(reverse_lookup(domain))
    if ((result in secret.blacklist) or (domain in secret.blacklist)) == True:
        result = "結果なし"
    return render_template("reverse.html", result=result, title="nslookup - 逆引き(reverse)")

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'error':'internal error'
    }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error':'not found'
    }), 404

app.run(debug=False)
