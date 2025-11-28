def is_palindrome(text):
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    
    # Check if cleaned text is the same forwards and backwards
    return cleaned == cleaned[::-1]
print(is_palindrome("Race car"))
print(is_palindrome("Hello"))
