class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # monitor the height (or depth, whichever)
        # of the directory
        # `height = 0` means we are at "Main"
        height = 0
        for log in logs:
            # "./" is a stationary operation
            # => keep `height` the same
            if log != "./":
                # "../" is a backward operation
                # => reduce `height` by 1
                # but if we're already at "Main", do nothing
                if log == "../":
                    height = max(height - 1, 0)
                # otherwise, it's a normal forward operation
                # => increase `height` by 1
                else:
                    height += 1

        return height
