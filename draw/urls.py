from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # 👈 form shown on home
    path('entries/', views.view_entries, name='view_entries'),
    path('pick-winner/', views.pick_winner, name='pick_winner'),
    path('winner/', views.show_winner, name='show_winner'),
]
