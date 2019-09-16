from django.db import models

# Create your models here.
class Users(models.Model):
    account = models.IntegerField(verbose_name='账号',primary_key=True)
    nickname = models.CharField(max_length=11,verbose_name='昵称')
    password = models.CharField(max_length=50,verbose_name='密码')

    class Meta:
        db_table = 'user'