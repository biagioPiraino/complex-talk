from datetime import datetime
from enum import Enum

class Article:
  Id:int
  Created:datetime
  Category:Enum
  Title:str
  Content:str