from django.urls import path, include
from stone.core.views import (
    register,
    delete_error_section,
    ErrorListView,
    ErrorDetailView,
    ErrorCreateView,
    ErrorUpdateView)


app_name = 'core'

urlpatterns = [
    path('', ErrorListView.as_view(), name='error-home'),
    path('detail/<int:pk>/', ErrorDetailView.as_view(), name='error-detail'),
    path('create/', ErrorCreateView.as_view(), name='error-create'),
    path('update/<int:pk>/', ErrorUpdateView.as_view(), name='error-update'),
    path('delete-error-section/', delete_error_section, name='error-delete-section'),

 
]
