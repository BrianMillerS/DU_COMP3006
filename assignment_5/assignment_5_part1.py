#!/usr/bin/env python3

class employee():
    """Represents a single employee in the organization"""
    
    def __init__(self, name='', title='', salary = 0):
        self.name = name
        self.title = title
        self.salary = salary
        self.direct_reports_list = []
        
        
    def direct_reports(self, employee):
        """Adds that employee object to direct_reports_list"""
        self.direct_reports_list.append(employee)
    
    
    def calculate_budget(self):
        """Returns the employees 'budget', which is 
        that employees salary plus all of the salaries of the 
        employees below them in the organization."""
        budget = self.salary
        emps_below = self.direct_reports_list
        
        # get a list of all employees below
        for emp_1_below in self.direct_reports_list:
            emps_below = emps_below + emp_1_below.direct_reports_list
            for emp_2_below in emp_1_below.direct_reports_list:
                emps_below = emps_below + emp_2_below.direct_reports_list
        
        # add the budgets together
        for emp in emps_below:
            budget += emp.salary
        
        return budget
              
        
    def __str__(self):
        """
        Prints the employee title and name for:
        > all direct reports
        > all other employees below them in the organization
        Also prints the employee's budget
        """
        # initilize empty otheremp list and output
        otheremp_list = []
        output_str = ""
        output_str += "{} - {}\n".format(self.title, self.name)
        output_str += "\nDirect Reports:\n"
        
        # print all the direct reports
        for emp in self.direct_reports_list:
            output_str += "{} - {}\n".format(emp.title, emp.name)
            otheremp_list = otheremp_list + emp.direct_reports_list

        output_str += "\nOther Employees:\n"
        
        # add the other employees to the list
        for emp in otheremp_list:
            otheremp_list = otheremp_list + emp.direct_reports_list

        # print all the other employees
        for emp in otheremp_list:
            output_str += "{} - {}\n".format(emp.title, emp.name)
            
        # add budget to output
        output_str += "\nTotal Budget: ${}".format(self.calculate_budget())
            
        return output_str
            

# make all the employees, all 12 employees have $100 for convience
marketing_intern = employee(name='Wesley', title='Marketing Intern', salary=100)
digital_marketing_associate = employee(name='Counselor Deanna Troi', title='Digital Marketing Associate', salary=100)
hiring_manager = employee(name='Doctor Pulaski', title='Hiring Manager', salary=100)
ads_manager = employee(name='Data', title='Ads Manager', salary=100)
program_associate = employee(name='Chief Miles O Brien', title='Program Associate', salary=100)
development_associate1 = employee(name='Nurse Alyssa Ogawa', title='Development Associate1', salary=100)
development_associate2 = employee(name='Guinan', title='Development Associate2', salary=100)
hr_director = employee(name='Dr Crusher', title='HR Director', salary=100)
marketing_director = employee(name='Worf', title='Marketing Director', salary=100)
programs_director = employee(name='Geordi', title='Programs Director', salary=100)
development_director = employee(name='Riker', title='Development Director', salary=100)
ceo = employee(name='Jean Luc Picard', title='CEO', salary=100)

# make the organizational structure
digital_marketing_associate.direct_reports(marketing_intern)
marketing_director.direct_reports(digital_marketing_associate)
marketing_director.direct_reports(ads_manager)
hr_director.direct_reports(hiring_manager)
programs_director.direct_reports(program_associate)
development_director.direct_reports(development_associate1)
development_director.direct_reports(development_associate2)
ceo.direct_reports(development_director)
ceo.direct_reports(programs_director)
ceo.direct_reports(marketing_director)
ceo.direct_reports(hr_director)

# testing
print(ceo)
