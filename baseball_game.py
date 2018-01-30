class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for ch in ops:
            if ch == 'C':
                stack.pop()
            elif ch == '+':
                stack.append(sum(stack[-2:]))
            elif ch == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(ch))

        return sum(stack)
