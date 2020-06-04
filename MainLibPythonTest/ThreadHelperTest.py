import MainLibPython

def main():
    threadHelper = MainLibPython.ThreadHelper()
    print("sleeping start!!!")
    threadHelper.sleep(10)
    print("sleeping 10 seconds")

main()