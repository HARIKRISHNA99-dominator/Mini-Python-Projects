a = [1,2,3,3,2,1]
i = 0
mid = (len(a))/2
same = True
while i<mid:
  if a[i] != a[len(a)-i-1]:
    print("no")
    same = False
    break
  i = i+1
if same == True:
    print ("Yes")