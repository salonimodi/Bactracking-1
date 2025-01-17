class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []

        def helper(remainingSum, path, curr):
            # base
            if remainingSum < 0:
                return
            
            if remainingSum == 0:
                self.result.append(path.copy())
                return

            # logic
            for idx in range(curr, len(candidates)):
                path.append(candidates[idx])
                helper(remainingSum - candidates[idx], path, idx)
                path.pop()
        
        helper(target,[], 0)
        return self.result




            
        


