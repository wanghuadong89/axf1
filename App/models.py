from django.db import models

# Create your models here.

class Common(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract = True #抽象类 而不是表的模型

#轮波图
class Wheel(Common):
    class Meta:
        db_table = 'axf_wheel'


#每日必抢
class Nav(Common):
    class Meta:
        db_table = 'axf_nav'

#必买
class MustBuy(Common):
    class Meta:
        db_table = 'axf_mustbuy'

#首页中间的商品图片
class Shop(Common):
    class Meta:
        db_table = 'axf_shop'

#首页下面的商品展示
class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=200)
    categoryid = models.CharField(max_length=200)
    brandname = models.CharField(max_length=200)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=200)
    productid1 = models.CharField(max_length=200)
    longname1 = models.CharField(max_length=200)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=200)
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=200)
    productid2 = models.CharField(max_length=200)
    longname2 = models.CharField(max_length=200)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=200)
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=200)
    productid3 = models.CharField(max_length=200)
    longname3 = models.CharField(max_length=200)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)
    class Meta:
        db_table = 'axf_mainshow'

#商品类别
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=7)
    typename = models.CharField(max_length=10)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()
    class Meta:
        db_table = 'axf_foodtypes'
"""
商品表：
商品id(productid)        118826
图片(productimg)      http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q
名字(productname)    爱鲜蜂·海南千禧果
长名字(productlongname)   爱鲜蜂·海南千禧果400-450g/盒
是否精选(isxf)    1
是否买一增一(pmdesc)   1
规格(specifics)
价格(price)         13.80
原价(marketprice)     13.8
商品组id(categoryid)       103532
商品子组id(childcid)      103533
商品子组名名称(childcidname)   国产水果
详情页id(dealerid)       4858
库存(storenums)     7
销量(productnum)
"""
class Goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=100)
    isxf = models.BooleanField(default=False)
    pmdesc = models.BooleanField(default=False)
    specifics = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    marketprice = models.CharField(max_length=10)
    categoryid = models.CharField(max_length=10)
    childcid = models.CharField(max_length=10)
    childcidname = models.CharField(max_length=20)
    dealerid = models.CharField(max_length=10)
    storenums = models.CharField(max_length=20)
    productnum = models.CharField(max_length=20)
    class Meta:
        db_table = 'axf_goods'

