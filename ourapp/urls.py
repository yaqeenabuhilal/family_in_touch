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


    path('choicelinktopic_teenageer/',views.choicelinktopic_teenager, name='choicelinktopic_teenageer'),
    path('behavioral_challenges_ten/', views.behavioral_challenges_ten, name='behavioral_challenges_ten'),
    path('communication_challenges_ten/', views.communication_challenges_ten, name='communication_challenges_ten'),
    path('emotional_support_ten/', views.emotional_support_ten, name='emotional_support_ten'),


    path('choicelinktopic_parent/', views.choicelinktopic_parent, name='choicelinktopic_parent'),
    path('behavioral_challenges_par/', views.behavioral_challenges_par, name='behavioral_challenges_par'),
    path('communication_challenges_par/', views.communication_challenges_par, name='communication_challenges_par'),
    path('time_management_par/', views.time_management_par, name='time_management_par'),

    path('choicelinktopic_psy_par/', views.choicelinktopic_psy_par, name='choicelinktopic_psy_par'),
    path('choicelinktopic_psy_ten/', views.choicelinktopic_psy_ten, name='choicelinktopic_psy_ten'),

    path('post_e_s_ten/', views.post_e_s_ten, name='post_e_s_ten'),
    path('post_c_ch_ten/', views.post_c_ch_ten, name='post_c_ch_ten'),
    path('post_b_ch_ten/', views.post_b_ch_ten, name='post_b_ch_ten'),

    path('post_t_m_par/', views.post_t_m_par, name='post_t_m_par'),
    path('post_c_ch_par/', views.post_c_ch_par, name='post_c_ch_par'),
    path('post_b_ch_par/', views.post_b_ch_par, name='post_b_ch_par'),

    path('view_links_psy_par/', views.view_links_psy_par, name='view_links_psy_par'),
    path('delete_link_psy_par/<int:link_id>/', views.delete_link_psy_par, name='delete_link_psy_par'),
    path('view_links_psy_ten/', views.view_links_psy_ten, name='view_links_psy_ten'),
    path('delete_link_psy_ten/<int:link_id>/', views.delete_link_psy_ten, name='delete_link_psy_ten'),

    path('thank_you_page/', views.thank_you_page, name='thank_you_page')
]
# loginParent