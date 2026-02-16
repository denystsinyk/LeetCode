'''
create the res array 
then the start of each bookuing and the end each get the seats
have a loop that goes start to end adding

'''

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # res = [0] * (n)

        # for b in bookings:
        #     for i in range(b[0],b[1] + 1):
        #         res[i-1] += b[2]
        
        # return res

        # tahts slow so need a faster implement
        # set the bounds 

        res = [0] * (n+1)

        for start, end, seats in bookings:
            res[start - 1] += seats
            res[end] -= seats

        # so now when we start we have the seat nums
        # and 1 after the end is the -seats

        #then we make a loop taht will loop res and for each spot take the one ahead of it and set it back
        for i in range(1,n):
            res[i] += res[i-1]
        
        return res[:-1]



