from entities.article import Article
from entities.data_objects.article_do import ArticleDo

class ArticleService:

  def __init__(self) -> None:
    pass

  def CreateArticle(self, article: Article):
    with ArticleDo() as data_object:
      data_object.CreateArticle(article)