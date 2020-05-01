# Time Complexity: O(N)
# Space Complexity: O(N)

from collections import defaultdict
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_order = []
        color = [Solution.WHITE for i in range(numCourses)]
        is_possible = True

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return False
            color[node] = Solution.GRAY
            for neighbour in adj_list[node]:
                if color[neighbour] == Solution.WHITE:
                    dfs(neighbour)
                elif color[neighbour] == Solution.GRAY:
                    is_possible = False

            color[node] = Solution.BLACK
            topological_order.append(node)

        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_order[::-1] if is_possible else []
