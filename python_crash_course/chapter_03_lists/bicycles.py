bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

#Accessing Elements in a List

print(bicycles[0])

#presentable by using the title() method:

print(bicycles[0].title())

#Index Positions Start at 0, Not 1

print(bicycles[1])

print(bicycles[3])

"""Python has a special syntax for accessing the last element

in a list. If you ask for the item at index -1, Python always

returns the last item in the list:"""

print(bicycles[-1])

#Using Individual Values from a List

message = f"My first bicycle was a {bicycles[0].title()}."

print(message) 
