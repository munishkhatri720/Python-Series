from collections import deque



my_deque = deque(maxlen=4)




my_deque.append(1)


my_deque.appendleft(2)


my_deque.extend([1 , 2, 4, 5 , 6, 2, 2, 4])


print(my_deque)