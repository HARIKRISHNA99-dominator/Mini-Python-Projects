c=[]
print("Input Integers")
for i in range(0,20):
    c.append(int(input()))
npos=0
nneg=0
nodd=0
neven=0
nzeros=0
for i in range(0,20):
    if c[i]>0:
        npos=npos+1
    elif c[i]<0:
        nneg=nneg+1
    else:
        nzeros=nzeros+1
    if c[i]%2==0:
        neven=neven+1
    else:
        nodd=nodd+1
print("Number Of Positive Numbers : ",npos)
print("Number Of Negative Numbers : ",nneg)
print("Number Of Odd Numbers : ",nodd)
print("Number Of Even Numbers : ",neven)
print("Number Of Zeros Numbers : ",nzeros)