#creating an empty list
my_list = []
#appending elements to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#inserting to position 2
my_list.insert(1,15)
print(my_list)
#extending the list
another_list = [50,60,70]
my_list.extend(another_list)
print(my_list)
#removing the last item on the list
my_list.remove(my_list[-1])
print(my_list)
#sort in ascending order
my_list.sort()
print(my_list)
#index of 30 on list
index = my_list.index(30)
print("Index of 30: ",index)