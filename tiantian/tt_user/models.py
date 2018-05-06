from django.db import models

# Create your models here.

# 创建用户信息表
class useerInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    postcode = models.CharField(max_length=6)
    recipients = models.CharField(max_length=10)
