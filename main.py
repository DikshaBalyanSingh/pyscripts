import os
print ("Enter 1. For Student_To_Teacher")
print ("Enter 2. For Battleship")
print ("Enter 3. For Exam Statistics")
user_input = int(input("Enter the file you want to run"))
if user_input == 1:
    os.system('python student_to_teacher.py')
elif user_input == 2:
    os.system('python battleship.py')
elif user_input == 3:
    os.system('python exam_stats.py')
else:
    print ("Please enter valid input")