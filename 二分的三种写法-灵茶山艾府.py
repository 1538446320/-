# 在区间中查找第一个>=target的下标
def lower_bound(nums: List[int],target: int) ->int:
    l=0
    r=len(nums)-1 #闭区间 [left,right]
    while l<r:
        mid=(l+r)//2
        if nums[mid]<target:
            l=mid+1
        else:
            r=mid
    return l

def lower_bound2(nums: List[int],target: int) ->int:
    l=0
    r=len(nums)-#左闭右开区间 [left,right)
    while l<r:
        mid=(l+r+1)//2
        if nums[mid]>target:
            r=mid-1
        else:
            l=mid
    return l
def lower_bound3(nums: List[int],target: int) ->int:
    left=-1
    r=len(nums) #开区间 (left,right)
    while left+1 < right:
        mid=(l+r)//2
        if nums[mid]<target:
            left=mid
        else:
            right=mid
    return left
