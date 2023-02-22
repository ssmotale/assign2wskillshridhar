#!/usr/bin/env python
# coding: utf-8

# In[8]:


"""
Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
range of 1 to 25.
ans: def is the keyword to create function 
"""
#ans:
a=list(range(1,26))

def oddno(a):
    n=[]
    for ele in a:
        if ele%2 !=0:
            n.append(ele)
            
        else:
            pass
    return n       


# In[9]:


a=list(range(1,26))
oddno(a)


# In[12]:


"""

Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to
demonstrate their use.

Ans:*args is uefull to include as many argumments that are required inside function.
    **kwargs is useful to include as many as key value arguments that are required inside function.  

"""
def test1(*shree):
    return shree
test1(1,2,3,4,4)


# In[14]:


def test2(**shree):
    return shree

test2(a=3,b=6,c=9)


# In[20]:


"""
Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,
18, 20].

ans:it is type of function which can iterate through list or string.
there are 2 methodes i.e iter() and next()
"""
list1=[2, 4, 6, 8, 10, 12, 14, 16,18, 20]
ele = iter(list1)

print(next(ele))
print(next(ele))
print(next(ele))
print(next(ele))
print(next(ele))


# In[21]:


"""
Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.

Ans:function which give output as iterator
    for example range function.generator functions are used to create sequance.
    
    if we used yield then there will be only single memory allocation.which makes program efficient
    
    range() is generator function
    
"""


# In[26]:


"""
Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers.

"""
def isprime():
        for ele in range(2,2000):
            if 2000 % ele == 0:
                isprime=False
                break
                
        if is_prime:
            
            yield ele


# In[27]:


a=isprime()
for i in range(20):
    print(next(a))
    


# In[ ]:




