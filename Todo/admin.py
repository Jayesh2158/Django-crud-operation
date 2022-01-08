from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import *

# admin.site.register(list)
# admin.site.register(DashBoard)
admin.site.register(User, UserAdmin)
