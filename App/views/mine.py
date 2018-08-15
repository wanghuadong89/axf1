from django.shortcuts import render,HttpResponse

# Create your views here.
def mine(req):
    return render(req,'mine.html')