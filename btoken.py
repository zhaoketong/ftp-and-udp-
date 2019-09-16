# import time
# import jwt
#
#
# def make_token(nickname, expire=3600 * 24):
#     '''
#     生成token
#     :param username:
#     :param expire:
#     :return:
#     '''
#
#     key = 'abcdef1234'
#     now_t = time.time()
#     payload = {'username': nickname, 'exp': int(now_t + expire)}
#     return jwt.encode(payload, key, algorithm='HS256')
#
from django.http import HttpResponseRedirect
print(dir(HttpResponseRedirect))


# < !-- if (data == 401)
# {-->
# < !--$('#sp_card').html = '账号输入错误' -->
# < !--} else if (data == 402){-->
# < !--$('#sp_phone').html='手机号输入有误'-->
# < !--} else if (data == 403){-->
# < !--$('#sp_name').html = '姓名输入有误'-->
# < !--} else if (data == 404){-->
# < !--$('#sp_gender').html = '性别选择有误'-->
# < !--} else if (data == 405){-->
# < !--$('#sp_birthday').html = '生日输入有误'-->
# < !--} else if (data == 406){-->
# < !--$('#sp_pwd1').html = '密码输入有误'-->
# < !--} else if (data == 407){-->
# < !--$('#sp_pwd2').html = '密码二次输入有误'-->
# < !--} else if (data == 409){-->
# < !--alert('该账号已存在')-->
# < !--location.href='http://127.0.0.1:8080/member/reg'-->
# < !--} else if (data == 408){-->
# < !--alert('两次密码不一致')-->
# < !--location.href='http://127.0.0.1:8080/member/reg'-->
# < !--} else if (data == 410){-->
# < !--alert('注册成功')-->
# < !--location.href='http://127.0.0.1:8080/member/info'-->
# < !--} else if (data == 411){-->
# < !--alert('注册失败')-->
# < !--location.href='http://127.0.0.1:8080/member/reg'-->
# < !--}-->








