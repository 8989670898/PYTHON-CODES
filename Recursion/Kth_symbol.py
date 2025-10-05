# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and
# each occurrence of 1 with 10.

# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 0-indexed.).

#  A = 3
#  B = 0    Output 1: 0

# for ex - 1 - 0
#          2 - 01
#          3 - 0110 (Bth index 0 is 0)

def Bth_index(A,B):
    def Ath_row(A):
        if A==1:
            return 0
        v1=Ath_row(A-1)
        v2=[]
        for x in v1:
            if x==0:
                v2.append(0)
                v2.append(1)
            v2.append(1)
            v2.append(0)
        return v2
    return Ath_row(A)[B]

# TC- O(2A)

# 2nd Optimized code
def Ath_row(A,B):
    if A==1:
        return 0
    parent = Ath_row(A-1,B//2)  #So we are finding parent of B, since a single digit generates 2 numbers i.e. 1 - 10 or 0 -01, so we dividing by B//2
    if parent == 0:
        return B%2
    else:
        return 1 - (B%2)

# TC - O(A)