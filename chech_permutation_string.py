s1=input("enter first string : ")
s2=input("enter second string : ")
s3=list(s1)
s4=list(s2)
s3.sort()
s4.sort()
if(s3==s4):
    print("yes! one is permutation of other")
else:
    print("No ")
