from .models import Learn, Comments
from rest_framework import viewsets
from .serializer import LearnSerializer, CommentsSerializer


class LearnViewSet(viewsets.ModelViewSet):
    queryset = Learn.objects.all()
    serializer_class = LearnSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
