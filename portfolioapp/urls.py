from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('component/', component, name='component'),
]