"""
如果浏览器向我请求内容为 / 就把刚才的网页内容给他作为响应体
如果向我请求其他的内容，则给浏览器返回404
"""
from socket import *

# 完成和浏览器的交互
def request(connfd):
    # 获取客户端请求
    data = connfd.recv(2048)
    # 从请求中获取请求内容
    request_line = data.decode().split('\n')[0]
    info = request_line.split(' ')[1]

    #　判断请求内容是什么
    if info == '/':
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        with open('index.html') as f:
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "Sorry......"
    connfd.send(response.encode()) #　发送响应

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8000))
s.listen(3)
while True:
    connfd,addr = s.accept()
    request(connfd)
