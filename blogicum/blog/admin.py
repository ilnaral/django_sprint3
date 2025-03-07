from django.contrib import admin

from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text_short',
        'location',
        'category',
        'pub_date',
        'is_published',
    )
    list_editable = (
        'location',
        'category',
        'pub_date',
        'is_published',
    )
    search_fields = (
        'title',
        'text',
        'location',
    )
    list_per_page = 25

    def text_short(self, object: Post) -> str:
        return f'{object.text[:50]}...'


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'description_short',
        'slug',
        'is_published',
        'created_at',
    )
    list_editable = (
        'slug',
    )
    list_filter = (
        'title',
        'description',
    )
    list_per_page = 25

    def description_short(self, object: Category) -> str:
        return f'{object.description[:50]}...'


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    list_filter = ('name',)
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
