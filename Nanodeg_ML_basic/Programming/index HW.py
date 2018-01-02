# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(p,q):
    n = 0
    for e in p:
        if e == q:
            n = n + 1
    if n == 0:
        return -1
    else:
        return p.index(q)





print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

#Here is the answer of this question.
#One thing I am not doing well is that I am still stubborn,
#and do not know how to use the latest knowledge properly.
#I will try to do better.

def find_element(p,q):
    if q in p:
        return p.index(q)
    else:
        return -1

#This is pretty simple.
