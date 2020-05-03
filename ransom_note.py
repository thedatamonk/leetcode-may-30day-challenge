class Solution:
    # O(N + M) space complexity where N and M are the number of distinct characters in ransom_note and magazine string
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_freq = dict(Counter(ransomNote))
        mag_freq = dict(Counter(magazine))
        
        for key, value in note_freq.items():
            if key not in mag_freq:
                return False
            if value > mag_freq[key]:
                return False
        
        return True

    """Optimized version"""
   	# O(1) space complexity
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
        	if char not in magazine:
        		return False
        	# decrease the count of this character by 1
        	magazine.replace(char, "", 1)

    	return True
