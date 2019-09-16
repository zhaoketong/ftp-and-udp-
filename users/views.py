import hashlib
from django.shortcuts import render,redirect
from users.models import Users
# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
# 首页
def home(request):
    return render(request,'home.html')

# 注册
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

def register_server(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        account = request.POST['account']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        account1 = Users.objects.filter(account=account)
        if not nickname:
            return HttpResponse('请输入用户名')
        if not account:
            return HttpResponse('请输入账号')
        if account1:
            return HttpResponse('该账号已存在')
        if not pwd1:
            return HttpResponse('请输入密码')
        if not  pwd2:
            return HttpResponse('请输入密码')
        if pwd1 != pwd2:
            return HttpResponse('两次密码不一致')
        h_p = hashlib.sha1()
        h_p.update(pwd1.encode())
        try:
            Users.objects.create(account=account,nickname=nickname,password=h_p.hexdigest())
        except:
            return HttpResponse('注册失败')
        msg = '注册成功'
        return HttpResponse(msg)

# 登录
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        account = request.POST['account']
        try:
            info = Users.objects.get(account=account)
        except:
            return HttpResponse(300)


        pwd = request.POST['pwd']
        h_p = hashlib.sha1()
        h_p.update(pwd.encode())
        pwd1 = info.password
        if pwd1 == h_p.hexdigest():
            request.session['nickname'] = info.nickname
            return HttpResponse('成功')
        else:
            return HttpResponse(300)

# 首页
def index(request):
    nickname = request.session.get('nickname')
    return render(request,'index.html',locals())


# 退出登录

def logout(request):
    request.session.flush()
    if not request.session.get('nickname'):
        return render(request,'home.html')

































