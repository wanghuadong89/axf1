from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/$', home.home,name='home'),
    url(r'^market/$', market.market,name='market'),
    url(r'^cart/$', cart.cart,name='cart'),
    url(r'^mine/$', mine.mine,name='mine'),
]