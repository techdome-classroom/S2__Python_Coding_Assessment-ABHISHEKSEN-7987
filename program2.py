class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse the Roman numeral string in reverse order
        for char in reversed(s):
            current_value = roman_map[char]
            
            # If current value is less than the previous value, subtract it (subtractive case)
            if current_value < prev_value:
                total -= current_value
            else:
                # Otherwise, add the value to the total
                total += current_value
            
            # Update the previous value
            prev_value = current_value
        
        return total

# Test cases
solution = Solution()

# Provided test cases
print(solution.romanToInt("III"))      # Output: 3
print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994

# Additional test cases
print(solution.romanToInt("IV"))       # Output: 4
print(solution.romanToInt("XL"))       # Output: 40
print(solution.romanToInt("CD"))       # Output: 400
print(solution.romanToInt("MMXXIII"))  # Output: 2023
