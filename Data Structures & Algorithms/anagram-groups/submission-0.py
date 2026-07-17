class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #WORKFLOW
        # --> first create array with 26 size as 0's as input.
        # --> now for each char in the word,calculate the ord and store it
        # --> now we make that the key of our duict,but since a list cant be the key,we change it to tuple
        #--> we also append the word
        #--> last we return the values
        groups = {}
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')]  += 1
            tup = tuple(count)
            if tup not in groups:
                groups[tup] = []
            groups[tup].append(word)
        return list(groups.values())

        

