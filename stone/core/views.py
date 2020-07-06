from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
)

from abc import ABC

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token 

from stone.core.forms import UserRegisterForm, ErrorForm
from stone.core.models import Error


User = get_user_model()


class ErrorABCView(ABC):
    model = Error
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['token'] = Token.objects.get_or_create(user=user)[0]
        return context


class ErrorListView(LoginRequiredMixin, ErrorABCView, ListView):
    template_name = 'core/home.html'
    context_object_name = 'errors'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filter_val = self.request.GET.get('enviroment')
        order = self.request.GET.get('orderby')
        if filter_val and order:
            queryset = Error.objects.filter(
                enviroment=filter_val
                ).order_by(f'{order}' if order == 'level' else f'-{order}')
        return queryset
   

class ErrorDetailView(LoginRequiredMixin, ErrorABCView, DetailView):
    template_name = 'core/error_detail.html'
    context_object_name = 'error'


class ErrorCreateView(LoginRequiredMixin, ErrorABCView, CreateView):
    template_name = 'core/error_create.html'
    context_object_name = 'error'
    form_class = ErrorForm

       
class ErrorUpdateView(LoginRequiredMixin, ErrorABCView, UpdateView):
    template_name = 'core/error_update.html'
    context_object_name = 'error'
    form_class = ErrorForm

  
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})


def delete_error_section(request, id=None):
    if request.method == 'POST':
        id_list = request.POST.getlist('error')
        for agent_id in id_list:
            Error.objects.get(id=agent_id).delete()
    return redirect('core:error-home')