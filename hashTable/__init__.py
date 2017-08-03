from hashClass import HashTable

a = HashTable(11)
input_value = list((54,26,93,17,77,31,44,55,20))

map(lambda x: a.put(x,x),input_value)
print(a.data)