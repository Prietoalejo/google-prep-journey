from typing import List

class Solution:
    """
    Problem: Contains Duplicate 
    Language: Python Difficulty: Easy
    Time: O() | Space: O(n)
    """
    def contains_duplicate(self, nums: List[int]) -> bool:
        """
        Docstring for containsDuplicate
        
        :param self: Description
        :param nums: Description
        :type nums: List[int]
        :return: Description
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    def contains_duplicate1(self, nums: List[int]) -> bool:
        """
        Docstring for contains_duplicate1
        
        :param self: Description
        :param nums: Description
        :type nums: List[int]
        :return: Description
        :rtype: bool
        """
        hash = set()
        for i in nums:
            if i in hash:
                return True
            else:
                hash.add(i)
        return False

sol = Solution()
l1 = [1,2,3,4,1]
print(sol.contains_duplicate1(nums=l1))

print (len(l1))