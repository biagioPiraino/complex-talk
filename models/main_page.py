from entities.article import Article
from services.article_service import ArticleService

class MainPageModel:
  def __init__(self) -> None:
    pass

  def GetMainArticle(self) -> Article:
    article_service = ArticleService()
    return article_service.GetLatestArticle()

  def GetArticlesToDisplay(self) -> list:
    categories = ["1","2","3","4"]
    
    articles_to_display = []
    article_service = ArticleService()

    for category in categories:
      article_to_add = article_service.GetLatestArticleByCategory(category)
      if article_to_add != None:
        articles_to_display.append(article_to_add)

    return articles_to_display
