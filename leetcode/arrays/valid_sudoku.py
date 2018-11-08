"""
>>> is_valid_sudoku = Solution().isValidSudoku

>>> li = [
...  ["5","3",".",".","7",".",".",".","."],
...  ["6",".",".","1","9","5",".",".","."],
...  [".","9","8",".",".",".",".","6","."],
...  ["8",".",".",".","6",".",".",".","3"],
...  ["4",".",".","8",".","3",".",".","1"],
...  ["7",".",".",".","2",".",".",".","6"],
...  [".","6",".",".",".",".","2","8","."],
...  [".",".",".","4","1","9",".",".","5"],
...  [".",".",".",".","8",".",".","7","9"]
... ]

>>> is_valid_sudoku(li)
True

>>> li = [
...  ["8","3",".",".","7",".",".",".","."],
...  ["6",".",".","1","9","5",".",".","."],
...  [".","9","8",".",".",".",".","6","."],
...  ["8",".",".",".","6",".",".",".","3"],
...  ["4",".",".","8",".","3",".",".","1"],
...  ["7",".",".",".","2",".",".",".","6"],
...  [".","6",".",".",".",".","2","8","."],
...  [".",".",".","4","1","9",".",".","5"],
...  [".",".",".",".","8",".",".","7","9"]
... ]

>>> is_valid_sudoku(li)
False

>>> li = [
...  ["1","3",".",".","7",".",".",".","."],
...  ["6",".",".","1","9","5",".",".","."],
...  [".","9","8",".",".",".",".","6","."],
...  ["8",".",".",".","6",".",".",".","3"],
...  ["4",".","5","8",".","3",".",".","1"],
...  ["7",".",".",".","2",".",".",".","6"],
...  [".","6",".",".",".",".","2","8","."],
...  [".",".",".","7","1","9",".",".","5"],
...  [".",".",".",".","8",".",".","7","9"]
... ]

>>> is_valid_sudoku(li)
True
"""
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        column_dic, box_dic = defaultdict(dict), defaultdict(dict)
        for row_i, row in enumerate(board):
            row_dic = {}
            # print(box_dic)
            for i, v in enumerate(row):

                if v == '.':
                    continue
                box_key = row_i // 3 + 3 * (i // 3)
                if v in row_dic or v in column_dic[i] or v in box_dic[box_key]:
                    return False

                row_dic[v] = ''
                column_dic[i][v] = ''
                box_dic[box_key][v] = ''

        return True

    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid(_li):
            dic = {}
            for _i in _li:
                if _i != '.':
                    if _i in dic:
                        return False
                    dic[_i] = 1
            return True

        for row in board:
            if not is_valid(row):  # validate row
                return False

        for column in zip(*board):
            if not is_valid(column):  # validate column
                return False

        for i in (3, 6, 9):  # validate 3*3 box
            cow_3 = board[i-3:i]
            for j in (3, 6, 9):
                li = []
                for l in cow_3:
                    li.extend(l[j-3:j])
                if not is_valid(li):
                    return False

        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # li = [
    #     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    #     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #     [".", "9", "8", ".", ".", ".", ".", "6", "."],
    #     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    #     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #     [".", "6", ".", ".", ".", ".", "2", "8", "."],
    #     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    # ]
    # print(Solution().isValidSudoku(li))
