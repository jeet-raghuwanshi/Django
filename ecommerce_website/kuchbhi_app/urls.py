from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('kuchbhiapp/',views.kuchbhi_app_say_hello),
    path('kuchbhiapp/hello/',views.kuchbhi_app_hello_say_hello),
    path('hello_page',views.hello_using_render)
]