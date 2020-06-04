from threading import Timer
import time
class ThreadHelper: 
    def mockupFunction(self):
        print("")

    def sleepWithCallback(self, seconds, callback):
        t = Timer(seconds, callback)
        t.start()
    
    def sleep(self, seconds):
        time.sleep(seconds)



