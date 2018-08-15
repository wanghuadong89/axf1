from django.shortcuts import render,HttpResponse
from App.models import Wheel,Nav,MustBuy,Shop,MainShow
# Create your views here.
def home(req):
    wheel = Wheel.objects.all() #轮波图
    nav = Nav.objects.all() #每日必抢
    mustbuy = MustBuy.objects.all() #酸奶女王
    shop = Shop.objects.all()
    shop1 = shop[0]
    shop2 = shop[1:3]
    shop3 = shop[3:7]
    shop4 = shop[7:11]
    mainShow = MainShow.objects.all()
    return render(req,'home.html',{'wheel':wheel,'nav':nav,'mustbuy':mustbuy,'shop1':shop1,'shop2':shop2,'shop3':shop3,'shop4':shop4,'mainshow':mainShow})
    # return render(req,'home.html',{'wheel':wheel})