class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        last_count = 0
        for x in words:
            count = 0
            for n in x:
                if n not in allowed:
                    count += 1
            if count == 0:
                last_count += 1

        return (last_count)

