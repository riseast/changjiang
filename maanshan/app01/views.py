from django.shortcuts import render,HttpResponse

# Create your views here.


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
    return HttpResponse(year+'-'+month+'-'+day)


# def article_detail(request,month,day,year):
#
#     return HttpResponse(year+month+day)


