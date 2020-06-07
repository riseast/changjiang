from django.shortcuts import render,HttpResponse,reverse
from app01.models import ebook

# Create your views here.
# from django.urls import reverse

def index(request):


    return HttpResponse(reverse("app02:index"))



