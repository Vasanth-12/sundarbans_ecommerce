import json

userData = {}

def loadUserData():
    with open("./load_userData.json") as fh:
        userData = json.load(fh)
    return userData


def getUserInfo(userId):
    userData = loadUserData()
    return userData.get(userId)


def orderPlaced(userId):

    userData = loadUserData()
    userData[userId]["ordercount"] += 1

    with open("./load_userData.json", "w") as fh:
        json.dump(userData, fh)

    print("Order count increased")