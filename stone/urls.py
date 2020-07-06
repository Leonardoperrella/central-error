
from django.contrib import admin
from django.urls import path, include
from stone.core.views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('stone.core.urls')),
    path('api/', include('stone.api.urls')),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]
