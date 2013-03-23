#--------------------------------------------------------------
# Script: Calculates the amount of time a procedure takes
# Author: Santiago Paiva
# Version: 1.0
#--------------------------------------------------------------

import time

def timeExecution(code):
    start = time.clock()
    result = eval(code)
    runtime = time.clock() - start
    return result, runtime


#-------------------------------------------------------------
# Test function
#-------------------------------------------------------------

def spinLoop(n):
    i=0
    while i < n:
        i = i + 1


print timeExecution('spinLoop(1000)')[1]
print timeExecution('spinLoop(10 ** 9)')[1]


