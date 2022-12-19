## Class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


#what we learned today:
#Class, Class attributes, instances 

    

        #print("self", self)


#if __name__ == "__main__":
    #print(Employee)
    #emp_1 = Employee(first="a", last="b", pay=100)
    #print(emp_1)