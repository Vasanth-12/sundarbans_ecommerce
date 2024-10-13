import json
from schema.orderSchema import Order

orderData = {}


###################################################################
# load the order data from the  json file
###################################################################
def loadOrderData():
    with open("./load_orderData.json") as fh:
        orderData = json.load(fh)

    return orderData


###################################################################
# persist the order details in order json file
###################################################################
def placeOrder(order: Order):
    orderData = loadOrderData()

    # convert the order object to dictionary
    orderData[order.id] = order.__dict__

    with open("./load_orderData.json", "w") as fh:
        json.dump(orderData, fh)
    print("Order placed for UserID ", order.user["id"], " with orderID ", order.id)

    return order.id


###################################################################
# Get the order details on admin request 
###################################################################
def getOrderDetails():

    orderData = loadOrderData()
    orderCount = len(orderData.keys())

    totalDiscount = 0
    totalPurchasedAmount = 0
    for key, value in orderData.items():
        totalDiscount += value["discountcost"]
        totalPurchasedAmount += value["totalcost"]

    return {"ordercount": orderCount, "totalpurchasedamount": totalPurchasedAmount, "totaldiscount": totalDiscount}
