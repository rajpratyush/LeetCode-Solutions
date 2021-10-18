// Time Complexity: O(n)
// Space Complexity: O(n)

/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
    std::unordered_map <Node*, Node*> m_storage;
public:
    Node* cloneGraph(Node* node) {
        if(!node) return nullptr;
        if(m_storage[node]) return m_storage[node];
        m_storage[node] = new Node(node->val);
        for(int i = 0; i < node->neighbors.size(); ++i) {
             m_storage[node]->neighbors.push_back(cloneGraph(node->neighbors[i]));
        }
        return m_storage[node];       
    }
};