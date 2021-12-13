class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        
        visited = {}
        visited[head] = Node(head.val)
        
        def copyNode(node, visited):
            if not node:
                return 
            if node in visited:
                return visited[node]
            new_node = Node(node.val)
            visited[node] = new_node
            return new_node
        cur = head
        while cur:
            visited[cur].next = copyNode(cur.next, visited)
            visited[cur].random = copyNode(cur.random, visited)
            cur = cur.next
        return visited[head]