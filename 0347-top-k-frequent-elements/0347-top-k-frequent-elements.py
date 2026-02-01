class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap
        # add each adn thenr eturn the highest 2 values

        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        sorted_by_value = sorted(d.items(), key=lambda x:x[1], reverse=True)
        top_k_keys = [k for k, v in sorted_by_value[:k]]   
        return top_k_keys