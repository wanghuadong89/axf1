from django.shortcuts import render,HttpResponse

# Create your views here.
def market(req):
    return render(req,'market.html')