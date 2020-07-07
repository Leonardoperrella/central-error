from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import resolve_url as r
from stone.core.managers import CustomUserManager


ENVIROMENTS = [
    ('production', 'production'),
    ('homologation', 'homologation'), 
    ('dev', 'dev')]

LEVELS = [
    ('error', 'error'),
    ('warning', 'warning'),
    ('debug', 'dubug')]


class Error(models.Model):
    enviroment = models.CharField('Level', choices=ENVIROMENTS, max_length=255)
    level = models.CharField('Level', choices=LEVELS, max_length=255)
    log = models.TextField('Log')
    events = models.IntegerField('Events')

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return r('core:error-home')
        #return r('core:error-home', self.id)    


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
