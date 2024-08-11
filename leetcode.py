# TWO-SUM

def twoSum(nums: list[int], target: int) -> list[int]:
    check = dict()
    for i in range(len(nums)):
        if target - nums[i] in check:
            return [check[target - nums[i]], i]
        else:
            check[nums[i]] = i

# Test the function with various test cases
print("Testing Two Sum")
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(twoSum([3, 3], 6))          # Output: [0, 1]
print(twoSum([1, 2, 3, 4, 5], 9)) # Output: [3, 4]
print(twoSum([1, 2, 3, 4, 5], 10))# Output: []

# Palindrome for Number

def isPalindromeNumber(x: int) -> bool:
    if x < 0: return False
    reversed_num = 0
    temp = x
    while temp != 0:
        reversed_num = reversed_num * 10 + (temp % 10)
        temp //= 10
    return reversed_num == x

testCases = [-10, 123, 121, 676756767, 1293128937123]
for num in testCases:
    print(isPalindromeNumber(num))

# Palindrome for Alphanumeric Lazy Version

def isPalindromeLazy(s: str) -> bool:
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == str[::-1]

# Palindrome for Alphanumeric Good Version
def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > 1 and not alphaNum(s[r]):
            r -= 1
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True
def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))

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

# Search Insert Position
def searchInsert(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left += 1
        elif nums[mid] > target: 
            right -= 1
        else:
            return mid
    return left

print("Search Insert Testing")
print(searchInsert([1,3,5,6], 5))

# Longest Common Prefix
def longestCommonPrefix(strs: list[str]) -> str:
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    ans = ""
    for i in range(len(min(first, last))):
        if first[i] == last[i]:
            ans += first[i]
        else: 
            return ans
    return ans

print("Longest Common Prefix Testing")
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["racecar","racecar"]))


# Merge Two Lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = node = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next
    node.next = list1 or list2
    return dummy.next

# Duplicate Integer
def hasDuplicate(nums: list[int]) -> bool:
    check = set()
    for num in nums:
        if num in check:
            return True
        else:
            check.add(num)

print("Has Duplicate Testing")
print(hasDuplicate([1,2,3]))
print(hasDuplicate([1,2,2,3]))

# is Anagram
def isAnagram(s: str, t: str) -> bool:
    checkS = dict()
    checkT = dict()
    for c in s:
        if c not in checkS:
            checkS[c] = 1
        else:
            checkS[c] += 1
    for c in t:
        if c not in checkT:
            checkT[c] = 1
        else:
            checkT[c] += 1
    return checkS == checkT
print("Anagram Testing")
print(isAnagram("cat", "tac"))
print(isAnagram("cat", "tac"))

# Roman to Integer
def romanToInt(s: str) -> int:
    m = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i + 1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
    return ans
print("Testing Roman to Int")
print(romanToInt("XXX"))
print(romanToInt("IV"))
print(romanToInt("MX"))

# Group Anagrams 
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = dict()
    for s in strs:
        sortedWord = "".join(sorted(s))
        if sortedWord not in anagrams:
            anagrams[sortedWord] = []
        anagrams[sortedWord].append(s)
    ans = []
    for anagram in anagrams:
        ans.append(anagrams[anagram])
    return ans

# Top K Frequent Elements
print(groupAnagrams(["cat", "tac", "act", "bat", "tab", "zebra", "lion", ""]))

def topKfrequent(nums: list[int], k: int) -> list[int]:
    count = dict()
    freq = []
    for i in range(len(nums) + 1):
        freq[i].append([])
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for value, count in count.items():
        freq[count].append(value)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res

# Length of Longest Substring
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0 
    ans = 0 
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        ans = max(ans, r - l + 1)
    return ans

# Longest Consecutive Sequence
def longestConsecutiveSequence(nums: list[int]) -> int:
    numSet = set(nums)
    ans = 0
    for num in nums:
        if num - 1 not in numSet:
            length = 1
            while num + length in numSet:
                length += 1
            ans = max(ans, length)
    return ans

# Minimum in Rotated Sorted Array
def findMinInRotatedArray(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

