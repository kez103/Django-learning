from django.db import models
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(Post, PostAdmin)
