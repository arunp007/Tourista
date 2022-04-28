from django.urls import path
from.import views

urlpatterns = [
    path('home',views.home),
    path('log',views.log),
    path('signup',views.signup)
]