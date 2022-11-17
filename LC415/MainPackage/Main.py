#main.py

from solutionPackage.Solution import *
# this is out entry point to the test code
# we will test the solution class
# for LeetCode problem 415
# the solution has been provided by...

# instantiate an object of type solution
mySolution = Solution()
'''
result = mySolution.addStrings("123", "456")
print(result) # we expect 123+456 = 579 .... this works
# do a test that will fail

result = mySolution.addStrings("aaa", "bbb")
print(result) # we do not know what to expect

result = mySolution.addStrings("-123", "456")
print(result) # -123+456 = 333

result = mySolution.addStrings("123.5", "456.1")
print(result) #123.5+456.1 = 579.6

result = mySolution.addStrings("123a", "456b")
print(result) # we do not know what to expect

result = mySolution.addStrings("123!", "456@")
print(result) # we do not know what to expect
'''
# lets build a list of test cases and expected results
num1= ["123", "999","1000"]
num2 = ["456", "111", "2000"]
expectedResult = ["579", "1110", "3000"]
#write a loop to try all the test cases
for i in range(0,3):
    result = mySolution.addStrings(num1[i], num2[i])
    if result == expectedResult[i]:
        print("test passed")
    else:
        print("test FAILED, Change professions.")
        print("expected result", expectedResult[i], "actual result", result)