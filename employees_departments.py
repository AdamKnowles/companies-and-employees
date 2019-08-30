# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.
# Create a Company type that employees can work for. A company should have a business name, address, and industry type.
# Create two companies, and 5 people who want to work for them.
# Assign 2 people to be employees of the first company.
# Assign 3 people to be employees of the second company.
# Output a report to the terminal the displays a business name, and its employees.
# For example:

# Acme Explosives is in the chemical industry and has the following employees
#    * Michael Chang
#    * Martina Navritilova

# Jetways is in the transportation industry and has the following employees
#    * Serena Williams
#    * Roger Federer
#    * Pete Sampras


class Employee:

    def __init__(self, employee_name, title, date ):
        self.name = employee_name
        self.job_title = title
        self.employment_start_date = date

class Company:

    def __init__(self, company_name, address, type):
        self.name = company_name
        self.address = address
        self.industry_type = type
        self.employees = list()


floatrx = Company("FloatRx", "123 nope ln,", "Healthcare")
shands = Company("Shands", "456 okay street", "Healthcare")


danny = Employee("Danny", "jr developer", "11/13/45")
curt = Employee("Curt", "registered nurse", "12/23/46")
dustin = Employee("Dustin", "Physician", "2/4/46" )
sam = Employee("Sam", "Respiratory Therapist", "4/23/56" )
sydney = Employee("Sydney", "Nurse Practioner", "4/12/89")
drew = Employee("Drew", "JANITOR", "4/12/89")

floatrx.employees.append(danny)
floatrx.employees.append(curt)
floatrx.employees.append(dustin)
shands.employees.append(sam)
shands.employees.append(sydney)
shands.employees.append(drew)


print(f'{floatrx.name} is a {floatrx.industry_type} Company and here are its employees:') 


for employee in floatrx.employees:
    print(f'{employee.name} is a {employee.job_title} ')


print(f'{shands.name} is a {shands.industry_type} and its employees are:')

for employee in shands.employees:
    print(f'{employee.name} is a {employee.job_title}')



        
       