# three defined sets
# then following results: i,j; a,b,c; ijnop; d; klmnop

blue=set('abcdijklm')
red=set('efghdijnop')
green=set('qrstklmijnop')

print(blue.intersection(red).intersection(green))
print(blue.difference(red).difference(green))
print(red.intersection(green))
print(blue.intersection(red).difference(green))
# print(green.intersection(red).difference(blue))
print(green.symmetric_difference(red))