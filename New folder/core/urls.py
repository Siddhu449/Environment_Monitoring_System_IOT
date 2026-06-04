
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
path('about/', views.about_view, name='about'),
path('contact/', views.contact_view, name='contact'),
path('signup/', views.signup_view, name='signup'),
path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),

path('match_setup/', views.match_setup_view, name='match_setup'),
path('match_history/', views.match_history, name='match_history'),

path('match/<int:match_id>/', views.match_detail, name='match_detail'),
path('match/<int:match_id>/delete/', views.delete_match, name='delete_match'),
path('save_match/', views.save_match, name='save_match'),


]

    
   
      


