from django.urls import path
from . import views

app_name = 'credit_card_defaulters'

urlpatterns = [
    path('', views.home, name='home'),

]
