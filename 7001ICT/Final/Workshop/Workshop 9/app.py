# Problem 1
# file_name = input("Enter a file name: ")
# file = open('./P1_v1.txt', 'r')
# content = file.read()

# words = content.split()

# unique_words = len(set(words))
# print(unique_words)

# Problem 2
# student_id_list = []
# while True:
#     student_id = input("Enter a student ID: ")
#     try:
#         student_id = int(student_id)
#     except:
#         break


#     if student_id in student_id_list:
#         break
#     elif int(student_id) < 0:
#         break

#     student_id_list.append(student_id)

# student_number = len(student_id_list)
# print(f"{student_number} students enrolled in the course.")

# Problem 3
book = {'a4': 50, 'a5': 50,}
pen = {'black': 80, 'blue':80, 'red': 80}


# def buypen():
#     while True:
#         request_pen_number = int(input("Number of pens requested by customer: "))
#         request_pen_colour = input("Colour of pen requested by customer: ").lower()
#         pen[request_pen_colour] -= request_pen_number
#         pen_inven_count = pen[request_pen_colour]
#         if pen_inven_count <= 5:
#             orderornot = input("There are only 50 pens in stock. Do you want to buy the 50 pens? Y/N: Y").lower()
#             if orderornot == 'y':
#                 pen[request_pen_colour] += 50
#                 print(f"New {request_pen_colour} pens must be ordered.")
        
        
#         more_pne =input("Any other pens: yes/no:").lower()
#         if more_pne == 'no':
#             return

# def buybook():
#     while True:
#         request_book_number = int(input("Number of books requested by customer: "))
#         request_book_size = input("Size of books requested by customer: ").lower()
#         book[request_book_size] -= request_book_number
#         book_inven_count = book[request_book_size]
#         if book_inven_count <= 5:
#             orderornot = input("There are only 5 books in stock. Do you want to buy the 50 pens? Y/N: Y").lower()
#             if orderornot == 'y':
#                 book[request_book_size] += 50
#                 print(f"New {request_book_size} books must be ordered.")
        
        
#         more_pne =input("Any other books: yes/no:").lower()
#         if more_pne == 'no':
#             return

# while True:
#     buypen()
#     buybook()

#     for _ in pen:
#         print(f"Number of {_} pens in stock: {pen[_]}")

#     for _ in book:
#         print(f"Number of {_} books in stock: {book[_]}")


# Problem 4
# scores = []
# for i in range(5):
#     score = input(f"Student {i+1} (courses 1-4): ").split()
#     score_num_list = []
#     for _ in score:
#         score_num = int(_)
#         score_num_list.append(score_num)
    
#     scores.append(score_num_list)



# def highest_average(scores):
#     highest_average_score = 0
    
#     for student in scores:
#         sum = 0
#         for _ in student:
#             sum += _
#         average_score = sum / 4
#         if average_score > highest_average_score:
#             highest_average_score = average_score

#     print(highest_average_score)

# def hightest_course_average(scores):
#     course_score = []
#     highest_course_average = 0
    
#     for _ in range(4):
#         sum = 0
#         for std in scores:
#             sum += std[_]
#         course_average = sum / 5
#         if course_average > highest_course_average:
#             highest_course_average = course_average


#     print(highest_course_average)

# highest_average(scores)
# hightest_course_average(scores)

# Problem 5
