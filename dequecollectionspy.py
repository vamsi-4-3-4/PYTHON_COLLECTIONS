from collections import deque
mydeque=deque()

print("TYPE OF THE COLLECTION:",type(mydeque))
print(mydeque)
#************
#|| append() ||
#-------------
#appends the given element at the right of the queue
def p():
    print(mydeque,"\n")
mydeque.append("java")
p()
mydeque.append("python")
p()
mydeque.append("golang")
p()
#******************
#|| appendleft() ||
#-----------------
#adds the given element at the right of the deque
mydeque.appendleft("c")
p()
mydeque.appendleft("c++")
p()
#********************
#||     clear()     ||
#--------------------
print("BEFORE THE CLEAR")
p()
print("AFTER CLEAR")
mydeque.clear()
p()

mydeque.append("c")
mydeque.append("c++")
mydeque.append("java")
mydeque.append("python")
mydeque.appendleft("golang")
mydeque.appendleft("nodejs")
mydeque.appendleft("scala")
p()

#**************
#|| copy()   ||
#--------------
mydequee=deque()
mydequee=mydeque.copy()
print(mydequee)


#***************
#|| count()   ||
#---------------
p()
print("COUNT NUMBER OF ELEMENTS EQUAL TO C(GIVEN):",mydeque.count("c"))
mydeque.append("c")
mydeque.appendleft("c")
mydeque.append("c")
p()
print("COUNT NUMBER OF ELEMENTS EQUAL TO C(GIVEN):",mydeque.count("c"))



#***************
#|| extend()  ||
#---------------
requiredlist=("mysql","mongodb","redis","dynamodb")
print("MYDEQUE BEFORE EXTENDING")
p()
mydeque.extend(requiredlist)
print("MYDEQUE AFTER EXTENDING")
p()

#******************
#|| extendleft() ||
#------------------
requiredlista=("jenkins","git","docker")
print("MYDEQUE BEFORE EXTENDING LEFT")
p()
mydeque.extendleft(requiredlista)
print("MYDEQUE AFTER EXTENDING LEFT")
p()

#*****************
#||   index()   ||
#----------------
print("INDEX OF nodejs:",mydeque.index("nodejs"))

#*************************
#|| insert(index,item)  ||
#-------------------------
print("MY DEQUE BEFORE INSERTING")
p()
mydeque.insert(0,"kubernetes")
mydeque.insert(0,"reactjs")
print("MY DEQUE AFTER INSERTING")
p()

#**************
#|| pop()    ||
#--------------
#removes the elements from the right
print("MY ARRAY LIST BEFORE POPING")
p()
print("POPPED ELEMENT:",mydeque.pop())
p()
print("POPPED ELEMENT:",mydeque.pop())
p()
print("POPPED ELEMENT:",mydeque.pop())
p()
print("POPPED ELEMENT:",mydeque.pop())
p()
print("POPPED ELEMENT:",mydeque.pop())
p()
print("POPPED ELEMENT:",mydeque.pop())
p()
print("POPPED ELEMENT:",mydeque.pop())
p()

#****************
#|| popleft()  ||
#----------------

print("MY ARRAY LIST BEFORE POPINGLEFT")
p()
print("POPPED ELEMENT:",mydeque.popleft())
p()
print("POPPED ELEMENT:",mydeque.popleft())
p()
print("POPPED ELEMENT:",mydeque.popleft())
p()
print("POPPED ELEMENT:",mydeque.popleft())
p()
print("POPPED ELEMENT:",mydeque.popleft())
p()


#***************
#|| remove()  ||
#---------------
#removes the specified element
#never return the removed element

print("MYDEQUE BEFORE REMOVING")
p()
print("REMOVED ELEMENT:",mydeque.remove("c"))
p()
print("REMOVED ELEMENT:",mydeque.remove("scala"))
p()

#***************
#|| reverse() ||
#---------------
print("MY DEQUE BEFORE REVERSING")
p()
print("MY DEQUE AFTER REVERSING")
mydeque.reverse()
p()

#***************
#|| rotoate() ||
#---------------
print("MY DEQUE BEFORE ROTATING")
p()
print("ROTATING THE DEQUE BY ONE ELEMENT")
mydeque.rotate(1)
p()

#****************
#|| maxlen()   ||
#----------------

#print(":",mydeque.maxlen)

