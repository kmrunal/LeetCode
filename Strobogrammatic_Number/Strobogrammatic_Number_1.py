# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# example:
# "69" -> True
# "88" -> True
# "962" -> False

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        cache = {"0":"0", "1":"1","6":"9","8":"8","9":"6"}
        result = ""

        for i in num:
            if i not in cache:
                return False
            result = cache[i] + result
        return result == num
