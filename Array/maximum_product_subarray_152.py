"""
URL of problem:
https://leetcode.com/problems/maximum-product-subarray/
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = nums[0]
        products_so_far = [[nums[0], nums[0]]]
        for idx, num in enumerate(nums[1:]):
            prod_with_min = num * products_so_far[idx][0]
            prod_with_max = num * products_so_far[idx][1]

            products_so_far.append([
                min(prod_with_min, num, prod_with_max),
                max(prod_with_min, num, prod_with_max)
            ])

            max_product = max(max_product, *products_so_far[-1])

        return max_product


    def maxProduct_2ndPass(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return -1


def main():
    print(Solution().maxProduct([2, 3, -2, -4]))


if __name__ == "__main__":
    main()
