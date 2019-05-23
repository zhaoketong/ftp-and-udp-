"客户端"
from socket import *
import sys
from time import sleep
# 具体功能
class FtpClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd
    def do_list(self):
        self.sockfd.send(b'L') # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode()
        # OK表示请求成功
        if data == 'OK':

            data = self.sockfd.recv(4096)
            print(data.decode())
        else:
            print(data)
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")
    def do_get(self,filename):
        # 发送请求
        self.sockfd.send(('G '+filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            fd = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                fd.write(data)
            fd.close()
    def do_put(self,filename):
        try:
            fd = open(filename,'rb')
        except IOError:
            print("文件不存在")
            return

        filename = filename.split('/')[-1]
        self.sockfd.send(('P '+ filename).encode())
        # 等待回复
        data = self.sockfd.recv(128)
        if data.decode() == 'OK':

            while True:
                data = fd.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            fd.close()
        else:
            print(data)

# 发起请求
def request(sockfd):
    ftp = FtpClient(sockfd)
    while True:
        print("\n========命令选项=========")
        print("*********查看文件列表************")
        print("*********下载文件************")
        print("*********上传文件************")
        print("*********退出************")

        cmd = input("请输入选项:")
        if cmd == "查看文件列表":
            ftp.do_list()
        elif cmd[:4] == "下载文件":
            filename = cmd.strip().split(' ')[-1]
            ftp.do_get(filename)
        elif cmd == "上传文件":
            filename = input("请输入文件路径:")
            ftp.do_put(filename)
        elif cmd == "退出":
            ftp.do_quit()


# 网络连接
def main():
    # 服务器地址
    ADDR = ("176.215.155.161",8888)
    sockfd = socket()
    sockfd.getsockopt(SOL_SOCKET, SO_REUSEADDR)
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("连接服务器失败",e)
        return
    else:
        print("*******data file 图片*****")
        cls = input("请输入文件种类:")
        if cls not in['data', 'file', '图片']:
            print("请重新输入:")
            return
        else:
            sockfd.send(cls.encode())
            request(sockfd) # 发送具体请求


if __name__ == "__main__":
    main()






























