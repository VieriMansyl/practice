class Solution {
  public:
    int lengthOfLongestSubstring(string s) {
      int maxLong = 0 , i = 0 , idx = -1;
      string sub = "";
      while(i < s.length()){
        // find
        for(int j = 0; j < sub.length() ; j++){
          if(sub[j] == s[i]){
            idx = j;
          }
        }
        
        // update
        if(idx != -1){
          sub.erase(0,idx+1);
          idx = -1;
        }
        sub += s[i];
        i++;    
        
        maxLong = maxLong > sub.length() ? maxLong : sub.length();
      }
      return maxLong;
    }
};