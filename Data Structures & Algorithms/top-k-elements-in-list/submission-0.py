from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        return [i for i, freq in c.most_common(k)] 