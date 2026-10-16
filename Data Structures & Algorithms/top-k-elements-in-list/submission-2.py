class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch , 0) + 1
        
        sorted_freq = sorted(freq, key=freq.get, reverse=True)

        return sorted_freq[:k]