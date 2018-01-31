
def is_palindrome(s):
    length = len(s)
    for i in range(length):
        for j in range(i, length-1):
            cut = s[i:j+2]
            if cut == cut[::-1]: return True
    return False

print(is_palindrome("code"))
print(is_palindrome("carerac"))