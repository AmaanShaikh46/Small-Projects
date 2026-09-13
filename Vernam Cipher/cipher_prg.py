plaintext = "Hello"
key = "world"
plaintxt_ascii = []
key_ascii = []
cipher_temp = 0
cipher_ascii = []
cipher_txt = ""



for i in plaintext:
    plaintxt_ascii_val = bin(ord(i))
    plaintxt_ascii.append(plaintxt_ascii_val[2:])
# print(plaintxt_ascii)

for i in key:
    key_val = bin(ord(i))
    key_ascii.append(key_val[2:])
# print(key_ascii)

# print(plaintxt_ascii[0])
# print(key_ascii[0])

print("Plaintext: ", plaintxt_ascii)
print("      Key: ", key_ascii)
for i in range (len(plaintxt_ascii)):
    plntxt_it_1 = plaintxt_ascii[i]
    print("\niteration: ", i)

    for j in range (len(plntxt_it_1)):
        plntxt_xor = plntxt_it_1
        break

    for k in range (len(key_ascii)):
        key_it_1 = key_ascii[i]
        break
    for m in range (len(key_it_1)):
        key_xor = key_it_1
        break
    plntxt_xor = int(plntxt_xor, 2)
    key_xor = int(key_xor, 2)
    print("Plaintext xor: ", plntxt_xor)
    print("key xor      : ", key_xor)
    cipher_temp = plntxt_xor ^ key_xor
    print(cipher_temp)

    cipher_ascii.append(format(cipher_temp, "08b"))




print("Cipher Text: ", cipher_ascii)
for i in range (len(cipher_ascii)):
    cipher_txt += chr(int(cipher_ascii[i], 2))
print("Cipher text string:", cipher_txt)




# print(bin(ord("H"))[2:])
# print(bin(ord("e"))[2:])
# print(bin(ord("l"))[2:])
# print(bin(ord("l"))[2:])
# print(bin(ord("o"))[2:])

# print(final_ascii)
