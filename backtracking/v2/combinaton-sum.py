class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        current = []

        candidates.sort()

        def dfs(i, k):
            if k == target:
                solutions.append(current[:])
                return

            for j in range(i, len(candidates)):
                if k + candidates[j] > target:
                    continue

                current.append(candidates[j])
                dfs(j, k + candidates[j])

                current.pop()              

        dfs(0, 0)
        return solutions