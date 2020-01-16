"""
获取进程PID号
"""
import os

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Chile PID:",os.getpid()) # 子
    print("Get parent PID:",os.getppid()) # 父
else:
    print("Get Chile PID:",pid) # 子
    print("Parent PID:",os.getpid()) # 父
