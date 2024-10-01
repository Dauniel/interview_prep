class Solution:
	def hasDuplicate(self, nums: list[int]) -> bool:
		n = set()
		for num in nums:
			if num in n:
				return True
			else:
				n.add(num)
		return False
	
	def validAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		checkS = dict()
		checkT = dict()
		
		for i in range(len(s)):
			checkS[s[i]] = checkS.get(s[i], 0) + 1
			checkT[t[i]] = checkT.get(t[i], 0) + 1

		return checkS == checkT
	
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		check = dict()
		
		for i in range(len(nums)):
			if target - nums[i] in check:
				return [check[target - nums[i]], i]
			else:
				check[nums[i]] = i
	
	def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
		anagrams = dict()
		for s in strs:
			sortedString = "".join(sorted(s))
			if sortedString not in anagrams:
				anagrams[sortedString] = []
				anagrams[sortedString].append(s)
			else:
				anagrams[sortedString].append(s)
		res = []
		for anagram in anagrams:
			res.append(anagrams[anagram])
		
		return res

	def topKFrequent(self, nums: list[int], k: int) -> list[int]:
		count = dict()
		freq = dict()
		for num in nums:
			count[num] = count.get(num, 0) + 1
		for key, value in count.items():
			if value not in freq:
				freq[value] = []
				freq[value].append(key)
			else:
				freq[value].append(key)
		res = []
		for key in reversed(sorted(freq.keys()):
			for num in freq[key[:
				res.append(num)
				if len(res) == k:
					return res


solution = Solution()

# For hasDuplicate
print("Has Duplicate for [1,2,3,4,5]:", solution.hasDuplicate([1,2,3,4,5]))
print("Has Duplicate for [1,2,3,4,5,6,7,1]:", solution.hasDuplicate([1,2,3,4,5,6,7,1]))

# For validAnagram
print("Valid Anagram for 'anagram' and 'nagaram':", solution.validAnagram("anagram", "nagaram"))
print("Valid Anagram for 'rat' and 'car':", solution.validAnagram("rat", "car"))

# For twoSum
print("Two Sum for [2, 7, 11, 15] with target 9:", solution.twoSum([2, 7, 11, 15], 9))
print("Two Sum for [3, 2, 4] with target 6:", solution.twoSum([3, 2, 4], 6))

# For groupAnagrams
print("Group Anagrams for ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']:", solution.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
print("Group Anagrams for ['']:", solution.groupAnagrams(['']))
print("Group Anagrams for ['a']:", solution.groupAnagrams(['a']))
