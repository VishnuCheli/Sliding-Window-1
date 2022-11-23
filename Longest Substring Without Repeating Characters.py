#Sliding Window Technique
#Time Complexity:: O(n) - traversing all elements in the list twice(two times with start and end)
#Space Complexity:: O(n) - creating a hashset to track the used characters
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashset = set() # create a hashset to store the characters that have been already used
        start = 0 #start pointer is initialized
        maximum = 0 #maximum counter is created
        
        for end in range(len(s)): #for loop which initializes the end pointer in every iteration(sliding window)
            if s[end] not in hashset: #if the end index character not in the hashset
                hashset.add(s[end]) #add the end index character to the hashset
                maximum = max(maximum,end-start+1) #maximum length of the currect subtring is updated 

            else: # if the end character is in the hashset
                while s[start]!=s[end]: #till there is no repeated characters
                    hashset.remove(s[start]) #remove the elements in the hashset start index
                    start+=1 #move the start index
                start+=1 #shift the start index for the next for loop iteration to validate a new subtring

        return maximum #return the maximum count 