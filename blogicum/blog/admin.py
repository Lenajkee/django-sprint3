from django.contrib import admin
from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'is_published',
    )
    list_filter = ('is_published', 'category', 'pub_date')
    search_fields = ('title', 'text')
    list_editable = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published')
    list_editable = ('is_published',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location)
