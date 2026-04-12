class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1
        res =0 
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            pop = x % 10
            x //= 10
            if res > MAX // 10 or (res == MAX // 10 and pop > 7):
                return 0
            res = (res * 10) + pop
        return res * sign