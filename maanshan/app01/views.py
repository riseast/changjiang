from django.shortcuts import render,HttpResponse,reverse

# Create your views here.
from app01.models import ebook

import time
import datetime

# def dater(request):
#     # ctime=time.time()
#     date2=datetime.datetime.now().date()
#     # date4=date2.strftime("%Y-%m-%d").encode("utf-8")
#     return render(request,"time.html",{"date":date2})
#
#
#
#
# def timer(request):
#     ctime=time.time()
#
#     return render(request,"time.html",{"time":ctime})

def dt(request):
    date1=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    date2=datetime.datetime.now()+datetime.timedelta(hours=8)
    return render(request,"time.html",{"date":date1,"time":date2})


def login(request):
    print(request.method)
    if request.method=="GET":
        return render(request,"login.html")
    else:
        print(request.GET)
        print(request.POST)
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # return HttpResponse("OK")

        if user=="huangjj" and pwd=="123":

            return HttpResponse("登录成功")
        else:
            return HttpResponse("用户名或者密码错误")







def article_deatil(request,year,day,month):
    print(type(year))
    return HttpResponse(year+'-'+month+'-'+day)


# def article_detail(request,month,day,year):
#
#     return HttpResponse(year+month+day)

# from django.urls import reverse
def index(request):
    return HttpResponse(reverse("app01:index"))



def path_year(request,year):
    print(type(year))
    return HttpResponse("path_year")


def test_path(request):

    path = request.get_full_path()
    print(path)
    return render(request,'index.html',{'path1':path})



#过滤器

def date_t(request):
    now = datetime.datetime.now()

    return render(request,'index.html',{'now1':now})

from django import template
register=template.Library()





@register.filter
def chenfa(x,y):
    return x*y


def insert(request):
    #方式1
    #添加表记录
    # book_obj=ebook(id=1,tile='python',price=100,pub_date="2020-03-01",publish="人民出版社")
    # book_obj.save()

    #方式2
    #对于自增字段，如果执行过程中未执行成功，自增字段会跳过
    # ebook_obj=ebook.objects.create(tile='go',price=201,pub_date="2020-03-01",publish="北京出版社")
    # print(ebook.id)
    # print(ebook.price)
    # print(ebook.tile)
    # return HttpResponse("OK")

    # book_list=ebook.objects.all()
    # print(book_list)
    # book_list=ebook.objects.filter(price=100)
    # print(book_list)
    ret=ebook.objects.all().order_by("price")
    print(ret)
    return HttpResponse("Ok")