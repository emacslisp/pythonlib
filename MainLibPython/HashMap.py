class HashMap:
    thisHashMap = {}
    def put(self, key, value):
        thisHashMap[key] = value

    def get(self, key):
        return thisHashMap[key]

    def getKeys(self):
        return thisHashMap.keys()