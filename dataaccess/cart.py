import json
from schema.productSchema import Product

cartData = {}

def loadCartData():
    with open("./load_cartData.json") as fh:
        cartData = json.load(fh)

    return cartData

def addToCart(userId, product: Product):

    cartData = loadCartData()
    print("BEFORE: ", cartData)
    if cartData.get(userId) == None:
        intialState = {}
        cartData[userId] = {"userid": userId, "productlist": []}

    cartData[userId]["productlist"].append(product.__dict__)
    print("AFTER: ", cartData)

    with open("./load_cartData.json", "w") as fh:
        json.dump(cartData, fh)

    return True


def getUserCardInfo(userId):
    cartData = loadCartData()
    return cartData[userId]


def clearCart(userId):
    cartData = loadCartData()
    if cartData.get(userId):
        cartData[userId]["productlist"].clear()

        with open("./load_cartData.json", "w") as fh:
            json.dump(cartData, fh)
        print("Cart cleared for userId: f{userId}")
        return True
    else:
        print("Cart for userId f{userId} not found")
        return False