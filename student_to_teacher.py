lloyd = {
    "name":"Lloyd",
    "homework": [90.0,97.0,75.0,92.0],     #array with 4 values
    "quizzes": [88.0,40.0,94.0],           #array with 3 values
    "tests": [75.0,90.0]                   #array with 2 values
}
alice = {
    "name":"Alice",
    "homework": [100.0,92.0,98.0,100.0],                                   #array with 4 values
    "quizzes": [82.0,83.0,91.0],                                           #array with 3 values
    "tests": [89.0,97.0]                                                   #array with 2 values
}
tyler = {
    "name":"Tyler",
    "homework": [0.0,87.0,75.0,22.0],                                      #array with 4 values
    "quizzes": [0.0,75.0,78.0],                                            #array with 3 values
    "tests": [100.0,100.0]                                                 #array with 2 values
}
students=[lloyd,alice,tyler]

#functions are below:-

def average(numbers):                                                      #creating a function average which accept an array parameter with integer elements
    total=sum(numbers)
    total=float(total)
    result=total/len(numbers)
    return result                                                          #return average of the elements

def get_average(student):                                                   #creating a function get_average which accept a single student dictionary
    homework=sum(student["homework"])/len(student["homework"])
    quizzes=sum(student["quizzes"])/len(student["quizzes"])
    tests=sum(student["tests"])/len(student["tests"])
    return .1*homework+.3*quizzes+.6*tests                                 #return weighted average

def get_letter_grade(score):                                               #creating a function get_lettr_grade
        if score>=90:
            return "A"
        elif score>=80:
            return "B"
        elif score>=70:
            return "C"
        elif score>=60:
            return "D"
        else:
            return "F"                                                      #return a value
def class_average(students):                                                #creating a function class_average
    results = []
    for student in students:
        r=get_average(student)
        results.append(r)
    return average(results)                                                 #return the average of score


print (class_average(students)                                              #this script printing the class average of all students and letter grade for the class's average
       ,get_letter_grade(class_average(students)))