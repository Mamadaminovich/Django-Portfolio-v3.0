from django.shortcuts import render
from .models import *
# Create your views here.
def home(context):
    return render(context, "index.html", {})
def component(context):
    return render(context, "components.html", {})