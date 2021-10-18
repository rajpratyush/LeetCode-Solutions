# Time:  O(n)
# Space: O(n)



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = defaultdict(Node)
        dic[None] = None
        visited = set()
        dq = deque()
        if node:
            dq.append(node)
        while dq:
            cur = dq.popleft()
            if cur not in visited:
                visited.add(cur)
                dic[cur].val = cur.val
                for nd in cur.neighbors:
                    dic[cur].neighbors.append(dic[nd])
                    dq.append(nd)
        return dic[node]

