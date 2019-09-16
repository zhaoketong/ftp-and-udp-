from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse,Http404
import json
import time
# Create your views here.
from member.models import Member,Rechar,Consume

# 注册会员
def reg(request):
    nickname = request.session.get('nickname')
    if nickname:
        if request.method == 'GET':
            return render(request,'reg.html',locals())
        elif request.method == 'POST':

            card = int(request.POST['card'])
            phone = int(request.POST['phone'])
            name = request.POST['name']
            gender = request.POST['gender']
            bir = str(request.POST['bir'])
            pwd1 = request.POST['pwd1']
            pwd2 = request.POST['pwd2']
            if not card:
                return HttpResponse(401)
            if not phone:
                return HttpResponse(402)
            if not name:
                return HttpResponse(403)
            if not gender:
                return HttpResponse(404)
            if not bir:
                return HttpResponse(405)
            if not pwd1:
                return HttpResponse(406)
            if not pwd2:
                return HttpResponse(407)
            if pwd1 != pwd2:
                return HttpResponse(408)
            try:
                info = Member.objects.get(card=card)
                if info:
                    return HttpResponse(409)
            except:
                try:
                    Member.objects.create(card=card,phone=phone,name=name,gender=gender,
                                          bir=bir,pwd=pwd1,inte=0,money=0)
                    return HttpResponse(410)
                except:
                    return HttpResponse(411)
    else:
        return render(request,'home.html')
# 会员信息查询
def info(request):
    nickname = request.session.get('nickname')
    if nickname:
        if request.method == 'GET':
            return render(request,'info.html')
        elif request.method == 'POST':
            card = request.POST['card']
            if not card:
                return HttpResponse(501)
            try:
                info = Member.objects.get(card=card)
                msg = {}
                msg['name'] = info.name
                msg['phone'] = info.phone
                if info.gender == '0':
                    msg['gender'] = '男'
                else:
                    msg['gender'] = '女'
                msg['bir'] = info.bir
                msg['inte'] = info.inte
                msg['money'] = info.money
                request.session['card'] = info.card
                return HttpResponse(json.dumps(msg))
            except:
                return HttpResponse(501)
    else:
        return render(request,'home.html')


# 会员充值
def rech(request):
    nickname = request.session.get('nickname')
    if nickname:
        if request.method == 'GET':
            return render(request,'rech.html')
        elif request.method == 'POST':
            card = request.POST['card']
            request.session['card'] = card
            try:
                user_info = Member.objects.get(card=card)
                name = user_info.name
                return HttpResponse(name)
            except:
                return HttpResponse(601)
    else:
        return render(request,'home.html')

# 充值服务
def rech_server(request):
    nickname = request.session.get('nickname')
    if nickname:
        if request.method == 'POST':
            card = request.session.get('card')
            num = int(request.POST['num'])
            try:
                info = Member.objects.get(card=card)
                info.money = info.money + num
                info.inte = info.inte + num
                info.save()
                try:
                    tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    Rechar.objects.create(card=card,money = num,tim = tim)
                    return HttpResponse('OK')
                except:
                    return HttpResponse(602)
            except:
                return HttpResponse(602)
    else:
        return render(request,'home.html')

# 会员消费
def consume(request):
    nickname = request.session.get('nickname')
    if nickname:

        if request.method == 'GET':
            return render(request,'consume.html')
        elif request.method == 'POST':
            card = request.POST['card']
            pwd = request.POST['pwd']
            try:
                info = Member.objects.get(card=card)
                request.session['card'] = card
            except:
                return HttpResponse(701)
            if not info:
                return HttpResponse(701)
            if pwd != info.pwd:
                return HttpResponse(702)
            return HttpResponse(info.name)
    else:
        return render(request,'home.html')

# 消费服务
def consume_server(request):
    nickname = request.session.get('nickname')
    if nickname:
        if request.method == 'POST':
            card = request.session.get('card')
            money = request.POST['money']
            try:
                info = Member.objects.get(card=card)
                if info.money >= int(money):
                    info.money = info.money - int(money)
                    info.save()
                else:
                    return HttpResponse(704)
                try:
                    tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    Consume.objects.create(card=card, money=money, tim=tim)

                except:
                    return HttpResponse(703)
            except:
                return HttpResponse(703)
            return HttpResponse('OK')
    else:
        return render(request,'home.html')

# 充值记录
def rech_record(request):
    nickname = request.session.get('nickname')
    if nickname:
        if request.method == 'GET':
            card = request.GET['card']
            try:
                data = Rechar.objects.filter(card=card)
                obj = []
                for i in data:
                    dic = {}
                    dic['card'] = i.card
                    dic['money'] = i.money
                    dic['tim'] = i.tim
                    obj.append(dic)
                return HttpResponse(json.dumps(obj))
            except:
                return HttpResponse(801)
    else:
        return render(request,'home.html')


# 消费记录
def con_record(request):
    nickname = request.session.get('nickname')
    if nickname:
        if request.method == 'GET':
            card = request.GET['card']
            try:
                data = Consume.objects.filter(card=card)
                obj = []
                for i in data:
                    dic = {}
                    dic['card'] = i.card
                    dic['money'] = i.money
                    dic['tim'] = i.tim
                    obj.append(dic)
                return HttpResponse(json.dumps(obj))
            except:
                return HttpResponse(801)
    else:
        return render(request,'home.html')

# 会员名单

def member_list(request):
    nickname = request.session.get('nickname')
    if nickname:
        if request.method == 'GET':
            try:
                info_list = Member.objects.all()
            except:
                return Http404
            data = []
            for info in info_list:
                item = {'card':info.card,
                        'phone':info.phone,
                        'name':info.name,
                        'gender':info.gender,
                        'bir':info.bir,
                        'inte':info.inte,
                        'money':info.money}
                data.append(item)
            return render(request,'member_list.html',locals())
    else:
        return render(request,'home.html')



























