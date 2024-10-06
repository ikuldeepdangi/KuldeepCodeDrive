from django.contrib import admin
from django.urls import path
from main import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_home, name='main_home'),  
    path('tableapp/', include('tableapp.urls')),
]
