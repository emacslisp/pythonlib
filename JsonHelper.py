import json

class JsonHelper:
  def indentJson(jsonStr):
    return json.dumps(jsonStr, sort_keys=True, indent=4, separators=(',', ': '))
