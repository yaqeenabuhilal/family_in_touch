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
    path('feedback_psy_teenger/', views.feedback_psy_teenger, name='feedback_psy_teenger'),
    path('feedback_psy_parent/', views.feedback_psy_parent, name='feedback_psy_parent'),
    path('summary_psy/', views.summary_psy, name='summary_psy'),
    path('testerforfeed/', views.testerforfeed, name='testerforfeed'),
    path('drop_down_list_psy/', views.drop_down_list_psy, name='drop_down_list_psy'),
    path('abes_contact_us/', views.abes_contact_us, name='abes_contact_us'),
    path('sammaryforparent/<str:parent_id>/', views.sammaryforparent, name='sammaryforparent'),
    path('sammaryforteenger/<str:teenger_id>/', views.sammaryforteenger, name='sammaryforteenger'),
    path('feedback_teenger/', views.add_teenger_feedback, name='feedback_teenger'),
    path('feedback_parent/', views.add_parent_feedback, name='feedback_parent'),
    path('send_sammary_to_parent/<str:username>/<str:date>/', views.add_send_sammary_to_parent, name='send_sammary_to_parent'),
    path('send_sammary_to_teen/<str:username>/<str:date>/', views.add_send_sammary_to_teen, name='send_sammary_to_teen'),
    path('list_of_teenger/', views.view_list_of_teenger, name='list_of_teenger'),
    path('list_of_parent/', views.view_list_of_parent, name='list_of_parent'),

]
