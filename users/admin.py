from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomCreationForm, CustomChangeForm

# Register your models here.
class CustomAdminUser(UserAdmin):
    add_forms = CustomCreationForm
    form = CustomChangeForm
    list_display = ['username', 'email', 'age']


admin.site.register(CustomUser, CustomAdminUser)