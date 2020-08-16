class User:
    name = 'Robert Hooten'
    email = 'robertr.hooten@gmail.com'
    password = '12345'
    account_number = 12345545

class Employee(User):
    base_pay = 25.00
    department = 'Development'

class Customer(User):
    mailing_address = '123 main street'
    mailing_list = True

