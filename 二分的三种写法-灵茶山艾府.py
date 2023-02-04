# 在单调不降序列中查找第一个>=target的下标 不存在则返回数组长度
def lower_bound(nums: List[int],target: int) ->int:
    left = 0
    right = len(nums) - 1  #闭区间 [left,right]
    while left <= right:  #区间不为空
        mid = (left + right) // 2  #mid=left+(right-left)//2
        if nums[mid] < target:
            left = mid + 1  #[mid+1,right]
        else:
            right = mid - 1  #[left,mid-1]
    return left

def lower_bound2(nums: List[int],target: int) ->int:
    left = 0
    right = len(nums)  #左闭右开区间 [left,right)
    while left < right:  #区间不为空
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  #[mid+1,right)
        else:
            right = mid  #[left,mid)
    return left  #right
def lower_bound3(nums: List[int],target: int) ->int:
    left = -1
    right = len(nums) #开区间 (left,right)
    while left + 1 < right:
        mid = (left+right)//2
        if nums[mid] < target:
            left = mid  #(mid,right)
        else:
            right = mid  #(left,right)
    return right
