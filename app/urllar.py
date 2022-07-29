from django.urls import path
from .views import home,university,say_hello,calculator,json,wiki
urlpatterns = [
    path('home',home),
    path('university',university),
    path('hello/<str:ism>',say_hello),
    path('calc/<int:a>/<int:b>',calculator),
    path('json',json),
    path('wikipedia/<str:key>',wiki)
]
