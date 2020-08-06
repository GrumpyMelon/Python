# -*- coding:utf8 -*-
from tree_node import TreeNode
from typing import List
import sys

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
        result = []
        transGroupByName = {}
        for trans in transactions:
            sepe = trans.split(',')
            if sepe[0] in transGroupByName:
                transGroupByName[sepe[0]].append(trans)
            else:
                transGroupByName[sepe[0]] = [trans]

        def takeTime(elem):
            return int(elem.split(',')[1])

        for trans in transGroupByName.values():
            crtR = set([])
            trans.sort(key=takeTime)
            if len(trans) < 2:
                for t in trans:
                    if int(t.split(',')[2]) > 1000:
                        crtR.add(t)
            else:
                for index, t in enumerate(trans):
                    newT = t.split(',')
                    if int(newT[2]) > 1000:
                        crtR.add(t)
                    for former in trans[0:index]:
                        newF = former.split(',')
                        if (newT[3] != newF[3] and int(newT[1]) - int(newF[1]) <= 60):
                            crtR.add(former)
                            crtR.add(t)
            if len(crtR) > 0:
                result.extend(crtR)
        return result
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        length = len(cardPoints)
        if k == length:
            return sum(cardPoints)
        l = [cardPoints[0]] * k
        r = [cardPoints[length - 1]] * k
        for i in range(1, k):
            l[i] = l[i - 1] + cardPoints[i]
            r[i] = r[i - 1] + cardPoints[length - 1 - i]
        res = max(l[k - 1], r[k - 1])
        for i in range(0, k):
            res = max(res, l[i] + r[k - i - 2]) 
        return res;

sol = Solution()  
t = [1120, 2,3,4,5,6]

# node = TreeNode.treeCreater(treeArray)

print(sol.maxScore(t, 3))





