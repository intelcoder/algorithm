
def flip(s):
    length = len(s)
    stack = []
    for i in range(length-1):
        if s[i] == '+' and s[i+1] == '+':
            replaced = s[0:i] + '--'
            if i+2 < length:
                replaced += s[i+2:]
            stack.append(replaced)
    return stack


print(flip('++-++'))
print(flip('+-++'))
print(flip('+-+++'))
print(flip('+-+-+--'))