
#Section 1:

import random
from datetime import datetime
while True:
    count = 0
    all_credits = 0
    all_courses = 0
    grade_cumilative = 0
    avarage_grade = 0

    
    print("You may select one of the following:")
    print("                1) Add student")
    print("                2) Search student")
    print("                3) Search course")
    print("                4) Add course completion")
    print("                5) Show student's record")
    print("                0) Exit")
    selection = input("What is your selection?\n")

    if selection == "1" :

        while count <1 :
            print("Name should contain only letters and start with capital letters.")
            first_name = input("Enter the first name of the student:\n")
                
            if first_name[0].isupper() and first_name.isalpha() :
                last_name = input("Enter the last name of the student:\n")
                if last_name[0].isupper() and last_name.isalpha() :
                        
                        print("Select student's major:")
                        print("                CE: Computational Engineering")
                        print("                EE: Electrical Engineering")
                        print("                ET: Energy Technology")
                        print("                ME: Mechanical Engineering")
                        print("                SE: Software Engineering")
                        while count <1 :
                            
                            major = input("What is your selection?\n")
                            if major in ("CE", "SE", "EE", "ET", "ME", "ce", "se", "ee", "et", "me") :
                                print("Student added successfully!\n\n")

                                student_email = (first_name + "." + last_name +"@lut.fi")
                                year = datetime.now().year
                                data = str(student_email) + str(year)
                                file = open("students.txt", "r")
                                for line in file:
                                    student_numbers = line[0:5]
                                file.close() 

                                while True:
                                    new_number = str(random.randint(10000,99999))
                                    if new_number not in student_numbers:
                                        new_student_number = new_number
                                        break
                                    
                                data = (str(new_student_number) + "," + str(first_name) + "," + str(last_name) + "," + str(year) + "," + str(major) + "," + str(student_email))
                                file = open("students.txt", "a")
                                file.write(data + "\n")
                                file.close()
                                
                                count = 1
                            
                            else:
                                print("Please enter a valid major.")
                                continue  
                else:
                    continue

            else:
                print("Please enter valid first and last names.")

#Section 2:
                
    elif selection == "2":
        while count < 1:
            search_student = input("Give at least 3 characters of the students first or last name:\n")
            if len(search_student) == 3:
                match_student = []
                file = open("students.txt", "r")
                for line in file:
                    if search_student in line:
                        student_info = line.strip().split(",")
                        student_id = student_info[0]
                        first_name_2 = student_info[1]
                        last_name_2 = student_info[2]
                        match_student.append("ID:" + student_id + "," + " First name: " + first_name_2 + "," + " Last name: " + last_name_2)
                file.close()

                if match_student:
                    print("Matching students:\n")
                    for line in match_student:
                        print(line)
                        count = 1

                else:
                    print("No students found.\n")
                    continue
            else:
                continue

#Section 3:
                        
    elif selection == "3":
        while count < 1:
            search_course = input("Give at least 3 characters of the name of the course or the teacher:\n")
            if len (search_course) == 3:
                found_course = []
                file= open("courses.txt", "r") 
                for line in file:
                    if search_course in line:
                        course_info = line.strip().split(",")
                        course_id = course_info[0]
                        course_name = course_info[1]
                        teacher_name = course_info[3:]
                        found_course.append("ID: " + course_id + "," + " Name: " + course_name + "," + " Teacher(s): " + str(teacher_name))
                file.close()
                if found_course:
                    for line in found_course:
                        print(line)
                        count = 1
                else:
                    print("No course found.")
                    continue
            else:
                continue

#Section 4:

    elif selection == "4":
        while count < 1:
            course_id = input("Give the course ID:\n")
            file=open("passed.txt", "r")
            for line in file:
                if course_id in line:
                    grade_info = line.strip().split(",")
                    course_idx = grade_info[0]
                    student_idx = grade_info[1]
                    course_datex = grade_info[2]
                    course_gradex = grade_info[3]
                    while count< 1:
                        if course_id == course_idx:
                            student_idxx = input("Give the student ID:\n")
                            if student_idxx == student_idx:
                                while count < 1:
                                    course_grade = input("Give the grade:\n")
                                    if course_grade < course_gradex:
                                        print("Student has passed this course earlier with grade:" + str(course_gradex))

                                    elif int(course_grade) > 5:
                                        print("Grade is not a correct grade.")
                                    else:
                                        while count < 1:
                                            course_date = input("Enter a date (DD/MM/YYYY): \n")
                                            try:
                                                input_date = datetime.strptime(course_date, "%d/%m/%Y")
                                            except ValueError:
                                                print("Invalid date format. Use DD/MM/YYYY. Try again!\n")
                                                continue
                                            if input_date > datetime.now():
                                                print("Input date is later than today. Try again!\n")
                                                continue
                                                
                                            elif(datetime.now() - input_date).days > 30:
                                                print("Input date is older than 30 days. Contact ""opinto"".\n")
                                                continue
                                            else:
                                                file = open("passed.txt", "a")
                                                file.write(course_id + "," + student_idxx + "," + course_date + "," + course_grade + "\n")
                                                file.close()
                                                print("Input date is valid.\nRecord added!\n")
                                                count = 1
                            else:
                                print("Invalid student ID")
                                continue
                        else:
                            break
            file.close()

#Section 5:

    elif selection == "5":
        while count < 1:
            student_document = input("Enter student ID:\n")
            file1 = open("students.txt", "r")
            for rule in file1:
                if student_document in rule:
                    further_information = rule.strip().split(",")
                    number = further_information[0]
                    first_namex = further_information[1]
                    last_namex = further_information[2]
                    the_year = further_information[3]
                    majorx = further_information[4]
                    email_addressx = further_information[5]
                    print("Student ID: " + number)
                    print("Student Name: " + last_namex + ", " + first_namex)
                    print("Starting Year: " + the_year)
                    print("Major: " + majorx)
                    print("Email address: " + email_addressx + "\n")
                    print("Passed courses:\n")
                    file2 = open("passed.txt", "r")
                    file3 = open ("courses.txt", "r")
                    for rule in file2:
                        if student_document in rule:
                            further_informationx = rule.strip().split(",")
                            number_passed = further_informationx[0]
                            x_passed = further_informationx[1]
                            date_passed = further_informationx[2]
                            grade_passed = further_informationx[3]
                            file3.seek(0)
                            for rule in file3:
                                xfurther_informationx = rule.strip().split(",")
                                courses_identity = xfurther_informationx[0]
                                name_of_courses = xfurther_informationx[1]
                                grades_of_courses = xfurther_informationx[2]
                                names_of_teachers = ", ".join(xfurther_informationx[3:])
                                if number_passed == courses_identity:
                                    print("Course ID: " + number_passed + "," + " Name: " + name_of_courses + "," + " Credits: " + grades_of_courses)
                                    print("Date: "+ date_passed + ", " + names_of_teachers + ", " + "Grade: " + grade_passed + "\n")
                                    all_credits += int(grades_of_courses)
                                    all_courses += 1
                                    grade_cumilative += int(grade_passed)
                                    avarage_grade = grade_cumilative / all_courses
                                    break
                    print("Total credits: " + str(all_credits) + "," + " avarage grade: " + str(avarage_grade) + "\n")
                    count = 1
        file1.close()
        file2.close()
        file3.close()

#Section 0:

    elif selection == '0':
            print("Goodbye! :)")
            break
    