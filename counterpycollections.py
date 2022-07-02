from collections import Counter

#COUNTER COLLECTION counts the number of occurences of  a characters
#counter collection also counts the occurences of the spaces

mycounter=Counter("JAVA IS A PROGRAMMING LANGUAGE")
print(mycounter)
#elements method returns a iterator for the number of times for the
#given element
#element method ignore the elements if the count of those is less than 1
#ELEMENTS()METHOD
myelemnt=Counter(hi=10)
myelementdict=Counter({"Ruby":3})
print(list(myelemnt.elements()))
print(list(myelementdict.elements()))
#MOSTCOMMON METHOD
print(mycounter.most_common())
#SUBTRACT METHOD
print("\nSUBTRACT METHOD")
mystring=Counter("hello")
print(mystring)
mystringa=Counter("hello world")
print(mystringa)
mystringa.subtract(mystring)
print(mystringa)
#


