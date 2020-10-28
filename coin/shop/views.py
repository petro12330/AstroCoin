from django.shortcuts import render

def shop(request):
    return render(request, 'shop/shop.html')

def basket(request):
    return render(request, 'shop/basket.html')