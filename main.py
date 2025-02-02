class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = f"{first}.{last}@company.com"
    
  def full_name(self):
    return "Hello, Mr.{} {}".format(self.first, self.last)
  
emp_1 = Employee("Eran", "Hasareli", 50000)

print(emp_1.full_name())
print(Employee.full_name(emp_1))