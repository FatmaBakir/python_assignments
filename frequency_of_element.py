#Task : Find out the most frequent number and its frequency.

#Write a program that;

#Finds out the most frequent number in the given list.
#Calculates its frequency.
#Prints out the result such as :

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
most_freq_element = max(numbers, key = numbers.count)
frequency = numbers.count(most_freq_element)

print("the most frequent number is {} and it was {} times repeated".format(most_freq_element, frequency))
print(f"the most frequent number is {most_freq_element} and it was {frequency} times repeated")

the most frequent number is 3 and it was 4 times repeated
the most frequent number is 3 and it was 4 times repeated
