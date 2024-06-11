"""
Given Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
 Output: [2,2,2,1,4,3,3,9,6,7,19]
""" 
from collections import Counter
class Madan:
    # Today is 11/06/2024
    def relativeSortedArray(self,arr1,arr2):
        dictCounter = Counter(arr1)
        numbers = dictCounter.keys()
        temp= []
        for key,value in dictCounter.items():
            if key not in arr2:
                for i in range(value):
                    temp.append(key)
        else:
            temp.sort()
        ans=[]
        for i in arr2:
            while dictCounter[i]:
                ans.append(i)
                dictCounter[i]-=1
        finalAns=ans + temp
        return finalAns
    
        


A, B = [28,6,22,8,44,17],[22,28,8,6]

t1=Madan()
print(t1.relativeSortedArray(A,B))

