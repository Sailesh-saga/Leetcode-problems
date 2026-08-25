class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        a=[0]*(n+1)
        for slot in bookings:
            l=slot[0]
            r=slot[1]
            val=slot[2]
            a[l-1]+=val #l
            a[r]-=val   #r+1 
        s=0
        for i in range(len(a)):
            s+=a[i]
            a[i]=s
        b=[]
        for i in range(len(a)-1):
            b.append(a[i])
        return b        