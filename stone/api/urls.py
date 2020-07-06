from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from stone.router import router


urlpatterns = [
    path('', include(router.urls)),
    path('token/', obtain_auth_token),
    
]