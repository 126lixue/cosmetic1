from django.db import models



class Cart(models.Model):
    user=models.ForeignKey('c_user.User',None)
    goods=models.ForeignKey('c_goods.GoodInfo',None)
    count=models.IntegerField(default=0)


