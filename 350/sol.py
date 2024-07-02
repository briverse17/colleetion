class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        # count occurrences of element in each array
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        # identify elements that appear in both arrays
        common = set(counter1.keys()).intersection(counter2.keys())
        # "as many times as it shows in both arrays" means
        # the smaller number of occurences
        intersection = []
        for c in common:
            intersection += [c] * min(counter1[c], counter2[c])
        return intersection
