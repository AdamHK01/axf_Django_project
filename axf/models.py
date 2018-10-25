from django.db import models

# Create your models here.


class Wheel(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)



class Nav(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)
    
class Mustbuy(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)    

class Shop(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)   

class MainShow(models.Model):
    trackid=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    img=models.CharField(max_length=150)
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=1)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField(default=0)
    marketprice2 = models.FloatField(default=1)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField(default=0)
    marketprice3 = models.FloatField(default=1)

#分类模型
class FoodType(models.Model):
    typeid = models.CharField(max_length=16)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)
    class Meta:
        db_table = "axf_foodtypes"

#商品模型
class Goods(models.Model):
    productid = models.CharField(max_length=16)   # 商品的id
    productimg = models.CharField(max_length=200)   #商品的图片
    productname = models.CharField(max_length=100)   # 商品的名称
    productlongname = models.CharField(max_length=200)  # 商品的规格
    isxf = models.IntegerField(default=1)   #是否精选
    pmdesc = models.CharField(max_length=100)  #是否买一赠一
    specifics = models.CharField(max_length=100)   # 规格
    price = models.FloatField(default=0)   # 折后价格
    marketprice = models.FloatField(default=1)  #  原价
    categoryid_id = models.CharField(max_length=16)   # 分类id
    childcid = models.CharField(max_length=16)   # 子分类id
    childcidname = models.CharField(max_length=100)  # 名称
    dealerid = models.CharField(max_length=16) #详情页
    storenums = models.IntegerField(default=1)  #库存
    productnum = models.IntegerField(default=1)  # 销量排序
    onSale=models.BooleanField()
    
#用户模型类
    
class User(models.Model):
    #用户账号 唯一
    userAccount =  models.CharField(max_length=20,unique=True)
    #密码
    userPasswd  =  models.CharField(max_length=20)
    #昵称
    userName    =  models.CharField(max_length=20)
    #手机号
    userPhone   =  models.CharField(max_length=20)
    #地址
    userAdderss  =  models.CharField(max_length=100)
    #头像路径
    userImg     =  models.CharField(max_length=150)
    #等级
    userRank    =  models.IntegerField()
    #token验证值,每次登入后都更新
    userToken   =  models.CharField(max_length=50)
    @classmethod
    def createuser(cls,account,passwd,name,phone,address,img,rank,token):
        u=cls(userAccount=account,userPasswd=passwd,userName=name,userPhone=phone,
              userAdderss=address,userImg=img,userRank=rank,userToken=token)
        return u


class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isDelete=False)

class Cart(models.Model):
    userAccount=models.CharField(max_length=20)
    productid=models.CharField(max_length=10)
    productnum=models.IntegerField()
    productprice=models.CharField(max_length=10)
    isChose=models.BooleanField(default=True)
    productimg=models.CharField(max_length=150)
    productname=models.CharField(max_length=100)
    orderid=models.CharField(max_length=20,default='0')
    isDelete=models.BooleanField(default=False)
    objects=CartManager1()
    @classmethod
    def createcart(cls,userAccount,productid,productnum,productprice,isChose,productimg,productname,isDelete):
        c=cls(userAccount=userAccount,productid=productid,productnum=productnum,productprice=productprice,isChose=isChose,productimg=productimg,productname=productname,isDelete=isDelete)
        return c
    
    
    
    
class Order(models.Model):
    orderid = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    progress=models.IntegerField()
    
    @classmethod
    def createorder(cls,orderid,userid,progress):
        o=cls(orderid=orderid,userid=userid,progress=progress)
        return o
    
    
    
    
    
    
    
    
    
    