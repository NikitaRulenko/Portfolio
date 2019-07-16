from django.urls import path

from . import views


app_name = "radio"

urlpatterns = [
    path('api/v1/radio/', views.getpost_all_radio, name='getpost_all_radio'),
    path('api/v1/radio/<int:pk>', views.getputdelete_one_radio, name='getputdelete_one_radio'),
]