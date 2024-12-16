class Student:
    '''
    후.....
    하기 싫다..
    '''
    scholarship_score = 80


    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


    def get_grade(self):
        print(f'called >>>> get_grade')
        return f'return >>>> {self.grade}'
    
    def scholarship_up(self):
        Student.scholarship_score +=5 

a=Student('aiden',13,6)
a.scholarship_up()
print(a.scholarship_score)
