from flask import render_template, Blueprint, request, redirect, url_for
from models.create_article import CreateArticleModel
from models.articles_category import ArticlesCategoryModel
from models.single_article import SingleArticleModel

articles_bp = Blueprint("articles", __name__, url_prefix="/articles")

@articles_bp.route('/create-article', methods=('GET', 'POST'))
def create_article():
  if request.method == 'POST':
    model = CreateArticleModel()
    model.CreateArticle(request.form)
    return redirect(url_for("index"))

  return render_template("create_article.html")

@articles_bp.route('/categories')
def articles_categories():
  return render_template("categories.html")

@articles_bp.route('/category/<category>')
def articles_category(category):
  model = ArticlesCategoryModel()
  articles = model.GetArticlesByCategory(category)
  return render_template("articles_category.html", articles_to_display=articles)

@articles_bp.route('/article/<int:article_id>')
def article(article_id):
  model = SingleArticleModel()
  article = model.GetArticle(article_id)
  return render_template("view_article.html", article=article)