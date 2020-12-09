class solution:
    a=list()
    def convert(self, s:str,numRows:int)-> str:
        if (len(s)<numRows)and(numRows==1):
            return s
        else:
            a=list()
            for i in range(numRows):
                a.append(s[i]) 
            k=0;kz=numRows-2;z=False
            for i in range(numRows,len(s)):
                if z:
                    a[k]+=s[i];k=k+1
                    if k==numRows:
                        z=False;k=0                
                else:
                    a[kz]+=s[i];kz=kz-1  
                    if kz==0:
                        z=True;kz=numRows-2
            final=''
            for i in range(numRows):
                final=final+a[i]
            return final



                
                
                
        print(a)  
if __name__=='__main__':
    s=input('s:')
    numRows=int(input('numRows:')) 
    result=solution()
    print(result.convert(s,numRows))

    print(str(result))

        