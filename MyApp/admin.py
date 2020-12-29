from django.contrib import admin

from MyApp.models import Comments, Profile


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date', 'text', 'parent', 'id')
    readonly_fields = ('date',)

@admin.register(Profile)
class ProfileRegisterAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo')

