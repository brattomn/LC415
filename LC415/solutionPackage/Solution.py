# LC415.py
# Solution to the LeetCode problem 415
# https://leetcode.com/problems/add-strings/
class Solution:
    def toInt(self, num):
        answer = 0
        for d in num:
            answer = answer * 10 + (ord(d)-48) 
        return answer
        
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = self.toInt(num1)
        n2 = self.toInt(num2)
        print(n1,n2)
        answer = n1+n2
        return str(answer)
    