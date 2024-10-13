import json

userData = {}

###################################################################
# load the data from the user json file
###################################################################
def loadUserData():
    with open("./load_userData.json") as fh:
        userData = json.load(fh)
    return userData


###################################################################
# get the userinfo for the given userid
###################################################################
def getUserInfo(userId):
    userData = loadUserData()
    return userData.get(userId)


###################################################################
# Increment the ordercount once order placed successfully
###################################################################
def orderPlaced(userId):

    userData = loadUserData()
    userData[userId]["ordercount"] += 1

    with open("./load_userData.json", "w") as fh:
        json.dump(userData, fh)

    print("Order count increased")