# NetTools-nslookup

## About
The front-end is developed using Bootstrap, and the back-end is developed using Python3 with Flask and jinja2.
The `socket` library is used to retrieve the results.

## Structure

main_example.py (逆引きの例)
```python
import socket

def reverse_lookup(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        return "No result"

result = reverse_lookup("example.com")
print(result) #203.0.113.0
```

`socket.gethostbyaddr()[0]`で正引きの結果を取得します。逆に`socket.gethostbyname()`で逆引きの結果を取得します。
上記のコードは逆引きの例です。
`main.py`では、POSTされたドメイン名(FQDN)又はIPv4アドレスを正引き・逆引きして返すシンプルな構造です。
なお、IPv6には対応していません。

## Libraries
- Flask
- jinja2
- request
- jsonify
- socket
Other dependent libraries are required.

# License
The source code is licensed MIT. The website content is licensed CC BY 4.0,see LICENSE.
