from django.contrib import admin

from webapp.models import Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "category", "create_at")
    list_filter = ("id", "status", "category", "create_at")
    search_fields = ("status", "text")
    filter = ("text", "status", "category", "create_at")
    readonly_fields = ("id", "create_at")


admin.site.register(Article, ArticleAdmin)
