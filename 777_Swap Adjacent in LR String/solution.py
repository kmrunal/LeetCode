# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
# a move consists of either replacing one occurrence of "XL" with "LX",
# or replacing one occurrence of "RX" with "XR".
# Given the starting string start and the ending string end, return True if
# and only if there exists a sequence of moves to transform one string to the other.

# example
# start = "RXXLRXRXL", end = "XRLXXRRLX"
# output = True

# Approach #2: Two Pointers [Accepted]
# Time complexity : O(N)
# Space complexity: O(1)
#

class Solution(object):
    def canTransform(self, start, end):
        # For (i, x) and (j, y) in enumerate(start), enumerate(end)
        # where x != 'X' and y != 'X',
        # and where if one exhausts early, it's elements are (None, None),...
        for (i, x), (j, y) in itertools.izip_longest(
                ((i, x) for i, x in enumerate(start) if x != 'X'),
                ((j, y) for j, y in enumerate(end) if y != 'X'),
                fillvalue = (None, None)):

            # If not solid or accessible, return False
            if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
                return False

        return True
