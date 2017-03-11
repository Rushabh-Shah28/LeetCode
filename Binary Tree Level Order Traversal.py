# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        if root is None: 
            return []
            
        queue = [[root]]
        for level in queue:
            record = []
            for node in level:
                if node.left: 
                    record.append(node.left)
                if node.right: 
                    record.append(node.right)
            if record: 
                queue.append(record)
                
    
        return [[x.val for x in level] for level in queue]

        
        
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """