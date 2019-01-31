def unique():
    string=input("enter the string : ")
    s=[]
    for i in string:
        if i not in s:
            s.append(i)
        else:
            print("not unique")
            break
    if(len(s)==len(string)):
        print("unique")
              
