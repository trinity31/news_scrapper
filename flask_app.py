from flask import Flask,render_template, request, redirect
from extractors.naver import extract_naver_news

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword is None:
    return redirect("/")
  else:
    newses = extract_naver_news(keyword)
    return render_template("search.html", keyword=keyword, newses=newses)