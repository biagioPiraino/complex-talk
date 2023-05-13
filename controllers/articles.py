from flask import render_template, Blueprint

articles_bp = Blueprint("articles", __name__, url_prefix="/articles")

@articles_bp.route('/create-article')
def create_article():
  return render_template("create_article.html")