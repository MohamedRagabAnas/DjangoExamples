from  article.models import Article

def run():
    # Get all products
    all_articles = Article.objects.all()
    print all_articles