
# #method 1

# num1 = int(input("Enter integer to be divided: "))
# num2 = int(input("Enter integer to divide by: "))

# x=0

# while num1 >= num2:
#     num1 -= num2
#     x+=1

# print(x)


# #method 2

# def division(numerator, denominator):
#     counter = 0
    
#     while numerator >= denominator:
#         numerator -= denominator
#         counter += 1

#     return counter

# print(division(64, 8))

      

#files

#   open()
#   with open() - automatically closes file when done

# file = open("/workspaces/Data_3500_notes/Lecture code/test.txt", "w")

# names = ["Jacob\n", "Geoffery\n", "Sarah\n", "Steven\n"]
# file.writelines(names)
# file.close()

# file = open("/workspaces/Data_3500_notes/Lecture code/test.txt", "w")
# ages = [25, 72, 5, 21]

# for age in ages:
#     file.write(str(age)+"\n")
# file.writelines(ages)
# file.close()



#numbers file
#find st dev, mean, write both in a new file

import statistics
# statistics.mean()
# statistics.stdev()

with open("/workspaces/Data_3500_notes/Lecture code/numbers.txt") as numbers_file:
    lines = numbers_file.readlines()

numbers = []
    
for line in lines:
    numbers.append(int(line))

mean = statistics.mean(numbers)
stdev = statistics.stdev(numbers)

print(mean, stdev)

with open("/workspaces/Data_3500_notes/Lecture code/statistics.txt") as file:
    file.write(str(mean))
    file.wirte(str(stdev))

   


