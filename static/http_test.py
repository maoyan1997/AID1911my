"""
http请求和响应测试
"""

from socket import *

# http -> 使用tcp传输
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096) # 接收到请求
print(data.decode())

data = """HTTP/1.1 404 Not Found
Content-Type:text/html

Tarena Python
"""
c.send(data.encode()) # 发送响应

c.close()
s.close()









