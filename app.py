from fastapi import FastAPI, Response
from core import user, admin
from schema.productSchema import Product

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status code": 200, "content": "pong"}


@app.put("/user/{id}/addtocart")
def addToCart(id: str, product: Product):
    try:
        if user.addToCart(id, product):
            print("ProductID ", product.id," added to the User cart", id)
            return {"content": "Product added to the cart"}
        else:
            print("UserID ", id," not found")
            return Response(status_code=404, content="User not found")
    except:
        return Response(status_code=500, content="Internal Server Error")
    

@app.post("/user/{id}/checkout")
def checkout(id:str):
    try:
        orderID = user.checkOut(id)
        if orderID:
            return {"content": "Order Placed with order id: " + orderID}
        else:
            return Response(status_code=404, content="No product in the cart")
    except:
        return Response(status_code=500, content="Internal Server Error")


@app.get("/admin/order")
def getOrdercontents():
    try:
        return admin.ordercontents()
    except:
        return Response(status_code=500, content="Internal Server Error")