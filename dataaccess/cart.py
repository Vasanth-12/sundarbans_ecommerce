import json
from schema.productSchema import Product

cartData = {}


###################################################################
# this function will load the data from cart data file
###################################################################
def loadCartData():
    # load data from the cart data file
    with open("./load_cartData.json") as fh:
        cartData = json.load(fh)

    return cartData


###################################################################
# this function will add the given product to the card for
#       the given userid
###################################################################
def addToCart(userId, product: Product):

    # before every cart operation, load the data first
    cartData = loadCartData()

    # if the particular user cart is not created before / not present
    #       create the dictionary for iit first
    # and then add the product in the card
    if cartData.get(userId) == None:
        intialState = {}
        cartData[userId] = {"userid": userId, "productlist": []}

    # Covnert the product object to dictionary and store it in json file
    cartData[userId]["productlist"].append(product.__dict__)

    # once add in dictionary, persiste in the cart data file
    with open("./load_cartData.json", "w") as fh:
        json.dump(cartData, fh)

    return True


###################################################################
# this function will get the cart info for the give userid
###################################################################
def getUserCardInfo(userId):
    cartData = loadCartData()
    return cartData[userId]


###################################################################
# this function will clear the product from cart, 
#       once the order the order is placed successfully
###################################################################
def clearCart(userId):
    cartData = loadCartData()
    if cartData.get(userId):

        # clear the prodcutlist for the user
        cartData[userId]["productlist"].clear()

        # persist in cart data file
        with open("./load_cartData.json", "w") as fh:
            json.dump(cartData, fh)
        print("Cart cleared for userId: f{userId}")
        return True
    else:
        print("Cart for userId f{userId} not found")
        return False