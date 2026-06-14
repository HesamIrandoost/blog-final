from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _
from Accounts.models import User, Profile


class UserChangeFormCustom(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = "__all__"


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeFormCustom
    change_password_form = AdminPasswordChangeForm

    # List of columns to display
    list_display = (
        "id",
        "email",
        "username",
        "is_active",
        "is_staff",
        "is_verified",
        "date_joined",
        "last_login",
    )

    # Right sidebar filters
    list_filter = ("is_active", "is_staff", "is_verified", "date_joined")

    # Searchable fields
    search_fields = ("email", "username")

    # Items per page
    list_per_page = 20

    # Read-only fields
    readonly_fields = ("date_joined", "last_login")

    # Default ordering (newest first)
    ordering = ("-date_joined",)

    # Editable fields directly in list view
    list_editable = ("is_active", "is_staff", "is_verified")

    # Custom actions
    actions = ["make_verified", "make_unverified", "activate_users", "deactivate_users"]

    # Form layout for view and edit
    fieldsets = (
        (None, {"fields": ("email", "username", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": ("date_joined", "last_login"),
                "classes": ("collapse",),
            },
        ),
    )

    # Form layout for creating new user
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "is_verified"),
            },
        ),
    )

    def get_queryset(self, request):
        """Optimize query with select_related"""
        return super().get_queryset(request).select_related()

    # Custom actions
    @admin.action(description="✅ Activate verified status")
    def make_verified(self, request, queryset):
        updated = queryset.update(is_verified=True)
        self.message_user(request, f"{updated} user(s) verified successfully.")

    @admin.action(description="❌ Deactivate verified status")
    def make_unverified(self, request, queryset):
        updated = queryset.update(is_verified=False)
        self.message_user(request, f"{updated} user(s) unverified successfully.")

    @admin.action(description="🔓 Activate users")
    def activate_users(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} user(s) activated successfully.")

    @admin.action(description="🔒 Deactivate users")
    def deactivate_users(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} user(s) deactivated successfully.")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # List of columns to display
    list_display = (
        "id",
        "user_email",
        "first_name",
        "last_name",
        "get_full_name",
        "has_image",
        "created_at",
    )

    # Searchable fields
    search_fields = ("first_name", "last_name", "user__email", "user__username")

    # Right sidebar filters
    list_filter = ("created_at", "updated_at")

    # Items per page
    list_per_page = 20

    # Read-only fields
    readonly_fields = ("created_at", "updated_at", "get_full_name_display")

    # Default ordering
    ordering = ("-created_at",)

    # Editable fields directly in list view
    list_editable = ("first_name", "last_name")

    # Direct link to related object
    raw_id_fields = ("user",)

    # Form layout
    fieldsets = (
        (None, {"fields": ("user",)}),
        (
            _("Personal Information"),
            {"fields": ("first_name", "last_name", "bio", "image")},
        ),
        (
            _("Metadata"),
            {
                "fields": ("created_at", "updated_at", "get_full_name_display"),
                "classes": ("collapse",),
            },
        ),
    )

    # Display image in detail page
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.image:
            from django.utils.safestring import mark_safe

            form.base_fields["image"].help_text = mark_safe(
                f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 200px;" />'
            )
        return form

    # Custom display methods for list_display
    @admin.display(description="User Email", ordering="user__email")
    def user_email(self, obj):
        return obj.user.email

    @admin.display(description="Full Name", boolean=False)
    def get_full_name_display(self, obj):
        return obj.get_full_name() or "-"

    @admin.display(description="Has Image", boolean=True)
    def has_image(self, obj):
        return bool(obj.image)

    # Custom actions
    actions = ["clear_bio", "delete_selected_profiles"]

    @admin.action(description="🗑️ Clear selected profiles bio")
    def clear_bio(self, request, queryset):
        updated = queryset.update(bio="")
        self.message_user(request, f"Bio cleared for {updated} profile(s).")

    @admin.action(description="⚠️ Delete selected profiles (irreversible)")
    def delete_selected_profiles(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} profile(s) deleted successfully.")

    # Query optimization
    def get_queryset(self, request):
        return super().get_queryset(request).select_related("user")

    # Validation on save
    def save_model(self, request, obj, form, change):
        if not obj.bio:
            obj.bio = "This user hasn't added a bio yet."
        super().save_model(request, obj, form, change)
