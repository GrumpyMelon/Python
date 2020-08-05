from tree_node import TreeNode
from typing import List

class Solution(object):
    def restoreString(self, s, indices):
        rs = [0 for _ in range(len(s))]

        for (i, index) in enumerate(indices):
            rs[int(index)] = s[i]
        return "".join(rs)
    def minFlips(self, target):
        rs = 0
        flag = 1
        for s in target:
            if int(s) == flag:
                rs += 1
                flag = int(not bool(flag))

        return rs
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root or not root.left and not root.right: 
            return 0
        
        def _dfs(root):
            """获取左右子树中叶子结点到当前节点的距离"""
            if not root: 
                return {}
            # 叶子节点
            if not root.left and not root.right: 
                return {root: 0}
            
            left_leaf = _dfs(root.left)
            right_leaf = _dfs(root.right)
            # 距离加1
            for k, v in left_leaf.items(): 
                left_leaf[k] = v + 1
            for k, v in right_leaf.items(): 
                right_leaf[k] = v + 1
            
            for lk, lv in left_leaf.items():
                for rk, rv in right_leaf.items():
                    if lv + rv <= distance:
                        self.ans += 1
            
            # 合并左右子树的叶子节点，向上返回
            left_leaf.update(right_leaf)
            return left_leaf

        self.ans = 0
        _dfs(root)
        return self.ans
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        if len(transactions) < 2:
            return None
        result = [t for t in transactions if int(t.split(',')[2]) > 1000]
        transactions = [t for t in transactions if int(t.split(',')[2]) <= 1000]
        transGroupByName = {}
        for trans in transactions:
            sepe = trans.split(',')
            if sepe[0] in transGroupByName:
                transGroupByName[sepe[0]].append(sepe)
            else:
                transGroupByName[sepe[0]] = [sepe]
        print(transGroupByName)
        for tranName, trans in enumerate(transGroupByName):
            if len(trans) < 2:
                pass
            else:
                stack = []
                for t in trans:
                    

        def takeTime(elem):
            return int(elem.split(',')[1])
        
        # 按照交易名划分所有的交易。

        transactions.sort(key=takeTime)
        last = transactions[0].split(',')
        for trans in transactions[1:]:
            t = trans.split(',')
            if int(t[1]) - int(last[1]) < 60 and t[0] == last[0]:
                if not result[-1] == last:
                    result.append(last)
                result.append(trans)
        return result

sol = Solution()  
treeArray = ["alice,20,800,mtv","alice,50,100,beijing"]
# t = ["alice,20,800,mtv","alice,50,100,mtv", "alice,70,100,beijing"]
t = ["alice,20,800,mtv","join,50,100,mtv", "alice,70,100,beijing"]

# node = TreeNode.treeCreater(treeArray)

print(sol.invalidTransactions(t))





