from django.shortcuts import render

# Create your views here.


def merchantStore (request):
    return render(request,'merchantTemplate/merchantStore.html',{})