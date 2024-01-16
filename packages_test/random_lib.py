import random

print(round(random.random(),2))    # between 0.0 to 1.0 -> 0.7933439277398385
#how to round off

print(random.randint(1,10))     #between 1 and 10    -> 8
#no comments

my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))         #from a list , picks a number -> 1

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)              #shuffles the list -> [2,1,4,3,5]
print(my_list)

my_list = [1, 2, 3, 4, 5]
sample_result = random.sample(my_list, 3)  # gives a list of k length of non-repetitive -> [5,1,2]
print(sample_result)


print(random.uniform(1.0, 5.0))       # random float value between a and b -> 3.5801674947526933