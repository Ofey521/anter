from django.contrib import admin
from .models import Post, Comment




class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date_posted', 'content')


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'date_posted')


admin.site.register(Comment, CommentAdmin)
