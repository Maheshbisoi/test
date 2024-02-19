
#raise program

class CollegeNameException(Exception):
    pass

college_name = input("Enter your college name: ")

if college_name == "GIETU":
    print("Correct")
else:
    raise CollegeNameException("Invalid college name")
