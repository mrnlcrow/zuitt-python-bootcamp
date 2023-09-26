from abc import ABC, abstractmethod

# Abstract Person class
class Person(ABC):
    def __init__(self, first_name, last_name, email, department):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._department = department

    @abstractmethod
    def getFullName(self):
        pass

    @abstractmethod
    def addRequest(self, request):
        pass

    @abstractmethod
    def checkRequest(self, request):
        pass

    @abstractmethod
    def addUser(self, user):
        pass

# Employee class
class Employee(Person):
    def __init__(self, first_name, last_name, email, department):
        super().__init__(first_name, last_name, email, department)

    def login(self):
        return f"{self._email} has logged in"

    def logout(self):
        return f"{self._email} has logged out"

    def addRequest(self, request):
        return "Request has been added"

    def checkRequest(self, request):
        return ""

    def addUser(self, user):
        return ""

    def getFullName(self):
        return f"{self._first_name} {self._last_name}"

# TeamLead class
class TeamLead(Person):
    def __init__(self, first_name, last_name, email, department):
        super().__init__(first_name, last_name, email, department)
        self._members = []

    def login(self):
        return f"{self._email} has logged in"

    def logout(self):
        return f"{self._email} has logged out"

    def addMember(self, employee):
        self._members.append(employee)

    def get_members(self):
        return self._members

    def addRequest(self, request):
        return ""

    def checkRequest(self, request):
        return ""

    def addUser(self, user):
        return ""

    def getFullName(self):
        return f"{self._first_name} {self._last_name}"

# Admin class
class Admin(Person):
    def login(self):
        return f"{self._email} has logged in"

    def logout(self):
        return f"{self._email} has logged out"

    def addUser(self, user):
        return "New user added"

    def addRequest(self, request):
        return ""

    def checkRequest(self, request):
        return ""

    def getFullName(self):
        return f"{self._first_name} {self._last_name}"

# Request class
class Request:
    def __init__(self, name, requester, date_requested):
        self._name = name
        self._requester = requester
        self._date_requested = date_requested
        self._status = "open"

    def updateRequest(self):
        return f"Request {self._name} has been updated"

    def closeRequest(self):
        self._status = "closed"
        return f"Request {self._name} has been closed"

    def cancelRequest(self):
        self._status = "cancelled"
        return f"Request {self._name} has been cancelled"

    def set_status(self, status):
        self._status = status

# Test cases
employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing")
employee2 = Employee("Jane", "Smith", "sjane@mail.com", "Marketing")
employee3 = Employee("Robert", "Patterson", "probert@mail.com", "Sales")
employee4 = Employee("Brandon", "Smith", "sbrandon@mail.com", "Sales")
admin1 = Admin("Monika", "Justin", "jmonika@mail.com", "Marketing")
teamLead1 = TeamLead("Michael", "Specter", "smichael@mail.com", "Sales")
req1 = Request("New hire orientation", teamLead1, "27-Jul-2021")
req2 = Request("Laptop repair", employee1, "1-Jul-2021")

# Capstone Test Cases
assert employee1.getFullName() == "John Doe", "Full name should be John Doe"
assert admin1.getFullName() == "Monika Justin", "Full name should be Monika Justin"
assert teamLead1.getFullName() == "Michael Specter", "Full name should be Michael Specter"
assert employee2.login() == "sjane@mail.com has logged in"
assert employee2.addRequest(req2) == "Request has been added"
assert employee2.logout() == "sjane@mail.com has logged out"

teamLead1.addMember(employee3)
teamLead1.addMember(employee4)
for indiv_emp in teamLead1.get_members():
    print(indiv_emp.getFullName())

assert admin1.addUser(employee1) == "New user added"

req2.set_status("closed")
print(req2.closeRequest())