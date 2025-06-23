from django.urls import path
from .views import create_admin_user
from . import views
from .views import create_admin_user

urlpatterns = [
    path('', views.register, name='register'),  # 👈 form shown on home
    path('entries/', views.view_entries, name='view_entries'),
    path('create-admin/', create_admin_user),
    path('pick-winner/', views.pick_winner, name='pick_winner'),
    path('winner/', views.show_winner, name='show_winner'),
]
