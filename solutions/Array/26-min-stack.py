    # 155. Min Stack
    # https://leetcode.com/problems/min-stack/
    # Time Complexity - O(1) for all operations
    # Space Complexity - O(n) where n is the number of elements in the stack
    # Category - Array
    # Hint - Use two stacks, one for the elements and one for the minimum elements, when pushing an element, push it to the elements stack and if it is smaller than or equal to the top of the minimum stack, push it to the minimum stack, when popping an element, pop it from the elements stack and if it is equal to the top of the minimum stack, pop it from the minimum stack, when getting the top element, return the top of the elements stack, when getting the minimum element, return the top of the minimum stack
    # video - https://www.youtube.com/watch?v=RfMroCV17-4

    class MinStack:

        def __init__(self):
            self.stk = []
            self.min_stk = []

        def push(self, value: int) -> None:
            self.stk.append(value)

            if not self.min_stk:
                self.min_stk.append(value)
            elif self.min_stk[-1] < value:
                self.min_stk.append(self.min_stk[-1])
            elif self.min_stk[-1] >= value:
                self.min_stk.append(value)

        def pop(self) -> None:
            self.stk.pop()
            self.min_stk.pop()

        def top(self) -> int:
            return self.stk[-1]

        def getMin(self) -> int:
            return self.min_stk[-1]