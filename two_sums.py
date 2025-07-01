nums = [2,7,11,15]
lookup={}
t=9#target
for i in range (len(nums)):
    rem=t-nums[i]
    if rem in lookup:
        print("pair found at",i,lookup[rem])
    lookup[nums[i]]=i