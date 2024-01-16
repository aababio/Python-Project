# %%
#import the libraries we need
from faker import Faker
import pandas as pd
#create an instance of Faker
fake =Faker(locale='en_US')

#Lets create a function
def create_patients(num_patients):

#Lets create an empty list to add our patient dictionaries
    patient_list = []

#Let's create an employee dictionary
    for i in range(1,num_patients):
        patient = {}
        patient['first_name'] = fake.first_name()
        patient['last_name'] = fake.last_name()
        patient['gender'] = fake.gender()
        patient['age'] = fake.age()
        patient['blood_type'] = fake.blood_type()
        patient['id_number'] = fake.id_number()
        patient['phone_number'] = fake.phone_number()
        patient['email'] = fake.email()
        patient['address'] = fake.address()
        patient['emergency_contact'] = fake.emergency_contact()
        patient['insurance_info'] = fake.insurance_info()
        patient['health_info'] = fake.health_info()
        patient_list.append(patient)
    return pd.DataFrame(patient_list)



# %%
