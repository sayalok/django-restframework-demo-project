from rest_framework import generics
from blog.models import BlogPost
from .serializers import BlogPostSerializer

app_name = 'api-blog'
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field        = 'pk'
    serializer_class    = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()