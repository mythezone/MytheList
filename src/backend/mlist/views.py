# Create your views here.
from rest_framework import viewsets
from .models import MList, Comment
from .serializer import MListSerializer, CommentSerializer

class MListViewSet(viewsets.ModelViewSet):
    queryset = MList.objects.all()
    serializer_class = MListSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer