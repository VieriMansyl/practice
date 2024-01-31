/**
 * @param {number} n
 * @return {number}
 */

var climbStairs = function(n) {
  if (n == 1) return n;

  let prev = 1;
  let curr = 2;

  for (let i = 3; i <= n; i++){
    curr = prev + curr;
    prev = curr - prev;
  }

  return curr;
};
