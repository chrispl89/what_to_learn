from .models import Learn, Comments
from rest_framework import serializers


class LearnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Learn
        fields = ['id', 'title', 'description', 'github_url', 'status']


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['learn', 'reason']
