class HashMap:
    thisHashMap = {}
    def put(self, key, value):
        self.thisHashMap[key] = value

    def get(self, key):
        return self.thisHashMap[key]

    def getKeys(self):
        return self.thisHashMap.keys()

    def dump(self):
        keys = self.getKeys()
        for i in keys:
            print(self.thisHashMap[i])