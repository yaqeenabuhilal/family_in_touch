from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name="dashbord"),
    path('feedback/', views.feedback),
    path('link/', views.link),
    path('loginTeenager/', views.loginTeenager, name='loginTeenager'),
    path('test/', views.test),
    path('aaa/', views.aaa),
    path('singupteenger/', views.singupteenager, name='singupteenger'),

    path('loginParent/', views.loginParent, name='loginParent'),
    path('sign_up_parent/', views.sign_up_parent, name='sign_up_parent'),
    path('navbarforpsy/', views.navbarforpsy, name='navbarforpsy'),
    path('homepageforpsy/', views.homepageforpsy, name='homepageforpsy'),
    path('homepage_parent/', views.homepage_parent, name='homepage_parent'),
    path('homepage_teenager/', views.homepage_teenager, name='homepage_teenager'),
    path('profile/', views.profile, name='profile'),
    path('login_psy/', views.login_psy, name='login_psy'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
