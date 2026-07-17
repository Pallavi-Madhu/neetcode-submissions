class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left<right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left+1,right+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        #hash_map = {}
        #l = []
        #for index,num in enumerate(numbers):
            #req = target - num
            #if req not in hash_map:
                #hash_map[num] = index
            #else:
                #l.append(index)
                #l.append(hash_map[req])
                #return l
