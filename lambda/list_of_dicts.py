list_of_dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 28},
    {"name": "David", "age": 22},
    {"name": "Eva", "age": 35}
]

list_of_dicts.sort(reverse=True,key=lambda i: i["age"])
print (list_of_dicts)