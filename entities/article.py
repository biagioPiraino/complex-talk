from datetime import datetime

class Article:
  Id:int
  Created:datetime
  Category:str
  DisplayCategory:str
  Title:str
  Content:str

  def __init__(self, category: str, title:str, content:str) -> None:
    self.Category = category
    self.Title = title
    self.Content = content