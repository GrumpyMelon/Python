
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    @classmethod
    def treeCreater(cls, array, index=0):
        if index < len(array) and array[index] != -1:
            treeNode = TreeNode(array[index])
            treeNode.left = TreeNode.treeCreater(array, 2 * index + 1)
            treeNode.right = TreeNode.treeCreater(array, 2 * index + 2)
            return treeNode
        return None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    @classmethod
    def listCreater(cls, array):
        l = ListNode(0)
        head = l
        for i in array:
            head.next = ListNode(i)
            head = head.next
        return l.next