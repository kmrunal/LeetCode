# Approach sliding window, keep moving through the array and counting fruits
# if the count of types of fruits becomes equal to x then remove that type
# take the maximum of current index and the index where last type of fruit
# was found and deleted

class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        count =  {}
        ans = j = 0

        for i,x in enumerate(tree):
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1

            while len(count) == 3:
                count[tree[j]] -= 1

                if count[tree[j]] == 0:
                    del count[tree[j]]

                j += 1

            ans = max(ans, i - j + 1)

        return ans
