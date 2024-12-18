from django.urls import path
from GameGuides import views

app_name = 'gameguides'

urlpatterns = [
    path('', views.gameguides_home_view, name='game_guides_home'),
    path('hsr_banner_history/', views.hsr_banner_history_view, name='hsr_banner_history'),
    path('survivorio_clans/', views.survivorio_clans_view, name='survivorio_clans'),
    path('survivorio_gear/', views.survivorio_gear_view, name='survivorio_gear'),
    path('survivorio_maps/', views.survivorio_map_types_bosses_view, name='survivorio_maps'),
    path('survivorio_pets/', views.survivorio_pets_view, name='survivorio_pets'),
    path('survivorio_survivors/', views.survivorio_survivors_view, name='survivorio_survivors'),
    path('survivorio_merging/', views.survivorio_merging_view, name='survivorio_merging'),
]