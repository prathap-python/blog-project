from django.contrib import admin
from blog.models import Post,Comment
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','publish')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    date_hierarchy='publish'
admin.site.register(Post,PostAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')
admin.site.register(Comment,CommentAdmin)


# Register your models here.
