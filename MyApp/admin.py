from django.contrib import admin


from MyApp.models import Comments, Links, LinksThemes, Profile



@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date', 'text', 'parent', 'id')
    readonly_fields = ('date',)


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('theme','description', 'link', 'draft')
    list_filter = ('theme', 'draft')
    list_editable = ('draft',)
    actions = ['publish', 'unpublish']

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change', )

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)
    
@admin.register(LinksThemes)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('theme',)

@admin.register(Profile)
class ProfileRegisterAdmin(admin.ModelAdmin):
    list_display = ('master', 'photo')


