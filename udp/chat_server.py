
#  服务端
from socket import *
import os,sys


# 服务器地址
ADDR = ("0.0.0.0",8815)

# 存储用户信息
user = {}

# 进入聊天室
def do_login(s,name,addr):
    if name in user or "管理员" in name:
        s.sendto("该用户以存在".encode(),addr)
        return
    s.sendto(b'OK',addr)

    # 通知其他人
    msg = "欢迎%s进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])

    # 将用户加入
    user[name] = addr
# 聊天
def do_chat(s,name,text):
    msg = "%s 发言: %s"%(name,text)
    for i in user:
        if i != name :
            s.sendto(msg.encode(),user[i])


# 退出
def do_quit(s,name):
    msg = "%s退出了聊天室"%name
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXIT',user[i])
    # 将用户删除
    del user[name]


# 接受各种客户端请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        msg = data.decode().split(" ")
        # 区分请求类型
        if msg[0] == 'L':
            do_login(s,msg[1],addr)
        elif msg[0] == 'C':
            text = ' '.join(msg[2:])
            do_chat(s,msg[1],text)
        elif msg[0] == "Q":
            if msg[1] not in user:
                s.sendto(b'EXIT',addr)
                continue
            do_quit(s,msg[1])



# 创建网络连接
def main():
    # 套接字创建
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        while True:
            text = input("管理员消息")
            msg = "C 管理员 " + text
            s.sendto(msg.encode(),ADDR)

    # 请求处理
    else:
        do_request(s) # 处理客户端请求


if __name__ == '__main__':
    main()














