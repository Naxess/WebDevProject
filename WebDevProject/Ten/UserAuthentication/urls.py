from django.urls import path
from UserAuthentication import views

app_name = 'user_auth'

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user_roster/', views.user_roster_view, name='user_roster')
]