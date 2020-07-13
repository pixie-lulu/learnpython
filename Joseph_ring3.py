class Creat_person:
    #__init__()函数的一个变量一定是self表示创建的实例，self不需要传参
    def __init__(self,num,name,gender,age):
        self.number = num
        self.name = name
        self.gender = gender
        self.age = age

persons = []
numbers = [1,2,3,4,5,6,7,8,9]
names = ["Bob","Cindy","Alex","Aira","Michael","James","Jack","David","Sasha"]
genders = ["male","female","male","female","male","male","male","male","female"]
age = [20,15,33,46,71,55,37,46,27]

for number_,name_,gender_,age_ in zip(numbers,names,genders,age):
    person = Creat_person(number_,name_,gender_,age_)
    persons.append(person)


def skilled_Joseph_ring(persons, step):

    input_ = persons
    output_killed = []
    
    for i in range(len(persons)-1):
        killed_index = (step-1) % len(input_)
        killed = input_[(step-1) % len(input_)]
        output_killed.append(killed)
        
        start_index = (killed_index + 1) % len(input_)
        end_index = (killed_index - 1) % len(input_)
        
        if killed_index == 0:
            input_ = input_[start_index:]
        elif killed_index == len(input_)-1:
            input_ = input_[:end_index+1] 
        else:
            input_ = input_[start_index:] + input_[:end_index+1]
    return output_killed

x = skilled_Joseph_ring(persons, 3)
for xx in x:
    print(xx.number,xx.name,xx.gender,xx.age)