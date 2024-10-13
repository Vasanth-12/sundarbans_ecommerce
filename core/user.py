import uuid
from dataaccess import user, order, cart
from schema.productSchema import Product
from schema.orderSchema import Order


def addToCart(userId, product: Product):

    # Add the product to the cart based on the userid
    if user.getUserInfo(userId) != None:
        return cart.addToCart(userId, product)
    return False


def checkOut(userId):

    # To place the order, the userinfo and products in the carts are needed
    # With userid, get the userinfo and productlist in cart
    userInfo = user.getUserInfo(userId)
    userCartInfo = cart.getUserCardInfo(userId)
    productList = userCartInfo["productlist"]

    # initialize the totalcode, discountcost, actualcost to 0
    totalCost = 0
    discountCost = 0
    actualCost = 0

    # Proceed only if we have atleast one product in the cart
    if (len(productList)):

        # iterate through every product in the cart
        for product in productList:
            actualCost += (product["price"] * product["count"])

        # apply discount on every nth time
        if userInfo["ordercount"] % 3 == 0:
            discountCost = actualCost * 10 / 100
        
        # calculate totalcost
        totalCost = actualCost - discountCost

        #using above info, create order object
        orderData = Order(id=str(uuid.uuid4()), user=userInfo, productlist=productList,  actualcost=actualCost, 
                      totalcost=totalCost, discountcost=discountCost)
        
        # create a order transaction
        # if the transaction is successful, clear the cart and increment the purchase count in the userinfo
        # else, do nothing
        if order.placeOrder(orderData):
            print("Order placed successfully with order id ", orderData.id)
            user.orderPlaced(userId)
            cart.clearCart(userId)

            return orderData.id
        else:
            print("Can't place the order")
            return False
    else:
        print("No item in cart to place order")
        return False
