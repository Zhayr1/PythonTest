#- Start with the string "CitricSheep". 
#- Use the ASCII values of each character in the string and generate a list of these values.
#- Multiply each value in the list by the number of characters in the string.
#- Find the sum of all numbers in the resulting list.
#- Use this sum to generate a SHA256 hash.
#- Convert this hash to a hexadecimal string.
from hashlib import sha256

start_string = "CitricSheep"
start_string_len = len(start_string)

ascii_list = list(bytes(start_string, 'ascii'))

multiplied_list = [x * start_string_len for x in ascii_list]

sum_list = sum(multiplied_list)

sha256_hash = sha256(str(sum_list).encode('utf-8'))

hex_string = sha256_hash.hexdigest()

print("Hexadecimal string:",hex_string)