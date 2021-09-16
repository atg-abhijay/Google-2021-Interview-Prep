"""
URL of problem:
https://leetcode.com/problems/kth-smallest-instructions/
"""


import heapq
from collections import deque
from math import comb


class PathWrapper:
    def __init__(self, path:int):
        self.val = path


class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        target_row, target_col = destination
        num_combinations = comb(target_row + target_col, target_row)
        if k > int(num_combinations/2):
            k = num_combinations - k + 1
            PathWrapper.__lt__ = lambda self, other: self.val < other.val
        else:
            # Use a reverse comparison to make
            # larger values smaller so that these
            # larger values are popped from the heap,
            # thereby only leaving the smaller values
            PathWrapper.__lt__ = lambda self, other: other.val < self.val

        grid_paths = [[[] for _ in range(target_col+1)] for _ in range(target_row+1)]
        self.determinePaths(grid_paths, [target_row, target_col, k])
        kth_path = heapq.heappop(grid_paths[0][0]).val
        kth_path_bits = bin(kth_path)[2:].zfill(target_row+target_col)
        return ''.join(["H" if bit == "0" else "V" for bit in kth_path_bits])
        # str_kth_path = []
        # for bit in str(kth_path.val):
        #     str_kth_path.append("H" if bit == "0" else "V")

        # return ''.join(str_kth_path)
        # return ''.join(["H" for bit in str(kth_path) if bit == "0" else "V"])
        # return ''.join(heapq.heappop(grid_paths[0][0]).val)


    def determinePaths(self, grid_paths, constants):
        target_row, target_col, k = constants
        backward_dirns = [(0, -1), (-1, 0)]
        enqueued = [[0 for _ in range(target_col+1)] for _ in range(target_row+1)]
        queue = deque([(target_row, target_col)])
        grid_paths[target_row][target_col] = [PathWrapper(0)]
        # num_iterations = 0
        while queue:
            row_idx, col_idx = queue.popleft()
            if [row_idx, col_idx] == [0, 0]:
                break
            # num_iterations += 1
            # print(num_iterations, (row_idx, col_idx))
            for decr_x, decr_y in backward_dirns:
                nbr_row, nbr_col = row_idx + decr_x, col_idx + decr_y
                within_bounds = 0 <= nbr_row <= target_row and 0 <= nbr_col <= target_col
                if not within_bounds:
                    continue

                if not enqueued[nbr_row][nbr_col]:
                    queue.append((nbr_row, nbr_col))
                    enqueued[nbr_row][nbr_col] = 1

                dirn = "H" if decr_y == -1 else "V"
                steps_away = target_row + target_col - nbr_row - nbr_col - 1
                for path in grid_paths[row_idx][col_idx]:
                    nbr_path = 1 << steps_away if dirn == "V" else 0
                    nbr_path |= path.val
                    heap = grid_paths[nbr_row][nbr_col]
                    heapq.heappush(heap, PathWrapper(nbr_path))
                    if len(heap) > k:
                        heapq.heappop(heap)


def main():
    print(Solution().kthSmallestPath([2, 3], 1))


if __name__ == "__main__":
    main()
