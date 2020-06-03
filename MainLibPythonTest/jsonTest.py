import MainLibPython

JsonHelper = MainLibPython.JsonHelper()
jsonBody = '{"abc": 5, "def": 7}'
print JsonHelper.indentJson(jsonBody)
