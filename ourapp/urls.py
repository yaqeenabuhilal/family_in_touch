from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="dashbord"),
    path('feedback/', views.feedback),
    path('link/', views.link),
    path('loginTeenager/', views.loginTeenager,name='loginTeenager'),
    path('test/', views.test),
    path('aaa/', views.aaa),
    path('singupteenger/', views.singupteenager,name='singupteenger'),
    path('loginParent/', views.loginParent, name='loginParent'),
    path('loginpsychologist/', views.loginpsychologist, name='loginpsychologist'),
]