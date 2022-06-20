from static.inheritance.person import Person

class Employee(Person):
    def __init__(self, first_name, last_name, age, job_title, salary):
        super().__init__(first_name, last_name, age)
        self.job_title = job_title
        self.salary = salary

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, value):
        self.__job_title = value

    def salary(self):
        return self.__salary

    def salary(self, value):
        if value <=0:
            raise ValueError('Salary must be more than 0')
        self.__salary = value
