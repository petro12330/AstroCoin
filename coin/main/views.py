from django.shortcuts import render



def home(request):
    return render(request, 'main/home.html')

def get(request):
    return render(request, 'main/get.html')





