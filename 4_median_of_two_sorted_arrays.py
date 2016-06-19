class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        i = 0
        j = 0

        while 1:
            if i >= len(nums1) and j >= len(nums2):
                break
            elif i >= len(nums1):
                num = nums2[j]
                j += 1
            elif j >= len(nums2):
                num = nums1[i]
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    num = nums1[i]
                    i += 1
                else:
                    num = nums2[j]
                    j += 1
            nums.append(num)

        if len(nums) % 2 == 0:
            return float((nums[len(nums)/2-1] + nums[len(nums)/2])) / 2
        else:
            return nums[len(nums)/2]

#test
test = Solution()
nums1 = []
nums2 = [1]
print nums1
print nums2
print test.findMedianSortedArrays(nums1, nums2)
print "\n"

nums1 = [1,2,3]
nums2 = [2,4,6]
print nums1
print nums2
print test.findMedianSortedArrays(nums1, nums2)
print "\n"