var plusOne = function(digits) {
  digits[digits.length-1] += 1;

  for (let i = digits.length-1; i >= 0; i--) {
    if (digits[i] === 10) {
      if (i !== 0) {
        digits[i-1] += 1;
        digits[i] = 0;
      } else {
        digits.unshift(1);
        digits[i+1] = 0;
      }
    }
  }
  return digits;
};