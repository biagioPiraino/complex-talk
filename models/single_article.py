from entities.article import Article
from services.article_service import ArticleService

class SingleArticleModel:
  def __init__(self) -> None:
    pass

  def GetArticle(self, id: int) -> Article:
    article_service = ArticleService()
    return article_service.GetArticle(id)