class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # it's always possible to turn `nums` into
        # an array with elements of the same value
        # within three moves
        if len(nums) <= 4:
            return 0

        # identify the 4 smallest and 4 largest values
        nums.sort()
        smallest = nums[:4]
        largest = nums[-4:]
        
        # calculate pairwise differences
        # the result is the minimum among them
        result = min(l - s for s, l in zip(smallest, largest))

        # you can also do the steps above using min- and max-heap
        # remember to keep the two arrays in the same order (ascending/descending)

        # why 4? and why must `smallest` and `largest` be in the same order?
        # > the ultimate goal is to minimize the difference between the largest and smallest values
        #   and for that to be feasible, we need to attack right at the largest and smallest values
        # > roughly speaking, the (s, l) pairs we are interested in are as follows
        #   1st smallest - 4th largest
        #   2nd smallest - 3rd largest
        #   3rd smallest - 2nd largest
        #   4th smallest - 1st largest
        #   (1st -est sounds dumb, just for alignment)
        # > whichever pair yields the minimum difference
        #   we can always change the other pairs so that
        #   the final largest and smallest values of `nums` are `s` and `l`
        #   within three moves
        return result
