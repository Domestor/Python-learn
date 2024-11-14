class Solution:
    def is_palindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]

sol = Solution()

print(sol.is_palindrome(121))
print(sol.is_palindrome(10))