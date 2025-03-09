from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        }),
    )
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
from django.contrib.auth.models import Group, Permission

# Define groups
editors_group, _ = Group.objects.get_or_create(name="Editors")
viewers_group, _ = Group.objects.get_or_create(name="Viewers")
admins_group, _ = Group.objects.get_or_create(name="Admins")

# Assign permissions
editors_group.permissions.add(
    Permission.objects.get(codename="can_edit"),
    Permission.objects.get(codename="can_create"),
)
viewers_group.permissions.add(Permission.objects.get(codename="can_view"))
admins_group.permissions.add(Permission.objects.get(codename="can_delete"))

