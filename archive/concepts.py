class listNode:
    def __init__(self, value: int = 0, next = None):
        self.value = value
        self.next = next
    def print(self):
        cur = self
        while cur:
            print(cur.value, end = "->" if cur.next else "\n")
            cur = cur.next

node1 = listNode(2)
node2 = listNode(4)
node3 = listNode(6)

node1.next = node2
node2.next = node3
node3.next = None

node1.print()

x = [1,2,3,4,5]
print(x[:4])

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
x = fib(5)
print(x)

s = "abc"

i = 0
j = 1


s = "123456789"
# starting at index 1 and ending at index 4 (not including index 5)
print(s[1:5])
print("".join(reversed(s)))
print(s[::-1])
strs = ["a","bb","ccc"]
max_str = max(strs, key=len)
print(max_str)

x = "hello"
x_reversed = ""
for i in range(len(x) - 1, -1, -1):
    x_reversed += x[i]
print(x)
print(x_reversed)

check = dict()

print(check)

x = [0, 1]

u, v = x

print(u)
print(v)

def numIslands(self, grid: list[list[str]]) -> int:
    if not grid: 
        return 0
    
    def dfs(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return 
        else:
            grid[i][j] == '0' # marking it as visited
            
            # explore the neigboring elements
            dfs(grid, i, j + 1) # right
            dfs(grid, i, j - 1) # left
            dfs(grid, i - 1, j) # up
            dfs(grid, i + 1, j) # down

    num_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num_islands += 1
                dfs(grid[i][j])
    return num_islands

def is_palindrome(s: str) -> bool:
    left = 0 
    right = len(s) - 1
    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -=1
    return True

print("palindrom checking lolz")
s = "abc"
print(s[::-1])
print(s[0:0])


def palindromic_substrings(s: str) -> list[str]:
    palindromes = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.append(s[i:j])
    return palindromes
print("Palindromic Substrings")
print(palindromic_substrings("abcd"))
print(palindromic_substrings("racecar"))

def is_alpha(s: str) -> int: # returning 0 if its alpha and returning the index of the char that is not in order
    for i in range(len(s) - 1): # going up to second to last char
        if s[i] > s[i + 1]:
            return s[i + 1] # this element is out of order
    return 0 # the string is in alphabetical order
print("Is the string in order")
print(is_alpha("abc"))
print(is_alpha("abdc"))

def is_alpha_2(s: str) -> bool:
    for i in range(len(s) - 1, 0, -1):
        if s[i] < s[i - 1]:
            return False
    return True
print("check if string is in alpha order")
print(is_alpha_2("abc"))
print(is_alpha_2("abdc"))

def length_of_longest_substring(s: str) -> int:
    charSet = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        longest = max(longest, len(charSet))
    return longest

print(length_of_longest_substring("abcabcbb"))

def binary_search(nums: list[int], target) -> bool: 
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return True
    return False

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(binary_search(nums, target))  # Expected output: True
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 1
print(binary_search(nums, target))  # Expected output: True
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
print(binary_search(nums, target))  # Expected output: False

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    checkS = dict()
    checkT = dict()
    for i in range(len(s)):
        checkS[s[i]] = checkS.get(s[i], 0) + 1
        checkT[t[i]] = checkT.get(t[i], 0) + 1
    return checkS == checkT

print(is_anagram("daniel", "adieln")) # true
print(is_anagram("car", "bat")) # false

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue # skipping duplcicate starting points
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                ans.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else: # total > 0
                right -= 1
    return ans

input1 = [-1, 0, 1, 2, -1, -4]
output1 = threeSum(input1)
print("Test Case 1:", output1)  # Expected: [[-1, -1, 2], [-1, 0, 1]]
input2 = [1, 2, -2, -1]
output2 = threeSum(input2)
print("Test Case 2:", output2)  # Expected: []

def characterReplacement(s: str, k: int) -> int:
    max_length = 0
    max_count = 0

    left = 0

    count = dict()

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])
        # (right - left + 1) - max_count is basically how many characters that are present that can be replaced to make the substring one continuos letter, if it is greater than k (the number of characters we can replace) we have to iterate the window by 1 from the left side and reduce the count     
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    return max_length

print(characterReplacement("AAABABB", 1))

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = []
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        [1,2,3]
        self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
    
