#function for word counting
def counter(str1):
    list1=str1.split()#splits all the words and creates a list
    count=len(list1)#counting the words
    print(f"The number of words in the given sentence or paragraph are: {count}")

print("Hello User!")
#try-except block for error handling
try:
    str1=input("Enter a sentence or paragraph of your choice:")
    if len(str1)==0: #checking possible error
        raise ValueError("Please enter some input") #if error exists print the statement
    counter(str1)
except ValueError as e:
    print(e)
    

