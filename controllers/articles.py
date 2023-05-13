from flask import render_template, Blueprint, request, redirect, url_for
from models.create_article import CreateArticleModel

articles_bp = Blueprint("articles", __name__, url_prefix="/articles")

@articles_bp.route('/create-article', methods=('GET', 'POST'))
def create_article():
  if request.method == 'POST':
    model = CreateArticleModel()
    model.CreateArticle(request.form)
    return redirect(url_for("index.html"))

  return render_template("create_article.html")