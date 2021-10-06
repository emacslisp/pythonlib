def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("it is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/exception")

ask_for_int()