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
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            if mid > 0 and mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid+1]:
                left = mid+2
            else:
                right = mid-1
        
        return nums[left]
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
        nums.sort()
        res = 0
        for i in range(len(nums)-1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        list_node = []
        while(head):
            list_node.append(head.val)
            head = head.next
        def compute_tree(start, end):
            if start>end:
                return None
            mid = start + (end-start)//2
            root = TreeNode(list_node[mid])
            root.left = compute_tree(start, mid-1)
            root.right = compute_tree(mid+1, end)
            return root
        root = compute_tree(0, len(list_node)-1)
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
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i = click[0]
        j = click[1]
        def clickBoard(board, i, j):
            if i >= len(board) or i < 0 or j >= len(board[i]) or j < 0:
                return board
            if board[i][j] == "M":
                board[i][j] = "X"
                return board
            if board[i][j] == "B" or board[i][j] in [str(num) for num in range(1, 9)]:
                return board
            if board[i][j] == "E":

                def isMine(board, i, j):
                    if i >= len(board) or i < 0 or j >= len(board[i]) or j < 0:
                        return False
                    return board[i][j] in ["M", "X"]

                aroundArray = [(i - 1, j - 1), (i, j - 1), (i + 1, j - 1), (i - 1, j), (i + 1, j), (i - 1, j + 1), (i, j + 1), (i + 1, j + 1)]
                mineCount = 0
                for l, r in aroundArray:
                    if isMine(board, l, r):
                        mineCount += 1
                if mineCount > 0:
                    board[i][j] = str(mineCount)
                    return board
                else:
                    board[i][j] = "B"
                    for l, r in aroundArray:
                        board = clickBoard(board, l, r)
                    return board
            return board
        return clickBoard(board, i, j)


    def repeatedSubstringPattern(self, s):    
        for i in range(2, len(s) + 1):
            if len(s) % i == 0:
                subLength = int(len(s) / i)
                targetString = s[0:subLength]
                repeat = True
                for j in range(1, i):
                    if targetString != s[j * subLength: (j + 1) * subLength]:
                        repeat = False
                        break;
                if repeat:
                    return True
            else:
                continue 
        return False
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort();
        if sum(nums) % k != 0:
            return False
        subSum = sum(nums) // k
        if nums[-1] > subSum:
            return False
        


sol = Solution()  
t = [2,2,3,4,5,6,7,8,9]
# l  = ListNode.listCreater(t)
s = 'abcabcabcs'
# board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
print(sol.canPartitionKSubsets(t, 4))





