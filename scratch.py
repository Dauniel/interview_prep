def has_Duplicate(nums: list[int]) -> bool:
    check = set()
    for num in nums:
        if num in check:
            return True
        check.add(num)
    return False

print(has_Duplicate([1,2,3,4,5,6,7,7]))



