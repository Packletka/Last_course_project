from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('Akame_ga_Kill', views.Akame_ga_Kill, name='Akame_ga_Kill'),
    path('konoSuba', views.konoSuba, name='konoSuba'),
    path('Future_Diary', views.Future_Diary, name='Future_Diary'),
    path('OnePunchMan', views.OnePunchMan, name='OnePunchMan'),
    path('Noragami', views.Noragami, name='Noragami'),
    path('Sword_Art_Online', views.Sword_Art_Online, name='Sword_Art_Online'),
    path('No_game_No_Life', views.No_game_No_Life, name='No_game_No_Life'),
    path('all_comments', views.all_comments, name="all_comments"),
    path('create', views.create, name="create")
]
