from django.db.models import Q
from rest_framework import generics, mixins
from blog.models import BlogPost
from .serializers import BlogPostSerializer

app_name = 'api-blog'

class BlogPostApiView(mixins.CreateModelMixin, generics.ListAPIView):
    
    lookup_field        = 'pk'
    serializer_class    = BlogPostSerializer

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs  = qs.filter(
                    Q(title__icontains = query) | 
                    Q(content__icontains = query)
                ).distinct()
        return qs

    def perform_create(self, serializers):
        serializers.save(user= self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request,*args, **kwargs)

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    
    lookup_field        = 'pk'
    serializer_class    = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()