from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blogapp/article_list.html'
    context_object_name = 'articles'
    queryset = (
        Article.objects.defer('content').select_related('author').prefetch_related('tags')
    )
