from blog.models import Post
from django import template
from django.db.models import Count
register=template.Library()
@register.simple_tag
def total_posts():
    return Post.objects.count()
@register.inclusion_tag("blog/latestposts123.html")
def latest_posts():
    posts=Post.objects.order_by('-publish')[:2]
    return {'posts':posts}
# @register.assignment_tag
# def get_most_commented_posts(count=5):
    #return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]