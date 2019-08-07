from django.urls import path, re_path
from .views import BlogPostApiView, BlogPostRudView

app_name = 'api-blog'
urlpatterns = [
    path('', BlogPostApiView.as_view(), name="blog_create"),
    re_path(r'^(?P<pk>\d+)$', BlogPostRudView.as_view(), name="blog_rud"),
]
