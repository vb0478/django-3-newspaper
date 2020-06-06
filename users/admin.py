from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    # Let’s do that now so that it displays email, username, age, and staff status
    list_display = ['email','username','age','is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)
