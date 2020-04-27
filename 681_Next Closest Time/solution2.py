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

class Solution:
    def nextClosestTime(self, time: str) -> str:
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = [i for i in time if i!=':']

        while True:
            cur = (cur + 1) % (24 * 60)

            hours = cur // 60
            minutes = cur % 60

            if hours < 10:
                hours = "0" + str(hours)
            if minutes < 10:
                minutes = "0" + str(minutes)

            ans = str(hours) + str(minutes)
            flag = True
            for i in ans:
                if i not in allowed:
                    flag = False
                    break
            if flag:
                return str(hours) + ":" + str(minutes)
