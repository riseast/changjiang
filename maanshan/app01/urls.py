# from django.contrib import admin


from django.urls import path,re_path


from app01 import views

urlpatterns = [
    path('login/', views.login),
    path('dt/', views.dt),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_deatil),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
]





