s = "a"
s=s.lower()
def checkPalin(st:str)->bool:
    for i in range(int(len(st)/2)):
        if(st[i]!=st[len(st)-i-1]):
            return False    
    return True
s1=''
for i in range(len(s)):
    if(s[i].isalpha()):
        s1=s1+s[i]
        
print(checkPalin(s1))