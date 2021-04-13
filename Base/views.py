from django.shortcuts import render

def index(request):
    return render(request,'Base/index.html')

def main(request):
    return render(request,'Base/main.html')
