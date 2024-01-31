class Solution:
	def longestPalindrome(self, s: str) -> str:
		self.maxLen = 0
		self.startIdx = -1

		for i in range(len(s)):
			self.expandFromCenter(s,i,i)
			if i+1<len(s) and s[i]==s[i+1]:
				self.expandFromCenter(s,i,i+1)

		if self.startIdx > -1:
			return s[self.startIdx:self.startIdx+self.maxLen]
		return -1


	def expandFromCenter(self,s,l,r):
		while(l>0 and r<len(s)-1 and s[l-1] == s[r+1]):
			l-=1
			r+=1
		if r-l+1 > self.maxLen:
			self.maxLen = r-l+1
			self.startIdx = l