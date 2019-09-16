from django.contrib import admin
from webapp.models import Article, Issue

admin.site.register(Article)


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'finish_date']
    list_filter = ['status']
    search_fields = ['description']



admin.site.register(Issue, IssueAdmin)

