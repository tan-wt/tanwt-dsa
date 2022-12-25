## Class

class Employee:
    def __init__(self, first, last, pay):   
        self.first = first  
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        self.fn = self.first+self.last

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000) #emp_1 is instance 
emp_2 = Employee('Test', 'User', 60000) 
print(emp_1.fn)

#what we learned today:
#Class, Class attributes, instances 

    

        #print("self", self)



#if __name__ == "__main__":
    #print(Employee)
    #emp_1 = Employee(first="a", last="b", pay=100)
    #print(emp_1)

class NCT: 
    """
    attributes: looks, rap, sing, dance, humour, age 
    method: total score with validation 
    """
    def __init__(self, name, looks, rap, sing, dance, humour, age):
        self.name = name
        self.looks = looks 
        self.rap = rap 
        self.sing = sing
        self.dance = dance
        self.humour = humour 
        self.age = age
        
    def nct_scores(self): #add normalise argument
        total_score = self.looks + self.rap + self.sing + self.dance + self.humour
        return total_score 

haechan = NCT(name = 'Haechan', looks = 8, rap = 4, sing = 8, dance = 8, humour = 8, age = 22)
print(haechan.looks)
haechan_score = haechan.nct_scores()
print(haechan_score)



def test(): 
    l = []
    for i in range(1000):
        l = l + [i]
    print(l)    
    
def test2():
    l = []
    for i in range(1000):
        l.append(i) 

def test3():
    l = [i for i in range(1000)]

def test4(): 
    l = list(range(1000))

print(test())