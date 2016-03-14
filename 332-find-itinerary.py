import collections

class Solution(object):
    @classmethod
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]

tickets = [["A","C"],["B","C"],["JFK","A"],["JFK","D"],["C","JFK"],["C","D"],["D","A"],["D","B"]]
print(Solution().findItinerary(tickets))
