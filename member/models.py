from django.db import models

# Create your models here.
class Member(models.Model):
    #  卡号
    card = models.IntegerField(verbose_name='卡号',primary_key=True)
    # 手机号
    phone = models.CharField(verbose_name='手机号',max_length=11)
    # 姓名
    name = models.CharField(verbose_name='姓名',max_length=50)
    # 性别
    gender = models.CharField(verbose_name='性别',max_length=10)
    # 生日
    bir = models.CharField(verbose_name='生日',max_length=20,default=None)
    # 密码
    pwd = models.CharField(verbose_name='密码',max_length=30)
    # 积分
    inte = models.IntegerField(verbose_name='积分')
    # 余额
    money = models.IntegerField(verbose_name='余额')
    class Meta:
        db_table = 'member'

class Rechar(models.Model):
    # 卡号
    card = models.IntegerField(verbose_name='卡号')
    # 充值金额
    money = models.IntegerField(verbose_name='充值金额')
    # 充值时间
    tim = models.CharField(verbose_name='充值时间',max_length=50)
    class Meta:
        db_table = 'rechar'


#  消费
class Consume(models.Model):
    # 卡号
    card = models.IntegerField(verbose_name='卡号')
    # 消费金额
    money = models.IntegerField(verbose_name='消费金额')
    # 消费时间
    tim = models.CharField(verbose_name='消费时间',max_length=50)









