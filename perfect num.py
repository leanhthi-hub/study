class solution:
    a=list()
    def convert(self, s:str,numRows:int)-> str:
        a=list()
        for i in range(numRows):
           a.append(s[i]) 
        k=0;kz=numRows-2;z=False
        for i in range(len(s)):
            if z:
                a[k]+=s[i];k=k+1
                if k==numrows-1:
                    z=False;k=0;break
                
            else:
                a[kz]+=s[i];kz=kz-1  
                if kz==1:
                    z=True;kz=numRows-2;break
                
        print(a)  
if __name__=='__main__':
    s=input('s:')
    numRows=int(input('numRows:')) 
    result=solution()
    print(result.convert(s,numRows))

    print(str(result))

        