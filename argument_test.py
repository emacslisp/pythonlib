import MainLibPython

# python argument_test.py 1 2 3
OptionHelper = MainLibPython.OptionHelper()
ArrayHelper = MainLibPython.ArrayHelper()
ArrayHelper.printArray(OptionHelper.getOptionList())