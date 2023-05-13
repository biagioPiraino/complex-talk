from entities.article import Article
from entities.data_objects.article_do import ArticleDo

class ArticleService:

  def __init__(self) -> None:
    pass

  def CreateArticle(self, article: Article):
    with ArticleDo() as data_object:
      data_object.CreateArticle(article)
  
  def GetLatestArticle(self) -> Article:
    query_result = []
    
    with ArticleDo() as data_object:
      query_result = data_object.GetLatestArticle()

    return self.BuildArticle(query_result)
  
  def BuildArticle(self, query_result) -> Article:
    article = Article(
      category=query_result[2],
      title=query_result[3],
      content=query_result[4])
    
    article.Id = query_result[0]
    article.Created = query_result[1]

    if article.Category == "1":
      article.DisplayCategory = "Tech"
    elif article.Category == "2":
      article.DisplayCategory = "Business"
    elif article.Category == "3":
      article.DisplayCategory = "World"
    else:
      article.DisplayCategory = "Lifestyle"

    return article