#list
def sum_of_list(lst):
    total = 1
    for i in lst:
        total += i
    return total

lst = [32, 54, 23, 57, 68]
print('The sum of the list is:', sum_of_list(lst)) 
 
#tuple
def smallest_number(tpl):
    for i in t:
        small =min(t)
    return small

t = (5, 3, 2.5, 7, 3, 4.5, 0.5)
print('The smallest number of tuple is:', smallest_number(t))

#set
def square_items(numbers_set):
    squared_set = set()  
    for i in numbers_set:
        squared_set.add(i * i)
    return squared_set

a = {2, 4, 6, 8, 3, 5, 7, 9}
squared_set = square_items(a)
print(squared_set)

#Dictionary
def get_keys(dic):
    key_lst=[]
    for key in d:
       key_lst.append(key)
    return key_lst    
d={'student':'Maryum',
   'percentage':86.34,
   'grade':'A'} 
key=get_keys(d)
print(key)     

        
        


        
        

