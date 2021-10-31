"""
URL of problem:
https://leetcode.com/problems/task-scheduler/
"""


import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_details = {}
        for task in tasks:
            # Use a negative count to emulate a max heap
            if task not in task_details:
                task_details[task] = -1
            else:
                task_details[task] -= 1

        # Push (remaining cooldown time, count, task)
        # The cooldown time will be the first
        # priority and then the count for the task
        heap, current_time = [], 0
        for task, count in task_details.items():
            heapq.heappush(heap, (0, count, task))

        # Alternate approach:
        # Here, the cooldown time is not decremented.
        # Rather, the current time is incremented and
        # that is used as a basis for selecting the
        # next task. Still giving problems though.
        # while heap:
        #     if heap[0][0] > current_time:
        #         print("idle -> ", end=" ")
        #     else:
        #         _, count, top_task = heapq.heappop(heap)
        #         print(f"{top_task} -> ", end=" ")
        #         if count + 1 != 0:
        #             heapq.heappush(heap, (n + current_time + 1, count + 1, top_task))

        #     current_time += 1

        # return current_time

        while heap:
            # If the top priority task doesn't have a remaining
            # cooldown time of 0, then the CPU has to be idle
            if heap[0][0] == 0:
                _, count, top_task = heapq.heappop(heap)
                print(f"{top_task} -> ", end=" ")
                if count + 1 != 0:
                    heapq.heappush(heap, (n + 1, count + 1, top_task))
            else:
                print("idle -> ", end=" ")

            # Decrement the cooldown times and heapify the heap
            are_cooldowns_updated = False
            for idx, (cooldown_left, count, task) in enumerate(heap):
                if cooldown_left != 0:
                    heap[idx] = (max(0, cooldown_left - 1), count, task)
                    are_cooldowns_updated = True

            if are_cooldowns_updated:
                heapq.heapify(heap)

            current_time += 1

        print()
        return current_time


def main():
    print(
        Solution().leastInterval(
            ["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"], n = 7
        )
    )


if __name__ == "__main__":
    main()