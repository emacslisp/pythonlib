from threading import Timer

class ThreadHelper: 
    def mockupFunction(self):
        print "Mockup Function"

    def sleep(self, seconds):
        t = Timer(seconds, self.mockupFunction)
        t.start()



