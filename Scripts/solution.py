# -*- coding:utf8 -*-
from base_define import TreeNode
from base_define import ListNode
from typing import List
import timeit
import sys
import collections

class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        return None
    def __init__(self, val=0, next=None):
        self.maxNum = 0
        self.aSet = set()
        self.bSet = set()

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.isnumeric;
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        queue = [(root, 0)]
        while len(queue) > 0:
            (node, depth) = queue[0]
            queue.pop(0)
            if len(result) > depth:
                nextList = result[depth]
                nextList.append(node.val)
                result[depth] = nextList
            else:
                result.append([node.val])
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        result.reverse()
        return reversed(result) 
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        result = sorted(dic.items(), key = lambda item:item[1], reverse = True)
        return [x[0] for x in result[:k]]
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                dp[i][j] = max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
        return dp[0][-1]>=0
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k or k == 0:
            return [[]]
        needReverse = False
        nums = range(1, n+1)
        if k == n:
            return [[i for i in nums]]
        if k > n / 2:
            k = n - k
            needReverse = True 
        queue = [[x] for x in nums]
        for _ in range(1, k):
            length = len(queue)
            for j in range(0, length):
                l = queue[j]
                lastIndex = l[-1]
                for num in nums[lastIndex:]:
                    lc = list(l)
                    lc.append(num)
                    queue.append(lc)
            queue = queue[length:]
        if needReverse:
            re = [[i for i in nums if i not in l] for l in queue]
            return re
        return queue
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target <= 0:
            return []
        reselt = set()
        candidates.sort()
        for i, x in enumerate(candidates):
            if x == target:
                reselt.add(tuple([x]))
                candidates = candidates[:i]
                break;
            if x > target:
                candidates = candidates[:i]
                break;
        ca_length = len(candidates)
        queue = [[x] for x in range(0, ca_length)]
        for _ in range(2, len(candidates) + 1):
            length = len(queue)
            for j in range(0, length):
                l = queue[j]
                lastIndex = l[-1]
                for index in range(lastIndex + 1, ca_length):
                    num = candidates[index]
                    lc = [candidates[i] for i in l]
                    lc.append(num)
                    if sum(lc) == target:
                        reselt.add(tuple(lc))                        
                    elif sum(lc) < target:
                        queue.append(l + [index])
                    else:
                        pass
            queue = queue[length:]
        return [list(x) for x in reselt]
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        result = [[nums[0]]]
        for num in nums[1:]:
            length = len(result)
            for i in range(0, length):
                l = result[i]
                for j in range(0, len(l) + 1):
                    newL = list(l)
                    newL.insert(j, num)
                    result.append(newL)
            result = result[length:]
        return [list(y) for y in set([tuple(x) for x in result])]
    def fingerGame(self):
        me = (1, 1)
        you = (1, 1)
        def gameProcess(a, b, myTurn):
            if a[0] == 5 or a[1] == 5:
                return True
            if b[0] == 5 or b[1] == 5:
                return False
            # a = (a[0] % 5, a[1] % 5)
            # b = (b[0] % 5, b[1] % 5)
            if a in self.aSet and b in self.bSet:
                return False
            else:
                self.aSet.add(a)
                self.bSet.add(b)
            if myTurn:
                return gameProcess((a[0] + b[0], a[1]), b, False) or gameProcess((a[0] + b[1], a[1]), b, False) or gameProcess((a[0], b[0] + a[1]), b, False) or gameProcess((a[0], b[1] + a[1]), b, False)
            else:
                return gameProcess(a, (b[0] + a[0], b[1]), True) and gameProcess(a, (b[0] + a[1], b[1]), True) and gameProcess(a, (b[0], a[0] + b[1]), True) and gameProcess(a, (b[0], a[1] + b[1]), True)
        print(gameProcess(me, you, True))
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [[], [nums[0]]]
        subSet = self.subsets(nums[1:])
        return [x+[nums[0]] for x in subSet] + subSet
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def calculateBST(node, rootVal):
            if node == None or (node.left == None and node.right == None):
                node.val += rootVal
                return (node, node.val)
            originNodeVal = node.val
            node.right, rightVal = calculateBST(node.right, 0)
            node.val += (rightVal + rootVal)
            node.left, leftVal = calculateBST(node.left, node.val)
            return (node, leftVal + originNodeVal + rightVal)
        result, _ = calculateBST(root, 0)
        return result
sol = Solution()  
# sys.setrecursionlimit(10000)
# sol.fingerGame()
t = [1,2,3]
# [1,5,1,1]
# t = [[1,3],[3,0,1,2],[2],[0]]
# t = [[1],[2],[3],[0]]
# t = [[1],[2],[3],[]]
m = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# l  = ListNode.listCreater(t)
s = 'abcabcabcs'
# board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]

# [[3,3,3,3,3,3],[2,2,2,2,2,2,2,2,2],[7,2,7,2],[3,2,3,2,2,2,2,2],[3,2,3,2,3,2,3]]
# [[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],,[2,2,2,3,3,3,3],[2,2,7,7],,[3,3,3,3,3,3]]
# [2,2,2,2,3,7] [2,3,3,3,7]
test = [5,2,13,1,3,12,14]
node = TreeNode.treeCreater(test)
print(sol.convertBST(node))






