from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_board, name='Home'),
    path('reports/', views.reports, name='Reports')

]
