from django.contrib import admin
from django.urls import path, include

from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('dashboard/', views.info_fun),

    # path('dashboard/', views.reporter_fun),
    # path('dashboard/', views.scammer_fun),
]
