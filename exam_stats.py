grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades):
    for grade in grades:
        print (grade)        #print all grade in grades list


def grades_sum(grades):
    total = 0
    for grade in grades:
        total  += grade            #total all grade of grades list
    return total             #return total of grades


def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))    #average of all grades
    return average                              #return the average of all grade score


def grades_variance(scores):                    #to find variance
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) **2

    return variance / float (len(scores))           #return the variance of grade score

variance = grades_variance(grades)

def grades_std_deviation(variance):
    return variance ** 0.5

print (grades_variance(grades))
print (grades_std_deviation(variance))
