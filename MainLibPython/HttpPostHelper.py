import urllib
import urllib.request
import html2text
import os, sys

class HttpPostHelper:
    def get(self, url, filePath):
        f = urllib.request.urlopen(url)

        # very important, byte by utf-8 
        myfile = f.read()
        myfileStr = myfile.decode('utf-8')

        # Open a file
        fd = os.open( filePath, os.O_RDWR|os.O_CREAT )

        # Write one string
        os.write(fd, myfile)

        # Close opened file
        os.close( fd )
