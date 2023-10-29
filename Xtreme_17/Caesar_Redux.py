def shift_lowercase(text, shift, decrypt=False):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            char_position = ord(char) - ord('a')
            shifted_position = (char_position - shift)% 26 if decrypt else (char_position + shift) % 26
            shifted_char = chr(ord('a') + shifted_position)
            result += shifted_char
        else:
            result += char
    return result

def is_plaintext(message):
    return " the " in message



n = int(input())
shift = []
message = []

for i in range(n):
    shift.append(int(input()))
    message.append(input())
    
    
for i in range(n):    
   
    if is_plaintext(message[i]):
       result = shift_lowercase(message[i], shift[i], decrypt=True)
    else:
        # Encrypt plaintext
       result = shift_lowercase(message[i], shift[i])
       
    print(result)
    