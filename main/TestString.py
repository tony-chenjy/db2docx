
byte = b'\x01\x00'

print(byte)
print(byte.decode('ASCII'))
# print(cmp(byte.decode('ASCII'), ' '))
print(type(byte.decode('ASCII')))

a = ' '
b = ' '
print(a == b)
