from django.shortcuts import render,redirect
from .models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodType,Goods,User,Cart,Order
from django.http import JsonResponse
import time
import random
from django.conf import settings
import os
# Create your views here.


def base(request):
    return render(request,'axf/base.html')

def home(request):
    wheelsList=Wheel.objects.all()
    navList=Nav.objects.all()
    mustbuyList=Mustbuy.objects.all()
    shopList=Shop.objects.all()
    shop1=shopList[0]
    shop2=shopList[1:3]
    shop3=shopList[3:7]
    shop4=shopList[7:11]
    
    mainList=MainShow.objects.all()
    return render(request,'axf/home.html',{
            'title':'home','wheelsList':wheelsList,'navList':navList,'mustbuyList':mustbuyList,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,'mainList':mainList 
            })

def market(request,categoryid_id,cid,sortid):
    leftSlider=FoodType.objects.all()
    if cid=='0':
        productList=Goods.objects.filter(categoryid_id=categoryid_id)
    else:
        productList=Goods.objects.filter(categoryid_id=categoryid_id,childcid=cid)
    
    #排序
    if sortid =='1':
        productList=productList.order_by('productnum')
    elif sortid=='2':
        productList=productList.order_by('price')
    elif sortid=='3':
        productList=productList.order_by('-price')
    
    
    
    
    group = leftSlider.get(typeid=categoryid_id)
    childList=[]
    
    childnames=group.childtypenames
    arr1=childnames.split('#')
    for str in arr1:
        arr2=str.split(':')
        obj={'childName':arr2[0],'childId':arr2[1]}
        childList.append(obj)
    
    
    cartlist=[]
    token = request.session.get('token')
    if token:
        user=User.objects.get(userToken=token)
        cartlist=Cart.objects.filter(userAccount=user.userAccount)
    
    for p in productList:
        for c in cartlist:
            if c.productid == p.productid:
                p.num=c.productnum
                continue
        
        
        
    return render(request,'axf/market.html',{'title':'market','leftSlider':leftSlider,'productList':productList,'childList':childList,'categoryid_id':categoryid_id,'cid':cid,"cartlist":cartlist,})

#购物车
def cart(request):
    cartslist=[]    
    token=request.session.get('token')
    if token != None:
        user=User.objects.get(userToken=token)
        cartslist=Cart.objects.filter(userAccount=user.userAccount)
        












    return render(request,'axf/cart.html',{'title':'cart',"cartslist":cartslist})

#修改购物车
def changecart(request,flag):
    #判断用户是否登录
    token=request.session.get('token')
    if token == None:
        #没登录
#        print('没登陆')
        return JsonResponse({'data':-1,'status':'error'})
    
    productid=request.POST.get('productid')
    product=Goods.objects.get(productid=productid)
    user=User.objects.get(userToken=token)

#增加订单
    if flag=='0':
        if product.storenums ==0:
                return JsonResponse({'data':-2,'status':'error'})
        carts=Cart.objects.filter(userAccount=user.userAccount)
        c=None
        if carts.count()==0:
            #直接增加一单订单
            c = Cart.createcart(user.userAccount,productid,1,product.price,True,product.productimg,product.productlongname,False)
            c.save()
            pass
        else:
            try:
                c=carts.get(productid=productid)
                #修改数量和价格
                c.productnum +=1
                c.productprice ='%.2f'%(float(product.price) * c.productnum)
                c.save()
                
            except Cart.DoesNotExist as e:
                #直接增加一条订单
                c = Cart.createcart(user.userAccount,productid,1,product.price,True,product.productimg,product.productlongname,False)
                c.save()
        #库存减一
        
        product.storenums -=1
        product.save()
        return JsonResponse({'data':c.productnum,'price':c.productprice,'status':'success'})                
 


