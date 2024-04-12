# Counter

from collections import Counter



array = [1 , 2, 1, 4, 6, 3  , 1, 3, 2]

dictionary = Counter(array)

for k , v in dictionary.items():
    print({f'{k}':f'{v}'})
print(dictionary)



