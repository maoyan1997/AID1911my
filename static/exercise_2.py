import time
import os

def fun1():
    print("求10000000以内整数和")
    time.sleep(2)
    print("执行完成")

def fun2():
    print("求100000以完数和")
    time.sleep(3)
    print("执行完成")

# 4s以内执行完上面两个函数
st = time.time()

pid = os.fork()
if pid == 0:
    fun1()
else:
    fun2()

print("执行时间:",time.time() - st)












