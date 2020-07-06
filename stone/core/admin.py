from django.contrib import admin
from stone.core.models import CustomUser, Error


admin.site.register(Error)
admin.site.register(CustomUser)