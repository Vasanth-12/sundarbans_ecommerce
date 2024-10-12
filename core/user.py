import uuid
from dataaccess import user, order, cart
from schema.productSchema import Product
from schema.orderSchema import Order


def loadUserData():
    user.loadUserData()


def addToCart(userId, product: Product):
    print("ID: ", userId, " PRODUCT: ", product)
    return cart.addToCart(userId, product)


def checkOut(userId):

    userInfo = user.getUserInfo(userId)
    print("Useriinfo: ", userInfo)
    userCartInfo = cart.getUserCardInfo(userId)
    print("userCartInfo: ", userCartInfo)
    productList = userCartInfo["productlist"]
    print("ProductList: ", productList)

    totalCost = 0
    discountCost = 0
    actualCost = 0
    if (len(productList)):

        for product in productList:
            actualCost += (product["price"] * product["count"])

        if userInfo["ordercount"] % 3 == 0:
            discountCost = actualCost * 10 / 100
        
        totalCost = actualCost - discountCost
        orderData = Order(id=str(uuid.uuid4()), user=userInfo, productlist=productList,  actualcost=actualCost, 
                      totalcost=totalCost, discountcost=discountCost)
        
        if order.placeOrder(orderData):
            print("Order placed successfully")
            user.orderPlaced(userId)
            cart.clearCart(userId)

            return True
        else:
            print("Can't place the order")
            return False
    else:
        print("No item in cart to place order")
        return False
