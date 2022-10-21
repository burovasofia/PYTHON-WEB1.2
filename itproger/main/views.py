from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h4>Проверка работа</h4>")

def about(request):
    return HttpResponse("<h4>Про нас</h4>")