class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for n in range(len(arr)):
            if arr[n] % 2 == 1 and arr[n+1] % 2 == 1 and arr[n+2] % 2 == 1:
                return True
        return False