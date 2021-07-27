from django.conf.urls import url
from django.urls import path
from downtube import views

urlpatterns = [
    path('',views.youtube),
]
