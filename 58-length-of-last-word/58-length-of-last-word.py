class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
            s = s.strip()
            return len(s.split()[-1]) if s else 0

            
        
    