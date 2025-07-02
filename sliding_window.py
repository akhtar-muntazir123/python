# print the largest subarray whose sum is equal to  k
# sliding window approach can be used if we are using a positive array for solving a -ve array we will use the concept of hashmap
n=[-1,-1,1]
k=9
l=0
t=0#counter to calculate total number of subarrays found 
curr=0
# if len(n)==1:
#     if(n[0]==k):
#         print (1)
for r in range (len(n)): #taking r=0 and traversing through the list
    curr=curr+n[r]#adding element to the cyurrent sum
    print(curr)
    if curr==k:#subarray found
        t=t+1
    elif curr>k:
        while(curr>k):#increasing left pointer until the current sum < k
            if(curr>k):
                curr=curr-n[l]
                l=l+1
        if(curr==k):#subarray found
            t=t+1
            print([l,r])
        
print(t)                
  
#   chatgpt code           
#     l = 0
#     t = 0
#     curr = 0
#     for r in range(len(nums)):
#         curr += nums[r]
#         while curr > k and l <= r:
#             curr -= nums[l]
#             l += 1
#         if curr == k:
#             t += 1
#     return t
        