# Given a time represented in the format "HH:MM", form the next
# closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid.
# "1:34", "12:9" are all invalid.

# Input: 19:34
# Output: 19:39


# Input: 23:59
# Output: 22:22

# Time Complexity: O(1), we try upto 24 * 60 times until we find an answer
# Space Complexity: O(1)

# Approach
# Simulate the clock going forward by one minute.
# Each time it moves forward, if all the digits are allowed,
# then return the current time.

class Solution(object):
    def nextClosestTime(self, time):
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))
