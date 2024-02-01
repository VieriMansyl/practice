/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
  let res = 0;
  let dp = new Array(nums.length).fill(1);

  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
    res = Math.max(res, dp[i]);
  }
  return res;
};

const arr1 = [10,9,2,5,3,7,101,18];
const arr2 = [0,1,0,3,2,3];
const arr3 = [7,7,7,7,7,7,7];

console.log(lengthOfLIS(arr1));