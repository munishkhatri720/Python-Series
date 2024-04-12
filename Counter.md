# Counter 

* The Counter clas sis used to count the occureneces of elements in an iterable.

* It returns a dictionary-like object with elements as keys and their count as values.

```py
# Counter

from collections import Counter
array = [1 , 2, 1, 4, 6, 3  , 1, 3, 2]

dictionary = Counter(array)

for k , v in dictionary.items():
    print({f'{k}':f'{v}'})
print(dictionary)

'''
output
{'1': '3'}
{'2': '2'}
{'4': '1'}
{'6': '1'}
{'3': '2'}
'''
```