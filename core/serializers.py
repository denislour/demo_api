from django.db import models
from rest_framework import fields, serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description', 'owner'
        )
