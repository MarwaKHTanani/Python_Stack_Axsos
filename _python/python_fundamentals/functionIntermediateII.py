# update value in dictionaries and list
# 1
x = [[5, 2, 3], [10, 8, 9]]
# x[1][0]=15
for i in range(len(x)):
    for j in range(len(x[i])):
        if x[i][j] == 10:
            x[i][j] = 15
print(x)

# 2
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]

# for i in range(len(students)):
#     if students[i]["last_name"] == "Jordan":
#         students[i]["last_name"] = "Bryant"
for student in students:
    if student["last_name"] == "Jordan":
        student["last_name"] = "Bryant"

print(students)

# 3
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
# sports_directory['soccer'][0]='Andres'
for key, values in sports_directory.items():
    for i in range(len(values)):
        if values[i] == "Messi":
            values[i] = "Andres"
print(sports_directory)

# 4
z = [{"x": 10, "y": 20}]
for index in z:
    index["y"] = 30
print(z)

# Iterate Through a List of Dictionaries
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
for student in students:
    print(f'first_name - {student["first_name"]}, last_name - {student["last_name"]}')


# Get Values From a List of Dictionaries
def iterateDictionary(key_name, some_list):
    for item in some_list:
        print(item[key_name])


iterateDictionary(
    "first_name",
    [
        {"first_name": "Michael", "last_name": "Jordan"},
        {"first_name": "John", "last_name": "Rosales"},
        {"first_name": "Mark", "last_name": "Guillen"},
        {"first_name": "KB", "last_name": "Tonel"},
    ],
)
iterateDictionary(
    "last_name",
    [
        {"first_name": "Michael", "last_name": "Jordan"},
        {"first_name": "John", "last_name": "Rosales"},
        {"first_name": "Mark", "last_name": "Guillen"},
        {"first_name": "KB", "last_name": "Tonel"},
    ],
)

# Iterate Through a Dictionary with List Values
dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}


def printInfo(some_dict):

    for key, values in some_dict.items():
        print(f"{len(values)} {key}")
        for i in range(len(values)):
            print(values[i])


printInfo(dojo)