#减少订单               
    elif flag=='1':
        carts=Cart.objects.filter(userAccount=user.userAccount)
        c=None
        if carts.count()==0:
            return JsonResponse({'data':-2,'status':'error'})
            pass
        else:
            try:
                c=carts.get(productid=productid)
                #修改数量和价格
                c.productnum -=1
                c.productprice ='%.2f'%(float(product.price) * c.productnum)
                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()
                
            except Cart.DoesNotExist as e:
                return JsonResponse({'data':-2,'status':'error'})
        #库存减一
        
        product.storenums +=1
        product.save()
        return JsonResponse({'data':c.productnum,'price':c.productprice,'status':'success'})

    elif flag=='2':
        carts=Cart.objects.filter(userAccount=user.userAccount)
        c=carts.get(productid=productid)
        c.isChose = not c.isChose
        c.save()
        str=' '
        if c.isChose:
            str='✓'
        return JsonResponse({'data':str,'status':'success'})

#    elif flag =='3':
#        pass
        





def mine(request):
    username=request.session.get('username','未登录')
    return render(request,'axf/mine.html',{'title':'mine','username':username})

from .forms.login import LoginForm

from django.http import HttpResponse


#登入
def login(request):
    if request.method=='POST':
        f=LoginForm(request.POST)
        if f.is_valid():
            #信息格式没多大问题，验证账号和密码的正确性

            nameid=f.cleaned_data.get('username')
            passwd=f.cleaned_data.get('passwd')
            
            try:
                user=User.objects.get(userAccount=nameid)
                if user.userPasswd != passwd:
                    #错误信息
                    return redirect('/login/')
            except User.DoesNotExist as e:
                return redirect('/login/')

            #登入成功
#            print('登入成功')
            token=time.time()+random.randrange(1,100000)
            user.userToken=str(token)
            user.save()
            request.session['username']=user.userName
            request.session['token']=user.userToken           
            return redirect('/mine/')
                
        else:
            return render(request,'axf/login.html',{'title':'登入','form':f,'error':f.errors})
    else:
        f=LoginForm()
        return render(request,'axf/login.html',{'title':'登入','form':f})


#注册

def register(request):
    if request.method=='POST':
        userAccount=request.POST.get('userAccount')
        userPasswd=request.POST.get('userPass')
        userName =request.POST.get('userName')
        userPhone =request.POST.get('userPhone')
        userAdderss =request.POST.get('userAdderss')
        userRank =0   
        
        token=time.time()+random.randrange(1,100000)
        userToken=str(token)
        f=request.FILES['userImg']
        userImg=os.path.join(settings.MDEIA_ROOT,userAccount+'.png')
        with open(userImg,'wb') as fp:
            for data in f.chunks():
                fp.write(data)
        user=User.createuser(userAccount,userPasswd,userName,userPhone,userAdderss,userImg,userRank,userToken)
        #保存到数据库
        user.save()
        
        #存sessions
        request.session['username']=userName
        request.session['token']=userToken        
        
        return redirect('/mine/')
    
    else:
        return render(request,'axf/register.html',{'title':'注册'})

#验证账号
def checkuserid(request):
    userid =request.POST.get('userid')
    try:
        user=User.objects.get(userAccount=userid)
        return JsonResponse({'data':'该用户已经被注册','status':'error'})
    except User.DoesNotExist as e:
        return JsonResponse({'data':'可以注册','status':'success'})
        
#退出登录
from django.contrib.auth import logout
def quit(request):
#    request.session.clear()
    logout(request)
    return redirect('/mine/')



def saveorder(request):
    #判断用户是否登录
    token=request.session.get('token')
    if token == None:
        #没登录
#        print('没登陆')
        return JsonResponse({'data':-1,'status':'error'})
    
    user=User.objects.get(userToken=token)
    carts=Cart.objects.filter(isChose=True)
    if carts.count()==0:
        return JsonResponse({'data':-1,'status':'error'})
    
    oid= time.time()+random.randrange(1,10000)
    oid = '%d'%oid
    o=Order.createorder(oid,user.userAccount,0)
    o.save()
    
    for item in carts:
        item.isDelete=True
        item.orderid=oid
        item.save()
    return JsonResponse({'status':'success'})        