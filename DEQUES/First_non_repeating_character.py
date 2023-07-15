Q1. First non-repeating character
Solved
feature icon
Using hints is now penalty free
Use Hint
Problem Description
Given a string A denoting a stream of lowercase alphabets, you have to make a new string B.
B is formed such that we have to find the first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found, append '#' at the end of B.



Problem Constraints
1 <= |A| <= 100000



Input Format
The only argument given is string A.



Output Format
Return a string B after processing the stream of lowercase alphabets A.

Example Input
Input 1:

 A = "abadbc"
Input 2:

 A = "abcabc"

Example Output
Output 1:

"aabbdd"
Output 2:

"aaabc#"

====================CODE===================

from collections import deque
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        res=""
        hm={}
        dq=deque()

        for i in range(len(A)):
            if A[i] in hm:
                hm[A[i]]+=1
            else:
                hm[A[i]]=1
                dq.append(A[i])
            while len(dq)>0 and hm[dq[0]]>1:
                hm[dq[0]]-=1
                dq.popleft()
            if len(dq)>0 and dq[0]==A[i]:
                res+=dq[0]
            elif len(dq)>0 and dq[0]!=i:
                res+=dq[0]
            else:
                res+="#"
        return res