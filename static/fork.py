"""
fork 进程基础演示
"""
import os
import time

print("============================")
a = 1

pid = os.fork()
if pid < 0:
    print("创建进程失败")
elif pid == 0:
    time.sleep(2)
    print("创建新的进程")
    print("a = ",a) # 父进程在ｆｏｒｋ前开辟的空间子进程也拥有
    a = 10000
else:
    time.sleep(3)
    print("这是老进程")
    print("a:",a) #子进程改变不会影响父进程

print("fork 测试结束")
print("a-->",a) # 打印两次