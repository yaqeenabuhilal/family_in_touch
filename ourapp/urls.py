from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="dashbord"),
    path('feedback/', views.feedback),
    path('link/', views.link),
    path('loginTeenager/', views.loginTeenager, name='loginTeenager'),
    path('test/', views.test),
    path('aaa/', views.aaa),
    path('singupteenger/', views.singupteenager, name='singupteenger'),

    path('loginParent/', views.loginParent, name='loginParent'),
    path('loginpsychologist/', views.loginpsychologist, name='loginpsychologist'),
    path('sign_up_parent/', views.sign_up_parent, name='sign_up_parent'),
    path('navbarforpsy/', views.navbarforpsy, name='navbarforpsy'),
    path('loginpsychologist/homepageforpsy', views.homepageforpsy, name='homepageforpsy'),
    path('homepage_parent/', views.homepage_parent, name='homepage_parent'),
    path('homepage_teenager/', views.homepage_teenager, name='homepage_teenager'),

]
# loginParent