from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route('/')
def index():
    cates = dao.load_categories()

    query= request.args.get("query")
    cate_id = request.args.get("cate_id")

    prods = dao.load_products(query=query,cate_id=cate_id)

    return render_template("index.html",categories=cates,products=prods)

if __name__ == "__main__":
    app.run(debug=True)
