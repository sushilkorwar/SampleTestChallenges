class Employee:
    '''Employee class of the company staff.
    
        :param first_name
            **MANDATORY** First name of the Employee
        :param last_name
            **MANDATORY** Last name of the Employee
        :param pay_rate
            **MANDATORY** Hourly Pay rate of Employee
        :param yearly_vacation
            **MANDATORY** Number of days of vacations in a year'''
    
    def __init__(self, first_name, last_name, pay_rate, yearly_vacation):
        self.fname = first_name
        self.lname = last_name
        self.pay_rate = pay_rate
        self.vacations = yearly_vacation
        
        if not isinstance(self.vacations, int):
            raise Exception("'yearly_vacation' should be an Integer number")
        
    def get_name(self):
        '''Method to get full name of the Employee.
        :return: Name in the format “Last Name, First Name"'''
        
        return "{}, {}".format(self.lname, self.fname)
    
    def get_pay_rate(self):
        '''Method to get hourly pay rate'''
        
        return self.pay_rate
    
    def get_yearly_vacation(self):
        '''Method to get the amount of yearly vacations'''
        
        return self.vacations
    
class Contractor(Employee):
    '''Contractor class of the company staff.
    
        :param first_name
            **MANDATORY** First name of the Contractor
        :param last_name
            **MANDATORY** Last name of the Contractor
        :param pay_rate
            **MANDATORY** Hourly Pay rate of Contractor
        :param yearly_vacation
            **MANDATORY** Number of days of vacations in a year
            By policy, it is always zero for Contractor.'''
    
    def __init__(self, first_name, last_name, pay_rate, agency_name):
        self.agency_name = agency_name
        super().__init__(first_name, last_name, pay_rate, 0)
        
    def get_name(self):
        '''Method to get full name of the Contractor.
        :return: Name in the format “Last Name, First Name"'''
        
        return "{}, {} [C]".format(self.lname, self.fname)
    
    def get_agency(self):
        '''Method to get Agency name.'''
        
        return self.agency_name
        
class Temporary(Contractor):
    '''Temporary class of the company staff.
    
        :param first_name
            **MANDATORY** First name of the Temporary
        :param last_name
            **MANDATORY** Last name of the Temporary
        :param pay_rate
            **MANDATORY** Hourly Pay rate of Temporary
        :param yearly_vacation
            **MANDATORY** Number of days of vacations in a year
            By policy, it is always zero for Temporary.'''
        
    def get_name(self):
        '''Method to get full name of the Temporary.
        :return: Name in the format “Last Name, First Name"'''
        
        return "{}, {} [T]".format(self.lname, self.fname)
