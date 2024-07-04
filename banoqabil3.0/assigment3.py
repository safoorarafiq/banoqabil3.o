#MARKSHEET
physics=int(input('enter the marks of physics: '))
biology=int(input('enter the marks of biology: '))
chemistry=int(input('enter the marks of chemistry: '))
english=int(input('enter the marks of english: '))
urdu=int(input('enter the marks of urdu: '))
total=physics+biology+chemistry+english+urdu
average=total/5
if average >=90 and average <100:
    print(average, 'grade is A+')
elif average >=80 and average <90:
    print(average, 'grade is A') 
elif average >=70 and average <80:
    print(average, 'grade is B')  
elif average >=60 and average <70:
    print(average, 'garde is c')
elif average >=50 and average <60:
    print(average, 'grade is D')  
else:
    print(average, 'grade is F')
    
#leap year

year=int(input('enter the year: '))
if year % 4==0 and 100!=0:
    print(year, 'year is leap year')    
else:
    print(year, 'year is not leap year')
    
#conversion of temperature

temp=float(input('enter the Temperature: '))
unit=input(" 'C' or 'F'  ")
C=5/9*(temp-32)
F=(temp*9/5)+32
if unit=='F':
    print('Temperature in Calsius is: ' ,C)
else:
    print('Temprature in Fahrenheit is: ' ,F)
      
#program to determine Triangle

side1=int(input('enter the side1 of triangle: '))
side2=int(input('enter the side2 of triangle: '))
side3=int(input('enter the side3 of triangle: '))
if side1==side2 and side2==side3:
    print('triangle is equilateral')
elif side1==side2  or side2!=side3:
    print('trinangle is isosceles') 
else:
    print('triangle is scalene')    



















    
    
    
    

         
