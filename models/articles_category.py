from services.article_service import ArticleService

class ArticlesCategoryModel:
  def __init__(self) -> None:
    pass

  def GetArticlesByCategory(self, category: str) -> list:
    article_service = ArticleService()
    return article_service.GetArticlesByCategory(category)