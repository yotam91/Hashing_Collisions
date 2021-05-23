return (nonce)

target_string = int(target_string)

for i in range(100):
    xInt = random.randint(1, 100)
    x = xInt.to_bytes(2, 'big')
    xHash256 = hashlib.sha256(x)
    xHash256 = xHash256.hexdigest()
    xBits = ''.join(format(ord(i), '08b') for i in xHash256)

    if countTrailingZero(xInt) == countTrailingZero(target_string):
        result = xInt

if result != 0:
    return (result)
else:
    return ('not found')

# Here the '10010' is the users input

print(hash_preimage('10010'))

# Use the following lines if you want to get input from the users on the command line

# x = input('Enter a binary value ')
# print(hash_preimage(str(x)))





