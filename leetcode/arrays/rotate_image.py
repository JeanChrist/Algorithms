"""
>>> rotate = Solution().rotate

>>> matrix = [
...   [1,2,3],
...   [4,5,6],
...   [7,8,9]
... ]

>>> rotate(matrix)
>>> matrix
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]

>>> matrix = [
...   [ 5, 1, 9,11],
...   [ 2, 4, 8,10],
...   [13, 3, 6, 7],
...   [15,14,12,16]
... ]

>>> rotate(matrix)
>>> matrix
[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

>>> matrix = [
...   [1,2],
...   [4,5],
... ]

>>> rotate(matrix)
>>> matrix
[[4, 1], [5, 2]]

>>> matrix = [[16, 49, 27, 12, 54, 13, 2, 69, 8],
...           [17, 33, 47, 50, 41, 8, 17, 10, 31],
...           [29, 30, 20, 39, 59, 25, 21, 79, 35],
...           [24, 42, 75, 71, 75, 60, 18, 7, 35],
...           [48, 26, 24, 58, 60, 75, 25, 30, 36],
...           [50, 49, 48, 1, 14, 14, 22, 71, 75],
...           [48, 28, 9, 3, 69, 68, 15, 61, 63],
...           [76, -1, 6, 31, 49, 50, 73, 43, 30],
...           [68, 69, 62, 24, 39, 47, 8, 57, 78]]

>>> rotate(matrix)
>>> matrix
[[68, 76, 48, 50, 48, 24, 29, 17, 16], [69, -1, 28, 49, 26, 42, 30, 33, 49], [62, 6, 9, 48, 24, 75, 20, 47, 27], [24, 31, 3, 1, 58, 71, 39, 50, 12], [39, 49, 69, 14, 60, 75, 59, 41, 54], [47, 50, 68, 14, 75, 60, 25, 8, 13], [8, 73, 15, 22, 25, 18, 21, 17, 2], [57, 43, 61, 71, 30, 7, 79, 10, 69], [78, 30, 63, 75, 36, 35, 35, 31, 8]]
"""


class Solution:

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        j_range = length - length // 2
        for i in range(length // 2):
            for j in range(j_range):
                left, top = i, j
                right, bottom = ~left, ~top
                # print(left, top, right, bottom)
                (matrix[top][right],
                 matrix[right][bottom],
                 matrix[bottom][left],
                 matrix[left][top]) = (matrix[left][top],
                                       matrix[top][right],
                                       matrix[right][bottom],
                                       matrix[bottom][left])

    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = zip(*matrix[::-1])

    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)

        for i in range(length**2//4):

            left, top = i // (length // 2), i % (length // 2)
            right, bottom = length - 1 - left, length - 1 - top
            # print(left, top, right, bottom)
            (matrix[top][right],
             matrix[right][bottom],
             matrix[bottom][left],
             matrix[left][top]) = (matrix[left][top],
                                   matrix[top][right],
                                   matrix[right][bottom],
                                   matrix[bottom][left])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # matrix = [[16, 49, 27, 12, 54, 13, 2, 69, 8],
    #           [17, 33, 47, 50, 41, 8, 17, 10, 31],
    #           [29, 30, 20, 39, 59, 25, 21, 79, 35],
    #           [24, 42, 75, 71, 75, 60, 18, 7, 35],
    #           [48, 26, 24, 58, 60, 75, 25, 30, 36],
    #           [50, 49, 48, 1, 14, 14, 22, 71, 75],
    #           [48, 28, 9, 3, 69, 68, 15, 61, 63],
    #           [76, -1, 6, 31, 49, 50, 73, 43, 30],
    #           [68, 69, 62, 24, 39, 47, 8, 57, 78]]
    # Solution().rotate(matrix)
    # print(matrix)