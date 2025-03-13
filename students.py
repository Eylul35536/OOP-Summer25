student1 = {
    'first_name': 'Eylul',
    'last_name': 'Kilagoz',
    'index_number': '35536',
    'nationality': 'Turkish',
    'starting_date': '15.01.2024',
    'courses': ['Object-Oriented Programming', 'Mathematics']
}

student2 = { 
    'first_name': 'Emirhan',
    'last_name': 'Turhan',
    'index_number': '220311065',
    'nationality': 'Turkish',
    'starting_date': '12.01.2024',
    'courses': ['Circuit', 'Physics']
}

student3 = {
    'first_name': 'Buse',
    'last_name': 'Acik',
    'index_number': '44344',
    'nationality': 'French',
    'starting_date': '10.01.2024',
    'courses': ['English Studies', 'Literature']
}
students = [student1, student2, student3]

for index, student in enumerate(students):
    print(f"Student {index + 1}: {student['first_name']} {student['last_name']}")
