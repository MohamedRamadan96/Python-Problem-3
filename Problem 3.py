# Question : Accept string from the user and display only those characters
#  which are present at an even index ?
def printEveIndexChar(str):
    for i in range(0,len(str),2):
        print("index[", i, "]", str[i])

inputString = input('Enter Your String ?')
print("Orginal String is ",inputString)
print("Printing only even index chars")
print(printEveIndexChar(inputString))

