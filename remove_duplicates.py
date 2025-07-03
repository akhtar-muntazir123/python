def removeDuplicates(nums):
        d=set()
        k=0
        p=0
        for i in range(len(nums)):
            if nums[i] in d:
                continue
            else:
                d.add(nums[i])
                nums[p]=nums[i]
                p+=1
                k+=1
        print(nums)
        return k
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))