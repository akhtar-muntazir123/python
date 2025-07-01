h=[1,8,6,2,5,4,8,3,7]
lp=0
rp=len(h)-1
maxArea=0
print(type(h))
while(lp<rp):
    height=min(h[lp],h[rp])#height
    w=rp-lp#width
    area=height*w
    if(area>maxArea):
        maxArea=area
    if(h[lp]<h[rp]):
        lp=lp+1
    else:
        rp=rp-1
print(maxArea)
    
    
    
# print(min(2,3))