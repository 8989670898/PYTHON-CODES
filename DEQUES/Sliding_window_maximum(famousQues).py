Q2. Sliding Window Maximum
Solved
feature icon
Using hints is now penalty free
Use Hint
Problem Description
Given an array of integers A. There is a sliding window of size B, moving from the very left of the array to the very right. You can only see the B numbers in the window. Each time the sliding window moves rightwards by one position. You have to find the maximum for each window.

Return an array C, where C[i] is the maximum value in the array from A[i] to A[i+B-1].

Refer to the given example for clarity.

NOTE: If B > length of the array, return 1 element with the max of the array.

Problem Constraints
1 <= |A|, B <= 106
Input Format
The first argument given is the integer array A.

The second argument given is the integer B.

Output Format
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

Example Input
Input 1:

 A = [1, 3, -1, -3, 5, 3, 6, 7]
 B = 3
Input 2:

 A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
 B = 6

Example Output
Output 1:

 [3, 3, 5, 5, 6, 7]
Output 2:

 [7, 7, 7, 7]

Example Explanation
Explanation 1:

 Window position     | Max
 --------------------|-------
 [1 3 -1] -3 5 3 6 7 | 3
 1 [3 -1 -3] 5 3 6 7 | 3
 1 3 [-1 -3 5] 3 6 7 | 5
 1 3 -1 [-3 5 3] 6 7 | 5
 1 3 -1 -3 [5 3 6] 7 | 6
 1 3 -1 -3 5 [3 6 7] | 7
 
 
 =============================CODE================
 from collections import deque
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, A, B):
        n=len(A)
        res=[]
        window=deque()
        if B>len(A):
            return max(A)
        if B==0 or A==0:
            return res
        
        #We are pushin index number rather than elements
        for i in range(B):
            while window and A[i]>=A[window[-1]]:
                window.pop()
            window.append(i)
        
        for i in range(B,n):
            res.append(A[window[0]])
        
            while window and window[0] <= i-B:
                window.popleft()
            
            while window and A[i]>=A[window[-1]]:
                window.pop()
            window.append(i)
        
        res.append(A[window[0]])

        return res