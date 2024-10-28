def is_palindrome(s):
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]
print(is_palindrome("Hello, world!"))
