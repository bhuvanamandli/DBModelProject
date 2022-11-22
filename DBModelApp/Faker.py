from faker import Faker;

fakerObj=Faker()
fullname=fakerObj.name()
print(fullname)
fname=fakerObj.first_name()
lname=fakerObj.last_name()
print(fname)
print(lname)
date1=fakerObj.date()
print(date1)
num=fakerObj.random_number(5)   #5-digit-number is generated
print(num)
email1=fakerObj.email()
print(email1)
print(fakerObj.city())
print(fakerObj.random_int(min=0, max=9))
print(fakerObj.random_element(elements=('Manager', 'HR', 'Developer', 'Director', 'CEO')));
