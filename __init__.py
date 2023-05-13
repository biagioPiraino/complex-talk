from flask import Flask, render_template
from controllers.articles import articles_bp
from models.main_page import MainPageModel

app = Flask(__name__)
app.register_blueprint(articles_bp)
  
@app.route('/')
def index():
  model = MainPageModel()
  main_article = model.GetMainArticle()
  articles_to_display = model.GetArticlesToDisplay()
  return render_template("index.html", main_article=main_article, articles_to_display=articles_to_display)

if __name__ == "__main__":
  app.run(debug=True)