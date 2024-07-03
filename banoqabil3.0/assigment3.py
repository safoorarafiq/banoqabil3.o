#MARKSHEET
#marks obtained in 5 subjects
physics=int(input('86'))
biology=int(input('88'))
chemistry=int(input('87'))
english=int(input('90'))
urdu=int(input('92'))
total=physics*biology*chemistry*english*urdu
average=total/5
if average >=90:
    print('grade is A+')
elif average >=80:
    print('grade is A') 
elif average >=70:
    print('grade is B')  
elif average >=60:
    print('garde is c')
elif average >=50:
    print('grade is D')  
else:
    print('grade is F')
    
#leap year

year=int(input('2017'))
if year % 4==0 and 400==0:
    print(year, 'year is leap year')    
elif year %100!=0:
    print(year, 'year is not leap yare')
    
#conversion of temprature

temp=float(input('enter the temprature: '))  
unit=  

         
