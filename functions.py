#!/usr/bin/env python
# coding: utf-8

# In[10]:


def say_hello():
    """function of saying Hello."""
    print("Assalamualaikum.")
say_hello()

a=say_hello    


# In[15]:


def sum_n_numbers():  
    """sum of n numbers in python"""
    n=int(input("Enter a number:"))
    s=0
    for i in range(n+1):
        s+=i
    print("sum=",s)
sum_n_numbers()
    
    


# In[16]:


print(sum_n_numbers.__doc__)


# In[17]:


def full_name(firstname,lastname):
    print(firstname, lastname)
full_name("Bill", "Gates")
    


# In[21]:


def calculate_age(birthyear, name):
    print(f"{name.title()} is {2021-birthyear}.")
    
calculate_age(name="Gabriel", birthyear=1990)


# In[30]:


def square_cube(number):
    print( s,'x',s,'=',number**2, "\n",s,'x',s,'x',s,'=',number**3)
s=int(input('Enter a number:\n>>>'))
square_cube(s)


# In[35]:


def enter_number():
    n=int(input('Enter number='))
    for i in range(2,11):
        if not n%i:
            print(f"{n} divides by {i} without a remainder.")
enter_number()


# In[37]:


def make_full_name(name, lastname):
    full_name=f"{name} {lastname}"
    return full_name
student1=make_full_name("Olim", "Hakimov")
print(student1)


# In[39]:


print(f" I am very happy to introduce a new student from Uzbekistan and his full name is {student1}")


# In[43]:


def make_full_name(name, lastname, middle_name=''):
    if middle_name:
        
        full_name=f"{name} {lastname} {middle_name}"
    else:
        full_name=f"{name} {lastname}"
    return full_name.title()
student1=make_full_name("mike", "tyson")
student2=make_full_name('mirco', 'cro', 'cop')
print("The best fighters in the world are", student1, 'and', student2)
        
    
  


# In[44]:


#prime number from min-max numbers
def find_prime_numbers(min,max):
    prime_numbers = []
    for n in range(min, max+1):
        prime=True
        if n==1:
            prime=False
        elif n==2:
            prime=True
        else:
            for x in range(2,n):
                if n%x==0:
                    prime=False
        if prime:
            prime_numbers.append(n)
    return prime_numbers
prime1=find_prime_numbers(1,50)
print(prime1)


# In[48]:


def assess(names):
    scores={}
    while names:
        name=names.pop()
        score=input(f" Enter {name.title()}' score:")
        scores[name]=int(score)
    return scores

students = ['ali', 'vali', 'hasan', 'husan']
scores = assess(students[:])    #   taking copy from list [:] we pass students (list) into assess (function)
print(scores)
print(students)

    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




