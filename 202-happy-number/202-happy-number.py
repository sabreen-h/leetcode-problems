class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            s = 0
            while n > 0:
                s += (n % 10)**2
                n = n //10
            return s
        
        d = set()
        while n != 1 and n not in d:
            d.add(n)
            n = get_next(n)
        return n == 1
        