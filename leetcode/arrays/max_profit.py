"""
>>> max_profit = Solution().maxProfit

>>> max_profit([])
0

>>> max_profit([1])
0

>>> max_profit([1,2,3,4,5])
4

>>> max_profit([6,5,4,3,2,1])
0

>>> max_profit([7,1,5,3,6,4])
7

"""


class Solution:

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for index, price in enumerate(prices):
            pre_index = index - 1
            pre_price = prices[pre_index]
            if pre_price < price and pre_index >= 0:

                profit += price - pre_price

        return profit


if __name__ == '__main__':
    import doctest
    doctest.testmod()
