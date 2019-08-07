from django.urls import path, re_path
from .views import BlogPostRudView

app_name = 'api-blog'
urlpatterns = [
    re_path(r'^(?P<pk>\d+)$', BlogPostRudView.as_view(), name="blog_rud"),
]
