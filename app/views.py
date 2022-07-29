from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import wikipedia
wikipedia.set_lang('uz')
# Create your views here.
def home(request):
    return HttpResponse('Salom,bu mening birinchi web sahifam!')
def university(request):
    return HttpResponse('This is TUIT')
def say_hello(request,ism):
    return HttpResponse(f'<strong>hello {ism}</strong>')
def calculator(request,a,b):
    c = a+b
    return HttpResponse(f'{a} + {b} = {c}') 
def json(request):
    lugat = {
        'hello':'salom',
        'come':'kelmoq'
    }
    return JsonResponse(lugat,safe=False)
def wiki(request,key):
    result = wikipedia.summary(key)
    return HttpResponse(result)