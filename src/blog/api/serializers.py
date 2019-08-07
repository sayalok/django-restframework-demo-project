from rest_framework import serializers

from blog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model   = BlogPost
        fields  = [
            'pk',
            'user',
            'title',
            'content',
            'timestamp'
        ] 

        read_only_fields = ['user']

    def validate_title(self,value):
        print('here')
        qs = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists() :
            raise serializers.ValidationError("The Title must be unique")
        return value
