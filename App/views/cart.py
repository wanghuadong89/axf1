from django.shortcuts import render,HttpResponse

# Create your views here.
def cart(req):
    return render(req,'cart.html')