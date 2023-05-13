from datetime import datetime
from enums.category import Category

class Article:
  Id:int
  Created:datetime
  Category:Category
  Title:str
  Content:str