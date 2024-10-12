import json

productData = {}

def loadProductData():
    with open("./load_productData.json") as fh:
        productData = json.load(fh)

    print("ProductData loaded")