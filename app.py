from fastapi import FastAPI
from core import user, order, product
from schema.productSchema import Product

app = FastAPI()

@app.get("/")
def ping():
    return {"status code": 200, "message": "pong"}


@app.put("/user/{id}/addtocart")
def addToCart(id: str, product: Product):
    try:
        print("ID: ", id)
        user.addToCart(id, product)
        return {"status code": 200, "message": "item added successfull"}
    except:
        return {"status code": 500}
    

@app.post("/user/{id}/checkout")
def checkout(id:str):
    try:
        user.checkOut(id)
        return {"status code": 200, "message": "order placed successfull"}
    except:
        return {"status": 500}
