from django.contrib import admin

from MyApp.models import Comments, Links, LinksThemes


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date', 'text', 'parent', 'id')
    readonly_fields = ('date',)


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('description', 'link')
    
@admin.register(LinksThemes)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('theme',)
