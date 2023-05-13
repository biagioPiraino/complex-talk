from entities.article import Article
from services.article_service import ArticleService

class CreateArticleModel:
  def __init__(self) -> None:
    pass

  def CreateArticle(self, form: dict):
    article = Article(
      category=form['article-category'],
      title=form['article-title'],
      content=form['article-content'])
    
    article_service = ArticleService()
    article_service.CreateArticle(article)
    
