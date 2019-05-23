"""
ftp 文件服务器
并发网络更能训练
"""
from socket import *
from threading import Thread
import sys
import os
import time
# 全局变量
ADDR = ("0.0.0.0", 8828)
FTP = "/home/tarena/FTP/"


# 将请求功能封装为类
class FtpServer:
    def __init__(self,connfd,FTP_PATH):
        self.connfd = connfd
        self.path = FTP_PATH

    def do_list(self):
        # 获取文件列表
        files = os.listdir(self.path)
        if not files:
            self.connfd.send("该文件类别为空".encode())
            return
        else:
            time.sleep(0.1)
            self.connfd.send(b"OK")
            fs = ''
        for file in files:
            if file[0] != '.' and os.path.isfile(self.path+file):
                fs += file +'\n'
        self.connfd.send(fs.encode())

    def do_get(self,filename):
        try:
            fd = open(self.path+filename,'rb')
        except IOError:
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
            # 发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b"##")
                break
            self.connfd.send(data)
    def do_put(self,filename):
        if os.path.exists(self.path + filename):
            self.connfd.send("该文件已存在".encode())
            return
        self.connfd.send(b'OK')
        fd = open(self.path + filename,'wb')

        # 接收文件
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()



# 客户端处理函数
def handle(connfd):
    # 选择文件夹
    cls = connfd.recv(1024).decode()
    FTP_PATH = FTP + cls + '/'
    ftp = FtpServer(connfd,FTP_PATH)
    while True:
        # 接受客户请求
        data = connfd.recv(1024).decode()
        # 如果客户端断开但会data为空
        if data[0] == 'Q' or not data:
            return
        elif data[0] == 'L':
            ftp.do_list()
        elif data[0] == 'G':
            filename = data.split(' ')[-1]
            ftp.do_get(filename)
        elif data[0] == 'P':
            filename = data.split(' ')[-1]
            ftp.do_put(filename)




# 网络搭建
def main():
    sockft = socket()
    sockft.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockft.bind(ADDR)
    sockft.listen(3)
    print("Listen the port 8888....")

    while True:
        try:
            connfd,addr = sockft.accept()
        except KeyboardInterrupt:
            sys.exit("退出服务器")

        except Exception as e:
            print(e)
            continue

        client = Thread(target=handle, args=(connfd,))
        client.setDaemon(True)  # 分支线程随主线程退出
        client.start()

if __name__ == "__main__":
    main()