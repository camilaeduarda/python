from employee import Employee

empregado1 = Employee("John Doe", 50000)
empregado2 = Employee("Jane Smith", 65000)

print("Antes do aumento")
print("-"*20)
print(empregado1.get_info())
print(empregado2.get_info())
print("-"*20)


empregado1.raise_salary(10)
empregado2.raise_salary(10)

print("Depois do aumento")
print("-"*20)
print(empregado1.get_info())
print(empregado2.get_info())
print("-"*20)