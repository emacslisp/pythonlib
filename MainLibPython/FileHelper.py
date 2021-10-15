import os, sys
class FileHelper:
  def stringToFile(self, str, filePath):
    fd = os.open(filePath, os.O_RDWR|os.O_CREAT)
    os.write(fd, str)
    os.close(fd)

  def fileToString(self, filePath):
    with open(filePath, 'r') as myfile:
      data=myfile.read()
    return data
    
