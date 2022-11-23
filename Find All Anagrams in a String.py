#Sliding Window Technique
#Time Complexity:: O(len(s)*len(p)) - traversing all characters in the strings twice(two times with start and end)
#Space Complexity:: O(len(s)*len(p)) - creating a dictionary to count the number of character occurances
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #edge case if the lenth of string p is greater than s then no anagrams
        if len(p)>len(s):
            return []
        result = [] #a result array to store the anagrams start index
        
        #creating a default dict manually and storing the count of characters
        pcount={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        ssCount={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        for ch in p: #for each character in p add the number of occurances in the pcount array
            if ch in pcount:
                pcount[ch]+=1
            else:
                pcount[ch]=1
    
        start = 0 #initializing start index

        #constructing the sliding window
        for end in range(len(p)): #keep iterating the end index over the length of p
            if s[end] in pcount: #if the s character is in the p 
                ssCount[s[end]]+=1 #add the occurance of the character in the count of matching strings in scount
        if pcount==ssCount: #if both strings have matching characters initially then append the start index to the anagram list
            result.append(start)


        #sliding/moving the window
        for end in range(len(p),len(s)):#slide the window from the first anagram to the end of the larger string s
            #incoming element at end increase the count at ssCount
            if s[end] in pcount:
                ssCount[s[end]]+=1

            #outgoing element at start increase the count at ssCount
            if s[start] in ssCount:
                ssCount[s[start]]-=1
            start+=1 #start index is manually iterated

            if pcount==ssCount: #if pcount is same as ssCount then it's an anagram
                result.append(start) #add anagram start index to result


        return result #returnt the array of anagram starting indexes