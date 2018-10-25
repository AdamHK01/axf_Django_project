from django.contrib import admin
from django.urls import path,re_path
from . import views


urlpatterns = [
    path('home/',views.home,name='home'),
    re_path('market/(\d+)/(\d+)/(\d+)/',views.market,name='market'),
    path('cart/',views.cart,name='cart'),
    path('mine/',views.mine,name='mine'),
    path('base/',views.base),
    
    
    #登入
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    
    #验证账号是否被注册
    path('checkuserid/',views.checkuserid,name='checkuserid'),
    #退出登录
    path('quit/',views.quit,name='quit'),
    #修改购物车
    re_path('changecart/(\d+)/',views.changecart,name='changecart'),
    #下订单
    path('saveorder/',views.saveorder,name='saveorder')
    
    
]
