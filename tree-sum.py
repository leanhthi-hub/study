#class Solution:
#   def threeSum(self, nums: List[int]) -> List[List[int]]:
outp=list[int]
sum=int()
def dequy(i:int,j:int,nums: list[int],sum) -> List[int]:
    if i==0:
        outp[0]=nums[0] 
    if i>=2:
        if sum==0:
            [print(outp[k])for k in range 2]
        sum=0
        continue
    j+=1
    sum=sum+nums[j]
    dequy[i+1,j,nums,sum]
    return outp
    
    

        




if __name__ == '__main__':
    inp=input('Enter separated by ,: ')
    nums=inp.split(',')
    
    for i in range(len(nums)):
        nums[i]=int(nums[i]) 
    for j in range(len(nums)):
        sum=nums[j]
        dequy(i,j,nums,sum);print(dequy)
    

    
    
