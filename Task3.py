'''
3 Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
*Пример*

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
'''

lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9] 
lst1 = []
for i in range(len(lst)):
   flag = 1
   for j in range(len(lst)):
      if lst[i] == lst[j] and i != j:
         flag = 0
         break
   if flag:
       lst1.append(lst[i])
print(f"{lst} -> {lst1}")
