# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Find all strobogrammatic numbers that are of length = n.

# example:
# n = 2 -> ["11","69","88","96"]

# hint -> Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.



class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(i):
            if i == 0:
                return [""]
            if i == 1:
                return ["0","1","8"]
            li = helper(i - 2)
            res = []

            for j in li:
                if i != n:
                    res.append("0" + j + "0")
                res.append("1" + j + "1")
                res.append("6" + j + "9")
                res.append("8" + j + "8")
                res.append("9" + j + "6")
            return res
        return helper(n)
