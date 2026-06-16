class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        solutions = []
        current = []

        candidates.sort()

        def backtrack(k, sum):
            if sum == target:
                solutions.append(current.copy())
                return

            for i in range(k, n):
                if sum + candidates[i] > target:
                    return

                current.append(candidates[i])
                backtrack(i, sum + candidates[i])
                current.pop()

        backtrack(0, 0)
        return solutions