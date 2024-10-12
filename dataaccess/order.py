import json
from schema.orderSchema import Order

orderData = {}

def loadOrderData():

    with open("./load_orderData.json") as fh:
        orderData = json.load(fh)
    print("Order data loaded")

    return orderData


def placeOrder(order: Order):

    orderData = loadOrderData()
    orderData[order.id] = order.__dict__

    with open("./load_orderData.json", "w") as fh:
        json.dump(orderData, fh)

    return True

