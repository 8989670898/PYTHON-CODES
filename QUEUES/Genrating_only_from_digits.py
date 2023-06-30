from collections import deque

class solution:
    def generate_number(self,A):
        res=[]
        q=deque()
        q.append(1)
        q.append(2)
        q.append(3)
        cnt=3
        while len(res)<A:
            num=q.popleft()
            res.append(num)
            if cnt>=A:
                continue
            q.append(num*10+1)
            q.append(num*10+2)
            q.append(num*10+3)
            cnt+=3
        return res