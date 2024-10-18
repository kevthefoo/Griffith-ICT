# Problem 1
# source_file_name = input("Enter the source file name: ")
# target_file_name = input("Enter the target file name: ")

# source_file = open(source_file_name, "r")
# content = source_file.readlines()
# count = 0

# new_content = []
# for line in content:
#     if line == "\n":
#         count += 1
#     else:
#         new_content.append(line)

# target_file = open(target_file_name, "w")
# target_file.writelines(new_content)
# print(f"Lines removed: {count}")

# Problem 2

# source_file_name = input("Enter the source file name: ")
# file = open(source_file_name, "r")
# content = file.readlines()
# print(content[0])
# print(content[1])
# print(content[-2])
# print(content[-1])

# Problem 3
# source_file_name = input("Enter the source file name: ")
# file = open(source_file_name, "r")

# content = file.readlines()

# count = 0
# for each_line in content:
#     clearn_line = each_line.replace("\n", "").split(" ")
#     sum = 0
#     for each_number in clearn_line:
#         each_number = int(each_number)
#         sum += each_number
#     average = sum / len(clearn_line)
#     print(f"Average of line {count+1} is {average}")
#     count += 1

# Problem 4
# source_file_name = input("Enter the source file name: ")
# file = open(source_file_name, "r")

# content = file.read()
# content.replace(" ", "")
# char_count = len(content)
# print(f"Caharacters: {char_count}")
# file.close()

# file = open(source_file_name, "r")
# content = file.readlines()

# total_word_count = 0
# for line in content:
    
#     word_count = len(line.strip().replace("\n","").split(" "))
#     total_word_count += word_count

# print(f"Words: {total_word_count}")
# file.close()

# file = open(source_file_name, "r")
# content = file.readlines()
# line_count  = len(content)
# print(f"Lines: {line_count}")
# file.close()