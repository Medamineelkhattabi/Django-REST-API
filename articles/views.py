from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Article
from .serializers import ArticleSerializer

class ArticleListCreateView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
