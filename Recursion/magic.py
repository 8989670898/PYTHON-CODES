# # Given a number A, check if it is a magic number or not.

# # A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively by adding the sum of the digits after every addition.
# If the single digit comes out to be 1, then the number is a magic number.

#  A = 83557, output = 1

def magic(A):
    while A>9:   #since a single digit lies between 1 to 9. if A becomes < 9 then it is single for ex-
        # 83557 = 28, A > 9, (2+8)=10 > 9,(1+0)=1 now  A < 9
        sum1=0
        while A>0:
            sum1+=A%10
            A=A//10
        A=sum1
    if A == 1:
        return 1
    return 0

print(magic(123))