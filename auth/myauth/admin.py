from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import normal_user_form
from .models import Mesage


class normal_user_form_Inline(admin.TabularInline):
    model = normal_user_form
    can_delete = False
    verbose_name_plural = 'normal_user_form'


class UserAdmin(BaseUserAdmin):
    inlines = (normal_user_form_Inline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin )

@admin.register(Mesage)
class MesageAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_time' )
