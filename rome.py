#class Solution:'''self,''''
dataa={'1':'I','4':'IV','5':'V','9':'IX','10':'X','40':'XL','50':'L','90':'XC','100':'C','400':'CD','900':'CM','1000':'M','500':'D'}
def intToRoman(num: int) -> str:
    result=str()
    for i in range(len(str(num))):
        if num//(10**i)>=0:
            doc=num%(10)
            if doc in (2,3):
                countt=doc*(10**i)
                temp=dataa[str(10**i)]*doc
                result=temp+result
                temp=''
            elif doc in(6,7,8):    
                temp=dataa[str(5*(10**i))]
                countt=doc-5
                temp=temp+dataa[str(10**i)]*(countt)
                result=temp+result
                temp=''
            elif doc==0:
                result+=""
            else:
                temp=dataa[str(doc*(10**i))]
                result=temp+result
                temp=''
        num=num//10
    return result
if __name__ == '__main__':
    #kio=Solution()
    inp=int(input())
    print(intToRoman(inp))

        