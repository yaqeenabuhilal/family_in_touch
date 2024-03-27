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
    path('sign_up_parent/', views.sign_up_parent, name='sign_up_parent'),
    path('feedback_parent/',views.feedback_parent,name='feedback_parent'),
    path('feedback_teenger/', views.feedback_teenger, name='feedback_teenger'),
    path('feedback_psy_teenger/', views.feedback_psy_teenger, name='feedback_psy_teenger'),
    path('feedback_psy_parent/', views.feedback_psy_parent, name='feedback_psy_parent'),
    path('summary_psy/', views.summary_psy, name='summary_psy'),
    path('testerforfeed/', views.testerforfeed, name='testerforfeed'),
    path('drop_down_list_psy/', views.drop_down_list_psy, name='drop_down_list_psy'),

]
# loginParent