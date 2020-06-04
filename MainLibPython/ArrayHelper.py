class ArrayHelper:
    def printArray(self, array):
        for i in array:
            print(i)

    def reverseArray(self, array):
        return list(reversed(array))

    def reverseArraySlice(self, array):
        return array[::-1]