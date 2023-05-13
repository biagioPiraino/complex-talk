from datetime import datetime
from enum import Enum

class Article:
  Id:int
  Created:datetime
  Category:str
  Title:str
  Content:str

  def __init__(self, category: Enum, title:str, content:str) -> None:
    self.Category = category
    self.Title = title
    self.Content = content