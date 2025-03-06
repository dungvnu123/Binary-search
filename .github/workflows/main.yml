def bilary_search(nums, target ):
    n = len(nums)
    left = 0
    right = n -1
    if left > right:
        return
    while left <= right:
        mid = (left +right)//2
        if nums[mid] == target:
            return True
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -=1
            continue
        #kiem tra tai cac vi tri khong trung lap:
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                left = mid + 1
            else:
                right = mid -1
        else:
            if nums[mid] <= target < nums[right]:
                right = mid - 1
            else:
                left = mid + 1 
    return False                    
nums = list(map(int, input("Nhap vao mang so nguyen cho truoc:").split()))
target = int(input("Nhap vao so mong muon tim kiem trong mang:"))
index = bilary_search(nums, target)
print(index)
