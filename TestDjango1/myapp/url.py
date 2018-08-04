from django.conf.urls import url,include
from article.views import articles
from article.views import article

urlpatterns = [url(r'^all/$', articles, name = 'articles'), url(r'^get/(?P<article_id>\d+)/$', article, name = 'article'), ]
