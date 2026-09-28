class Solution(object):
    def smallestEvenMultiple(self, n):
        
        if int(n) % 2 == 0:
            return(int(n))
        else:
            return(int(n)*2)
        