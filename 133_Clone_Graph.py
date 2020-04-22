
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'DICT':
        if node is None:
            return None 
        if len(node.neighbors)==0:
            return Node(1)
        queue = [node]
        his =set()
        his_node_c = set()
        new_node_dict = {}
        # result_adj_list = []
        while queue:
            node=queue.pop(0)
            if node.val in his:
                continue
            # result_adj = []
            if node.val not in his_node_c:
                new_node = Node(node.val)
                new_node_dict[new_node.val]= new_node
                his_node_c.add(new_node.val)
            else:
                new_node = new_node_dict[node.val]
            for n in node.neighbors:
                if n.val in his_node_c:
                    neighbor_node = new_node_dict[n.val]
                else:
                    neighbor_node = Node(n.val)
                    new_node_dict[neighbor_node.val]= neighbor_node
                    his_node_c.add(neighbor_node.val)
                new_node.neighbors.append(new_node_dict[neighbor_node.val])
                # result_adj.append(n.val)
                if n.val not in his:
                    queue.append(n)
            his.add(node.val)
            # result_adj_list.append(result_adj)
        # print(result_adj_list)
        # print(node.val)
        return new_node_dict


if __name__ == "__main__":
    node_list=[[2,4],[1,3],[2,4],[1,3]]
    # nodes = []
    # for i,n in enumerate(node_list):
    #     node = Node(i,n)
    #     nodes.append(node)
    node_1 = Node(1)
    print(node_1)
    node_2 = Node(2)
    print(node_2)
    node_3 = Node(3)
    print(node_3)
    node_4 = Node(4)
    print(node_4)
    node_1.neighbors=[node_2,node_4]
    node_2.neighbors=[node_1,node_3]
    node_3.neighbors=[node_2,node_4]
    node_4.neighbors=[node_1,node_3]
    node_dict = Solution().cloneGraph(node_1)
    for k in node_dict:
        print(node_dict[k])