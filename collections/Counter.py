# Counter

from collections import Counter



array = [1 , 2, 1, 4, 6, 3  , 1, 3, 2]

dictionary = Counter(array)

for k , v in dictionary.items():
    print({f'{k}':f'{v}'})
print(dictionary)



x = Counter('Manishhhhhh')
print(x.items())

'''
output

dict_items([('M', 1), ('a', 1), ('n', 1), ('i', 1), ('s', 1), ('h', 6)])
'''

