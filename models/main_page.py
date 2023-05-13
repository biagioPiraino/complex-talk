from entities.article import Article
from services.article_service import ArticleService

class MainPageModel:
  def __init__(self) -> None:
    pass

  def GetMainArticle(self) -> Article:
    article_service = ArticleService()
    return article_service.GetLatestArticle()

  def GetArticlesToDisplay(self) -> list:
    return list()
