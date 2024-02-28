my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert(1, "15")
print(my_list)

my_list = (10, 15, 20, 30, 40)
new_list = (50, 60, 70)
combined_list = my_list + new_list
print (combined_list)

my_list = [10, 15, 20, 30, 40, 50, 60, 70]
my_list = my_list[:7] + my_list[8:]
print(my_list)

my_list = [60, 10, 50, 40, 20, 15, 30]
my_list.sort()
print('List in Ascending Order: ', my_list)

my_list = [10, 15, 20, 30, 40, 50, 60]
element = 30
index = my_list.index(element)
print("index of", element, "is", index)