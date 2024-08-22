def substring(string,str):
        k=0
        i=0
        n=len(str)
        while(k!=(len(string)-n)+1):
            n_str=string[k:n+k]
            if n_str==str:
                  i=i+1
            k=k+1
        print(i)
string="ABCDCDC"
str="CDC"
substring(string,str)