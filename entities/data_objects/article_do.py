import psycopg2
import os
from entities.article import Article

class ArticleDo:
  def __init__(self):
    self.host     = os.environ.get("HOST")
    self.port     = os.environ.get("PORT")
    self.dbname   = os.environ.get("DB_NAME")
    self.user     = os.environ.get("DB_USER")
    self.password = os.environ.get("PASSWORD")

  def __enter__(self):
    self.conn  = psycopg2.connect(
      host     = self.host,
      port     = self.port,
      dbname   = self.dbname,
      user     = self.user,
      password = self.password
    )
    self.cursor = self.conn.cursor()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.cursor.close()
    self.conn.close()

  def CreateArticle(self, article: Article):
    self.cursor.callproc(
      "create_article", 
      (article.Category, article.Title, article.Content))
    self.conn.commit()

  def GetLatestArticle(self):
    self.cursor.callproc("get_latest_article")
    return self.cursor.fetchone()
  
  def GetLatestArticleByCategory(self, category: str):
    self.cursor.callproc("get_latest_article_by_category", [category])
    return self.cursor.fetchone()

  def GetArticlesByCategory(self, category: str):
    self.cursor.callproc("get_articles_by_category", [category])
    return self.cursor.fetchall()