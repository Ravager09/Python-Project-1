#function_to_check primes
def is_prime(n):
    for i in range(2, n-1):
        if n%i == 0:
            return False
    return True




a=[i for i  in range(2,101,1) if is_prime(i)]
print(a)
print(len(a))


list_of_lists=[[1,2,3],[4,5,6],[7,8,9]]
print(list_of_lists[1][1])
print(len(list_of_lists[0]))


date_of_birth={3}
date_of_birth = {'Adarsh':'9th june', 'Anish':'19th july'}

print(date_of_birth['Adarsh'])


# A dictionary is a collection of key-value pairs.
student = {
    "name": "Rahul",
    "age": 25,
    "courses": ["Math", "Computer Science"],
    "graduated": True
}

print(f"student = {student}")

#print the differnt parts of the dictionary

print(f"student = {student['name']}")
print(f"age of student = {student['age']}")
print(f"what courses did the student have = {student['courses']}")
print(f"did student graduate = {student['graduated']}")

#add GPA
student['gpa'] = 9.1
print(f"student = {student}")

print("method 1")
for key in student:
    print(f"key = {key},value = {student[key]}")

print("-"*100)
# looping over dictionaries : Method 2
print("method 2")
for key in student.keys():
    print(f"key = {key},value = {student[key]}")

print("-"*100)
print("method 3")
for key,value in student.items():
    print(f"key = {key}, value= {value}")

# Nested Dictionaries
# Dictionaries can contain other dictionaries, allowing for complex data structures.
students_dictionary = {
    "student1": {"name": "Rahul", "age": 25, "GPA": 8},
    "student2": {"name": "Atheendra", "age": 24, "GPA": 9},
}
print("-"*100)
print("student 1 details:")
print(f"name = {students_dictionary['student1']['name']}")
print(f"name = {students_dictionary['student1']['age']}")
print(f"name = {students_dictionary['student1']['GPA']}")

print("student 2 details:")
print(f"name = {students_dictionary['student2']['name']}")
print(f"age = {students_dictionary['student2']['age']}")
print(f"gpa = {students_dictionary['student2']['GPA']}")

print("-"*100)
print("method 2")
for student in students_dictionary:
    print(f"name = {students_dictionary[student]['name']}")
    print(f"age = {students_dictionary[student]['age']}")
    print(f"gpa = {students_dictionary[student]['GPA']}")

# Earlier we looped over dictionary of dictionaries
# loop over list of dictionaries


# List of Dictionaries
students_list = [
{"name": "Rahul", "age": 25, "GPA": 8},
{"name": "Atheendra", "age": 24, "GPA": 9}
]
print("-"*100)
print("method 1")
print("-"*100)
for student in students_list:
    print(f"student name = {student['name']}")
    print(f"student age = {student['age']}")
    print(f"student GPA = {student['GPA']}")

print("-" * 100)
print("method 2")
print("-" * 100)
for i in range(len(students_list)):
    print(f"student name = {students_list[i]['name']}")
    print(f"student age = {students_list[i]['age']}")
    print(f"student GPA = {students_list[i]['GPA']}")

print("-" * 100)
print("method 3")
print("-" * 100)
for index, student in enumerate(students_list):
    print(f"name of student number {index + 1} = {students_list[index]['name']}")
    print(f"age of student number {index + 1} = {students_list[index]['age']}")
    print(f"gpa of student number {index + 1} = {students_list[index]['GPA']}")

print("-"*100)
print("method 2")
for student in students_list:
    print(f"name = {student['name']}")
    print(f"age = {student['age']}")
    print(f"gpa = {student['GPA']}")


