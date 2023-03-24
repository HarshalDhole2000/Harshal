#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python program to enter two numbers and find their sum.
num1=int(input("Enter 1st number:-"))
num2=int(input("Enter 2nd number:-"))
num3=num1+num2
print("Sum of",num1,"&",num2,"is:-",num3)


# In[ ]:


#2. Write a Python program to enter two numbers and perform all arithmetic operations.
num1=int(input("Enter 1st number:-"))
num2=int(input("Enter 2nd number:-"))
add=num1+num2
print("Addition is:-",add)
sub=num1-num2
print("Subtraction is:-",sub)
div=num1/num2
print("Division is:-",div)
mult=num1*num2
print("Multiplication is:-",mult)
mod=num1%num2
print("Remainder is:-",mod)
floor=num1//num2
print("Floor division is:-",floor)
#print("\nAddition is:-",add,"\nSubtraction is:-",sub,"\nDivision is:-",div,"\nMultiplication is:-",mult,"\nRemainder is:-",mod,"\nFloor division is:-",floor)


# In[ ]:


#3. Write a Python program to enter length and breadth of a rectangle and find its Area
length=int(input("Enter the length:-"))
breadth=int(input("Enter the breadth:-"))
area=length*breadth
print("Area of rectangle is:-",area)


# In[ ]:


#4. Write a Python program to enter base and height of a triangle and find its area.
base=int(input("Enter the base:-"))
height=int(input("Enter the height:-"))
area=1/2*base*height
print("Area of triangle is:-",area)


# In[ ]:


#5. Write a python Program to calculate Square of given number.
num=int(input("Enter the number:-"))
square=num**2
print("Square of",num,"is:-",square)


# In[ ]:


#6. Write a python Program to calculate cube of given number.
num=int(input("Enter the number:-"))
cube=num**3
print("Cube of",num,"is:-",cube)


# In[ ]:


#7. Write a Python program to enter marks of five subjects and calculate total, average and percentage.
marks=int(input("Enter the out of marks:-"))
sub=int(input("Enter the number of subjects:-"))
out_of=marks*sub
sub1=int(input("Enter the marks of subject1:-"))
sub2=int(input("Enter the marks of subject2:-"))
sub3=int(input("Enter the marks of subject3:-"))
sub4=int(input("Enter the marks of subject4:-"))
sub5=int(input("Enter the marks of subject5:-"))
total=sub1+sub2+sub3+sub4+sub5
average=total/sub
percentage=total/out_of*100
print("Total of marks of all subjects:-",total)
print("Average of marks of all subjects",average)
print("Percentage is:-",percentage)


# In[ ]:


#8. Write a Python program to enter P, T, R and calculate Simple Interest.
principal=int(input("Enter the principal amount:-"))
rate=int(input("Enter the interest rate:-"))
time=int(input("Enter the time/period:-"))
si=principal*rate*time/100
print("Simple interest is:-",si)


# In[ ]:


#9. Write a Python program to enter length and breadth of a rectangle and find its perimeter
length=int(input("Enter the length:-"))
breadth=int(input("Enter the breadth:-"))
perimeter=2*length*breadth
print("Area of rectangle is:-",perimeter)


# In[ ]:


#10. Swap values of two integer variables
num1=int(input("Enter 1st number:-"))
num2=int(input("Enter 2nd number:-"))
print("before swapping num1 is:-",num1,"&","num2 is:-",num2)
num1,num2=num2,num1
print("after swapping num1 is:-",num1,"&","num2 is:-",num2)


# In[ ]:


#11. Write a program to find a raise to b accept a and b from user
a=int(input("Enter 1st number:-"))
b=int(input("Enter 2nd number:-"))
power=a**b
print("Power of a raise to b is:-",power)


# In[ ]:


#12. Write a program to accept 2 number and find greatest
num1=int(input("Enter 1st number:-"))
num2=int(input("Enter 2nd number:-"))
if num1>num2:
    print("num1 is greatest")
elif num1==num2:
    print("both are same")
else:
    print("num2 is greatest")


# In[ ]:


#13. Write a program to accept number and check whether positive or negative
number=int(input("Enter number:-"))
if number>0:
    print("number is positive")
elif number==0:
    print("number is zero")
else:
    print("number is negative")


# In[ ]:


#14. WAP to check whether given number is three digit if yes check whether armstrong or not.
num=int(input("Enter the number:-"))
num1=str(num)
temp=num
length=len(num1)
sum=0
while temp>0:
    rem=temp%10
    sum=sum+rem**length
    temp=temp//10
print(sum)

if num==sum:
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")


# In[ ]:


#15. WAP to accept four digit number and do sum of digits
num=int(input("Enter four digit number:-"))
num1=str(num)
temp=num
length=len(num1)
sum=0
if length>=4:
    while temp>0:
        rem=temp%10
        sum=sum+rem
        temp=temp//10
    print(sum)
else:
    print("Please enter four digit number only!!!")


# In[ ]:


#16. Write a python program to check whether a number is even or odd
num=int(input("Enter teh number:-"))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")


# In[ ]:


#17. Write a program to check whether a year is leap year or not
year=int(input("Enter the year:-"))
if year%400==0 and year%100==0 or year%4==0:
    print(year,"is Leap year")
else:
    print(year,"is not Leap year")


# In[ ]:


#18. Write a program to check whether a number is divisible by 5 and 11 or not
num=int(input("Enter the number:-"))
if num%5==0 and num%11==0:
    print(num,"is divisible by 5 & 11")
else:
    print(num,"is not divisible by 5 & 11")


# In[2]:


#19. WAP to check whether given number is special 2 digit number or not
#A special two-digit number is a number such that when the sum of the digits of the number is added to the product of its digits,
#the result is equal to the original two-digit number.
num=int(input("Enter the number:-"))
sum=0
prod=1
temp=num
while temp>0:
    rem=temp%10
    sum=sum+rem
    prod=prod*rem
    temp=temp//10
total=sum+prod

if num==total:
    print(num,"is special number")
else:
    print(num,"is not special number")


# In[3]:


#20. Write a program to input name and basic salary of an employee. Calculate and
#display the gross salary and net salary when : da = 30% of basic, hra = 12.5% of basic, pf = 10% of basic,
#gross= basic+ da+ hra,
#net pay = gross - pf

name=input("Enter employee name:-")
basic=int(input("Enter employee's basic salary:-"))
da=basic*(0.30)
hra=basic*(0.125)
pf=basic*(0.10)
gross=basic+da+hra
net_pay=gross-pf
print("The gross salary of",name,"is",basic)
print("The gross salary of",name,"is",gross)
print("The gross salary of",name,"is",net_pay)

