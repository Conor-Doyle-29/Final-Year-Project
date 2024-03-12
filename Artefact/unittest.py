from mean import mean
import statistics as stat
def unitTest(testLists):
    passes = 0 
    fails = 0 
    for i in testLists:
        expectedValue= stat.mean(i)
        actualValue = mean(i)
        if expectedValue == actualValue:
            passes += 1
        else: 
            fails +=1 
    return passes, fails

testLists = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

passes , fails = unitTest (testLists)

print("Passes",passes)
print("Fails", fails)