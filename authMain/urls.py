from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='auth.index'),
    path('login/', login, name='auth.login'),
    path('register/', register, name='auth.register'),
    path('logout/', logout, name='auth.logout'),

]
