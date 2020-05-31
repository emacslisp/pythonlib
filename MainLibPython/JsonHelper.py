import json

class JsonHelper:
  def indentJson(self, jsonStr):
    jsonObject = json.loads(jsonStr)
    return json.dumps(jsonObject, sort_keys=True, indent=4, separators=(',', ': '))
