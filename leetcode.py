# TWO-SUM

def twoSum(nums: list[int], target: int) -> list[int]:
    check = dict()
    for i in range(len(nums)):
        if target - nums[i] in check:
            return [check[target - nums[i]], i]
        else:
            check[nums[i]] = i

# Test the function with various test cases
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(twoSum([3, 3], 6))          # Output: [0, 1]
print(twoSum([1, 2, 3, 4, 5], 9)) # Output: [3, 4]
print(twoSum([1, 2, 3, 4, 5], 10))# Output: []

# PALINDROME 

def isPalindrome(x: int) -> bool:
    if x < 0: return False
    reversed_num = 0
    temp = x
    while temp != 0:
        reversed_num = reversed_num * 10 + (temp % 10)
        temp //= 10
    return reversed_num == x

testCases = [-10, 123, 121, 676756767, 1293128937123]
for num in testCases:
    print(isPalindrome(num))

# Valid Parenthesis

def isValid(s: str) -> bool:
        Map = {")" : "(" , "]" : "[", "}" : "{"}
        stack = []
        for c in s: 
             if c not in Map:
                  stack.append(c)
                  continue
             elif not stack or stack[-1] != Map[c]:
                return False
             stack.pop()
        return not stack

