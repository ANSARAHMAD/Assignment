# Program 1

# print(4)
# print("Hello Class")  # Output: Hello Class
# a = "Hello Python"
# print(a)  # Output: Hello Python

# message = "I am Studying in Uaf"
# abc = 123
# pi = 3.14

# print(message,abc,pi) # Output: I am studying in Uaf 123 3.14

# print(type(message)) # Output: <class 'int'> 

# Program 2

# print(1 + 2)   # Output: 3
# x = 13
# y = 2
# z = x * 2
# print(z) # Output: 26


# Program 3


# x = 5
# print(x)   # Output: 5
# x = x + 3
# print(x)  # Output: 8


# Program 4


# x = 7//2
# y = 7%2
# print(x,y)   # Output: 3 1

# first = "100"
# second = 3
# print(first*second)   # Output: 100 100 100

# inp = float(input("Enter Something: "))   # Input: 23.2
# ans = inp + 30
# print(ans)    # Output: 53.2


# Program 5 


# inp = int(input("Enter Math Marks: ")) #Input Marks from User
# percentage = (inp/100)*100
# print(percentage)

# inp = int(input("Enter Percentage in Exams: "))

# if inp >= 80:
#     print("A")
# elif inp >=70:
#     print("B")
# elif inp >=60:
#     print("C")
# elif inp < 60:
#     print("D")
# elif inp <40:
#     print("F")

# Program 6


# if inp >= 100:
#     print("Full Marks")
# else:
#     if inp >= 80:
#         print("A")
#     elif inp >=70:
#         print("B")
#     elif inp >=60:
#         print("C")
#     elif inp < 60:
#         print("D")
#     elif inp <40:
#         print("F")


# Program 7

# try:
#     inp_hrs = int(input("Enter Hours Worked: ")) 
#     rate = 10
#     ad_rate = rate * 1.5
#     if inp_hrs > 40:
#         ad_hrs = inp_hrs - 40
#         pay = (ad_hrs*ad_rate)+(40*rate)
#         print(pay)
#     else:
#         pay = inp_hrs * rate
#         print(pay)
# except:
#     print("Input an Integer")


# Program 8

# inp = input('Enter Fahrenheit Temperature:')
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Please enter a number')

# x = 5


# if x <2 :
#     print("Below 2")
# elif x<20 :
#     print("Below 20")
# elif x<10 :
#     print("Below 10")
# else:
#     print("Something Else")

# Functions 

# print(min("Hello World"))

# print(len("Hello world"))

# def lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# def repeat_lyrics():
#     print(lyrics())
#     print(lyrics())

# print(repeat_lyrics())

# def twice(bruce):
#     print(bruce)
#     print(bruce)

# print(twice("Spam " * 4))

# def add(a,b):
#     c = a+b
#     return c

# x = add(4,6)
# print(x)

# inp = float(input("Enter Percentage: "))
# def grades(inp):
#     if inp >= 80:
#         x = "A"
#     elif inp >=70:
#         x= "B"
#     elif inp >=60:
#         x = "C"
#     elif inp < 60:
#         x = "D"
#     elif inp <40:
#         x = "F"
#     return x

# print(grades(inp))


# n = 10
# while True:
#     print(n)
#     n = n-1
# print("Done")

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')


# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')


# friends = ['Joseph', 'Glenn', 'Sally']
# for each in friends:
#     print('Happy New Year:', each)
# print('Done!')


# count = 0
# array = [3, 41, 12, 9, 74, 15]
# for var in array:
#     count = var + 1
#     print('Count: ', count)

# total = 0
# array = [3, 41, 12, 9, 74, 15]
# for itervar in array:
#     total = total + itervar
#     print('Total: ', total)




# array = [65, 41, 12, 9, 74, 15]

# def min(array):
#     smallest = None
#     for itervar in array:
#         if smallest is None or itervar < smallest :
#             smallest = itervar
#     return smallest

# print(min(array))

# count = 0
# n1 , n2 = 0,1
# nterms = 6
# while count<nterms:
#     print(n1)
#     nth = n1+n2
#     n1 = n2
#     n2 = nth
#     count += 1

x = 12//3
print(type(x))

