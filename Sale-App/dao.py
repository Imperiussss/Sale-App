import json

def load_categories():
    with open("data/category.json", encoding="utf-8") as cate_f:
        return json.load(cate_f)

def load_products(query=None, cate_id=None):
    with open("data/product.json", encoding="utf-8") as prod_f:
        prods = json.load(prod_f)

        if query:
            prods = [p for p in prods if p["name"].find(query) >= 0]

        if cate_id:
            prods = [p for p in prods if p["cate_id"].__eq__(int(cate_id))]

        return prods


if __name__ == "__main__":
    print(load_categories())