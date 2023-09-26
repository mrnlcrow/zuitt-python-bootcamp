from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def getFullName(self):
        pass

    @abstractmethod
    def addRequest():
        pass

    @abstractmethod
    def checkRequest():
        pass

    @abstractmethod
    def addUser(self):
        pass

class Employee(Person):
    def __init__(self, firstName, lastName, email, department):
        super().__init__()
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._department = department

    def getFirstName(self):
        return self._firstName

    def setFirstName(self, firstName):
        self._firstName = firstName

    def getLastName(self):
        return self._lastName

    def setLastName(self, lastName):
        self._lastName = lastName

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getDepartment(self):
        return self._department

    def setDepartment(self, department):
        self._department = department

    def getFullName(self):
        return f"{self._firstName} {self._lastName}"

    def addRequest(self):
        return "Request has been added"

    def checkRequest():
        pass

    def addUser():
        pass

    def login(self):
        return(f'{self._email} has logged in')

    def logout(self):
        return(f'{self._email} has logged out')

class TeamLead(Person):
    def __init__(self, firstName, lastName, email, department):
        super().__init__()
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._department = department
        self._members=[]
    def getFirstName(self):
        return self._firstName

    def setFirstName(self, firstName):
        self._firstName = firstName

    def getLastName(self):
        return self._lastName

    def setLastName(self, lastName):
        self._lastName = lastName

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getDepartment(self):
        return self._department

    def setDepartment(self, department):
        self._department = department

    def setMembers(self,memberName):
        self._members.append(memberName)

    def get_members(self):
        return self._members

    def getFullName(self):
        return f"{self._firstName} {self._lastName}"

    def checkRequest():
        return "Request has been checked"

    def addRequest():
        pass

    def addUser():
        pass

    def login(self):
        return(f'{self._email} has logged in')

    def logout(self):
        return(f'{self._email} has logged out')

    def addMember(self,employee):
        self._members.append(employee)

class Admin(Person):
    def __init__(self, firstName, lastName, email, department):
        super().__init__()
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._department = department
    def getFirstName(self):
        return self._firstName

    def setFirstName(self, firstName):
        self._firstName = firstName

    def getLastName(self):
        return self._lastName

    def setLastName(self, lastName):
        self._lastName = lastName

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getDepartment(self):
        return self._department

    def setDepartment(self, department):
        self._department = department

    def getFullName(self):
        return f"{self._firstName} {self._lastName}"

    def checkRequest():
        pass

    def addRequest():
        pass

    def addUser(self):
        return "User has been added"

    def login(self):
        return(f'{self._email} has logged in')

    def logout(self):
        return(f'{self._email} has logged out')

class Request():
    def __init__(self, name, requester, dateRequested):
        self.name = name
        self.requester = requester
        self.dateRequested = dateRequested
        self.status='online'
    
    def updateRequest(self):
        return f"Request {self.name} has been updated"
    
    def closeRequest(self):
        return f"Request {self.name} has been closed"
    
    def cancelRequest(self):
        return f"Request {self.name} has been cancelled"
    def set_status(self,status):
        self.status=status
#Test cases:

employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")
employee2 = Employee("Jane", "Smith", "sjane@mail.com", "Marketing")
employee3 = Employee("Robert", "Patterson", "probert@mail.com", "Sales")
employee4 = Employee("Brandon", "Smith", "sbrandon@mail.com", "Sales")
admin1 = Admin("Monika", "Justin", "jmonika@mail.com", "Marketing")
teamLead1 = TeamLead("Michael", "Specter", "smichael@mail.com", "Sales")
req1 = Request("New hire orientation", teamLead1, "27-Jul-2021")
req2 = Request("Laptop repair", employee1, "1-Jul-2021")

#Capstone Test Cases:
#here, assert is used to debug
assert employee1.getFullName() == "John Doe", "Full name should be John Doe"
assert admin1.getFullName() == "Monika Justin", "Full name should be Monika Justin"
assert teamLead1.getFullName() == "Michael Specter", "Full name should be Michael Specter"
assert employee2.login() == "sjane@mail.com has logged in"
assert employee2.addRequest() == "Request has been added"
assert employee2.logout() == "sjane@mail.com has logged out"

teamLead1.addMember(employee3)
teamLead1.addMember(employee4)
for indiv_emp in teamLead1.get_members():
    print(indiv_emp.getFullName())

assert admin1.addUser() == "User has been added"

req2.set_status("closed")
print(req2.closeRequest())