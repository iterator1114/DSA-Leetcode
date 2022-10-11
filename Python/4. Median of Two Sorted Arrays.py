# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=[]
        for i in range(len(nums1)):
            l.append(nums1[i])
        for j in range(len(nums2)):
            l.append(nums2[j])
        l.sort()
        n=len(l)
        if(n%2==0):
            return (l[(n//2)-1]+l[(n//2)])/2
        else:
            return (l[n//2])
