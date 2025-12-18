student_admission = {}

def student_profile():
    print("Welcome to Glorich School's admission")
    name =input("Enter your name: ")
    age =input("Enter your age: ")
    email =input("Enter your email: ")
    grade =float(input("Enter your grade: "))

    if grade >=20 :
        print(f"Congratulation {name} you have been admitted to our school")

        student_admission['name'] = name
        student_admission["age"] = age
        student_admission['email'] = email
        student_admission['grade'] = grade

        print('This is your student information:',student_admission)
        print('Thank you for applying to our prestigious school')

    else:
        print(f"Sorry {name}, you're not elegible for admission")
          
student_profile()

