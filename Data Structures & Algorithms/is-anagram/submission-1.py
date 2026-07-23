class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1=dict()
        map2=dict()
        for char in s:
        # if the char doesn't exist in the map, add it, otherwise, increment the count
            if char not in map1:
                map1[char]=0
            map1[char]+=1
        for char in t:
            if char not in map2:
                map2[char]=0
            map2[char]+=1
        return map1==map2