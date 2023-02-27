nums = [2, 7, 11, 15]
target = 9

nums = [3, 2, 4]
target = 6

nums = [3, 3]
target = 6


nums = [3, 2, 3]
target = 6

def twoSum(nums, target):
    index_result = []
    for element in nums:
        second = target - element
        if second == element:
            nums1 = nums.copy()
            nums1[nums.index(element)] = None
            if second in nums1:
                a = nums.index(element)
                b = nums1.index(second)
                index_result.append(a)
                index_result.append(b)
                break
        else:
            if second in nums:
                i1 = nums.index(element)
                i2 = nums.index(second)
                index_result.append(i1)
                index_result.append(i2)
                break
    return index_result

print(twoSum(nums, target))