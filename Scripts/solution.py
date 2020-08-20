# -*- coding:utf8 -*-
from base_define import TreeNode
from base_define import ListNode
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
        # 对于 dfs(root,distance)，同时返回：
        # 每个叶子节点与 root 之间的距离
        # 以 root 为根节点的子树中好叶子节点对的数量
        def dfs(root: TreeNode, distance: int) -> (List[int], int):
            depths = [0] * (distance + 1)
            isLeaf = not root.left and not root.right
            if isLeaf:
                depths[0] = 1
                return (depths, 0)
            
            leftDepths, rightDepths = [0] * (distance + 1), [0] * (distance + 1)
            leftCount = rightCount = 0

            if root.left:
                leftDepths, leftCount = dfs(root.left, distance)
            if root.right:
                rightDepths, rightCount = dfs(root.right, distance)
            
            for i in range(distance):
                depths[i + 1] += leftDepths[i]
                depths[i + 1] += rightDepths[i]
            
            cnt = 0
            for i in range(distance + 1):
                for j in range(distance - i - 1):
                    cnt += leftDepths[i] * rightDepths[j]
            
            return (depths, cnt + leftCount + rightCount)
        

        list11, ret = dfs(root, distance)
        print(list11)
        return ret
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
        def run(cardPoints,k):
            min_num = len(cardPoints)-k
            t = k + 1
            rl = []
            sum2 = sum1 = sum(cardPoints[:min_num])
            for i in range(0,t-1):
                sum2 = sum2 + cardPoints[min_num+i] - cardPoints[i]
                if sum2 < sum1:
                    sum1 = sum2
            return sum(cardPoints) - sum1
        if len(cardPoints) <= k:
            return sum(cardPoints)
        elif len(cardPoints) >= 2*k:
            cardPoints_new = cardPoints[:k]+cardPoints[len(cardPoints)-k:]
            return run(cardPoints_new,k)
        else:
            return run(cardPoints,k)
    def singleNonDuplicate(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]
        i = int((length - 1) / 2)
        isOdd = i % 2 != 0
        if nums[i] == nums[i - 1]:
            if isOdd:
                return self.singleNonDuplicate(nums[i+1:])
            else:
                return self.singleNonDuplicate(nums[:i-1])
        else:
            if nums[i] == nums[i + 1]:
                if isOdd:
                    return self.singleNonDuplicate(nums[:i])
                else:
                    return self.singleNonDuplicate(nums[i+2:])
            else:
                return nums[i]
    def parseBoolExpr(self, expression):
        if len(expression) == 0:
            return False
        stack = []
        for ch in expression:
            if ch == ')':
                hasT, hasF = False, False
                for i in range(len(stack) - 1, -1, -1):
                    sCh = stack[i]
                    if sCh == "(":
                        oCh = stack[i - 1]
                        stack = stack[:i-1]
                        newCh = ""
                        if oCh == "&":
                            newCh = "f" if hasF else "t"
                        elif oCh == "|":
                            newCh = "t" if hasT else "f"
                        else:
                            newCh = "t" if hasF else "f"
                        stack.append(newCh)
                        break;
                    elif sCh == "t":
                        hasT = True
                    elif sCh == "f":
                        hasF = True
                    else:
                        pass
            else:
                stack.append(ch)
        if stack[0] == "t":
            return True
        else:
            return False
    def triangleNumber(self, nums):
        if len(nums) < 3:
            return 0
        nums.sort()
        result = 0
        cursor = list(range(1, len(nums) + 1))
        print(cursor)
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                while cursor[j] < len(nums) and nums[i] + nums[j] > nums[cursor[j]]:
                    cursor[j] += 1
                result += (cursor[j] - j - 1)
        return result
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        def createTree(l):
            length = len(l)
            if length == 1:
                return TreeNode(l[0])
            if length == 0:
                return None
            i =  int(length / 2)
            root = TreeNode(l[i])
            root.left = createTree(l[:i])
            root.right = createTree(l[i+1:])
            return root
        root = createTree(l)
        return root
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = len(s)
        for (i, c) in enumerate(s[:-1]):
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break;
            if s[i] == s[i + 1]:
                left = i - 1
                right = i + 2
                result += 1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        result += 1
                        left -= 1
                        right += 1
                    else:
                        break;

        return result
sol = Solution()  
# t = [2,2,3,4,5,6,7,8,9]
# l  = ListNode.listCreater(t)
s = 'abc'
print(sol.countSubstrings(s))





