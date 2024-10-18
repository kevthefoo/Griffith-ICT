# Problem 1

# while True:
#     content = input("Enter the content: ").lower()
#     if content == "":
#         break
#     content = content.split(" ")
#     content.sort()
    
#     new_content = ''
#     for word in reversed(content):
#         new_content += word + " "
#     new_content.strip()
#     print(new_content)

# Problem 2
# first_list = input("Enter the first list: ").split(" ")
# second_list = input("Enter the second list: ").split(" ")

# if len(first_list) == 1:
#     sum_of_first = float(first_list[0])
# else:
#     sum_of_first = float(first_list[0])+float(first_list[-1])

# if len(second_list) == 1:
#     sum_of_second = float(second_list[0])
# else:
#     sum_of_second = float(second_list[0])+float(second_list[-1])


# if sum_of_first > sum_of_second:
#     print(sum_of_first)
# elif sum_of_first < sum_of_second:
#     print(sum_of_second)
# else:
#     print("Same")


# Problem 3
# gstring = input("Enter the string: ")

# def check_happy_g(s):
#     if 'gg' not in s:
#         return (False, s)
#     else:
#         new_s = s.replace("gg", "")
#         if 'g' not in new_s:
#             return (True, s)
#         else:
#             return (False, s)

# ishappy, ori_input = check_happy_g(gstring)
# if ishappy:
#     print(f"HAPPY {ori_input}")
# else:
#     print(f"Lonely {ori_input}")

# Problem 4
# def ctoF(c):
#     f = round(c*9/5+32, 2)
#     print(f"{c} C is {f} F" )
#     return (c, f)

# def ftoC(f):
#     c = round((f-32)*5/9, 2)
#     print(f"{f} F is {c} C" )
#     return (f, c)

# user_input = input("Enter the degrees and the unit (C/F): ").lower()
# degree = ''
# for _ in user_input:
#     if _.isdigit() or _ == '.':
#         degree += _
# degree = round(float(degree), 2)


# if 'c' in user_input:
#     user_unit = 'c'
#     ctoF(degree)
# elif 'f' in user_input:
#     user_unit = 'f'
#     ftoC(degree)
# else:
#     print("Please enter the correct unit")

# Problem 5
