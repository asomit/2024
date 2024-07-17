





number_grades = [97, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 57, 53, 50]
letter_grades = ["a+", "a", "a-", "b+", "b", "b-", "c+", "c", "c-", "d+", "d", "d-", "f+", "f", "f-"]


print(
    """Welcome to the final grade calculator!
If you know your current grade and the weight of the final exam,
you can calculate the grade you need on the final exam to reach your target course grade.""")


def letter_to_number_converter(letter):

    
    if letter in letter_grades:
        letter_grade_index = letter_grades.index(letter)

    return number_grades[letter_grade_index]


def calculate(C, w, G):

    F = (G - ((1 - w) * C)) / w

    if F > 100:
        
        G1 = float((1 - w)*(C) + (100 * w))
        G2 = float((1 - w)*(C) + (90 * w))
        
        print("Sorry, you cannot get a " + str(target_grade).capitalize() + " in this course.")
        print("But, you can get a " + str(round(G1,2)) + " if you get 100 on exam. " +
              "Or you could get a " + str(round(G2,2)) + " if you get 90 on the exam.")
    else:

        print("In order to get a " + str(target_grade).capitalize() + " you would need " + 
              "to get a " + str(round(F,2)) + " on the exam. Good luck!")

while True:
    current_grade = input("What is your current grade in the course? ").replace("%", "")
    try:
        current_grade_converted = float(current_grade)

        if current_grade_converted > 100:
            print("You cannot have a higher grade than 100%.")
            continue

        elif current_grade_converted < 0:
            print("You cannot have a negative grade.")
            continue
    
    
    except ValueError:
        print("You must input an integer. With or without a decimal point or a % sign.")
    else:
        break


while True:
    exam_weight = input("What is the final exam weight? ").replace("%", "")
    try:
        exam_weight_converted = float(exam_weight)

        if exam_weight_converted < 1:
            print("You must give it as a percent of your grade. Not in decimal form")
            continue

        
        exam_weight_decimal = exam_weight_converted / 100

        if exam_weight_decimal > 1:
            print("You cannot have an exam weight more than 100% of your grade")
            continue
        else:
            break

    except ValueError:
        print("You must input an integer. With or without a decimal point or the % sign")
    else:
        break


while True:
    target_grade = input("What letter grade do you want in the class? ").lower().replace(" ", "")

    if target_grade in letter_grades:

        number_target_grade = float(letter_to_number_converter(target_grade))
        
        break

    else:
        print("Please input an acutual letter grade. Like A- or B. ")
        continue


        
calculate(current_grade_converted, exam_weight_decimal, number_target_grade)






