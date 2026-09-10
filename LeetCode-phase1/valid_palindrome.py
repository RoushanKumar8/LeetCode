class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return True if it is a palindrome, or False otherwise.
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
        and removing all non-alphanumeric characters, it reads the same forward and backward.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("a.", True),
        ("ab_a", True)
    ]
    
    for i, (test_input, expected) in enumerate(test_cases):
        result = solution.isPalindrome(test_input)
        assert result == expected, f"Test case {i+1} failed: Input: '{test_input}', Expected: {expected}, Got: {result}"
        print(f"Test case {i+1} passed!")
    
    print("All test cases passed successfully!")
