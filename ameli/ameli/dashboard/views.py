from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')

def network(request):
    return render(request,'dashboard/network.html')

def suggestion(request):
    return render(request,'dashboard/suggestion.html')

def insight(request):
    return render(request,'dashboard/insight.html')

def attachment(request):
    return render(request,'dashboard/attachment.html')            
