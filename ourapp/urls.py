from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.official_homepage, name="official_homepage"),
    path('feedback/', views.feedback),
    path('link/', views.link),
    path('loginTeenager/', views.loginTeenager, name='loginTeenager'),
    path('test/', views.test),
    path('aaa/', views.aaa),
    path('singupteenger/', views.singupteenager, name='singupteenger'),
    path('loginParent/', views.loginParent, name='loginParent'),
    path('navbarforpsy/', views.navbarforpsy, name='navbarforpsy'),
    path('homepageforpsy/', views.homepageforpsy, name='homepageforpsy'),
    path('homepage_parent/', views.homepage_parent, name='homepage_parent'),
    path('homepage_teenager/', views.homepage_teenager, name='homepage_teenager'),
    path('profile/', views.profile, name='profile'),
    path('profileforparent/', views.profileforparent, name='profileforparent'),
    path('profileforteenager/', views.profileforteenager, name='profileforteenager'),
    path('login_psy/', views.login_psy, name='login_psy'),
    path('sign_up_parent/', views.sign_up_parent, name='sign_up_parent'),
    path('feedback_psy_teenger/', views.feedback_psy_teenger, name='feedback_psy_teenger'),
    path('feedback_psy_parent/', views.feedback_psy_parent, name='feedback_psy_parent'),
    path('summary_psy/', views.summary_psy, name='summary_psy'),
    path('testerforfeed/', views.testerforfeed, name='testerforfeed'),
    path('drop_down_list_psy/', views.drop_down_list_psy, name='drop_down_list_psy'),
    path('abes_contact_us/', views.abes_contact_us, name='abes_contact_us'),
    path('sammaryforparent/', views.sammaryforparent, name='sammaryforparent'),    path('sammaryforteenger/<str:teenger_id>/', views.sammaryforteenger, name='sammaryforteenger'),
    path('feedback_teenger/', views.add_teenger_feedback, name='feedback_teenger'),
    path('feedback_parent/', views.add_parent_feedback, name='feedback_parent'),
    path('send_sammary_to_parent/<str:username>/<str:date>/', views.add_send_sammary_to_parent, name='send_sammary_to_parent'),
    path('send_sammary_to_teen/<str:username>/<str:date>/', views.add_send_sammary_to_teen, name='send_sammary_to_teen'),
    path('list_of_teenger/', views.view_list_of_teenger, name='list_of_teenger'),
    path('list_of_parent/', views.view_list_of_parent, name='list_of_parent'),
    path('navbar_parent/', views.navbar_parent, name='navbar_parent'),
    path('navbar_teenager/', views.navbar_teenager, name='navbar_teenager'),
    path('official_homepage/', views.official_homepage, name='official_homepage'),
    path('About/', views.About, name='About'),
    path('contact_parent/', views.contact_parent, name='contact_parent'),
    path('contact_teens/', views.contact_teens, name='contact_teens'),
    path('logout/', views.logout, name='logout'),


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

    path('thank_you_page/', views.thank_you_page, name='thank_you_page'),
    path('error_parent/', views.error_parent, name='error_parent'),
    path('error_teenger/', views.error_teenger, name='error_teenger'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
