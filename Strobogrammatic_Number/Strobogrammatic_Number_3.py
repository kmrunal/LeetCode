# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

# example:
# Input: low = "50", high = "100"
# Output: 3
# Explanation: 69, 88, and 96 are three strobogrammatic numbers.

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def helper(i, n):
            if i == 0:
                return [""]
            if i == 1:
                return ["0","1","8"]

            li = helper(i - 2, n)
            res = []

            for j in li:
                if i != n:
                    a = "0" + j + "0"
                    res.append("0" + j + "0")

                res.append("1" + j + "1")
                res.append("6" + j + "9")
                res.append("8" + j + "8")
                res.append("9" + j + "6")

            return res

        st = len(low)
        en = len(high)

        # find answers for all n length

        ans = []
        for i in range(st, en + 1):
            ans += helper(i, i)

        # filter the answers which do not lie between low and high

        ans_count = []
        for i in ans:
            num = int(i)
            if int(low) <= num <= int(high):
                ans_count.append(num)

        return len(ans_count)
