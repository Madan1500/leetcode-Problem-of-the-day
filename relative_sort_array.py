"""
Given Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
 Output: [2,2,2,1,4,3,3,9,6,7,19]
""" 

from collections import Counter
class Madan:
    # Today is 11/06/2024
    # `This is the first way to solve the problem`
    # TimeComplexity is O(nlogn + m )

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
    


    # This is the second way to solve the problem

    # Time complexity is O(nlogn) and space complexity is O(n)

    def relativeSortArray(self,arr1,arr2):
        hash_map = {}
        for i in range(len(arr2)):
            hash_map[arr2[i]] = i
        for i in range(len(arr1)):
            if arr1[i] not in hash_map:
                hash_map[arr1[i]] = 1000 + arr1[i]
        arr1.sort(key=lambda x: hash_map[x])
        return arr1

        


A, B = [28,6,22,8,44,17],[22,28,8,6]

t1=Madan()
print(t1.relativeSortArray(A,B))

