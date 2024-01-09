from django.contrib import admin
from django.utils.html import format_html
from .models import Learn, Comments


class CommentsInLine(admin.StackedInline):
    model = Comments


@admin.register(Learn)
class LearnAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status', 'show_github_url']
    list_filter = ['status']
    inlines = [
        CommentsInLine
    ]

    def show_github_url(self, obj):
        if obj.github_url is not None:
            return format_html(f'<a href="{obj.github_url}" target=*_blank>{obj.github_url}</a>')
        else:
            return ''

    show_github_url.short_description = "GitHub URL"


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'learn', 'reason']
    list_filter = ['learn']
