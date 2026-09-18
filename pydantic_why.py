from pydantic_model import Patient

# Usually python allows dynamic typing not static typing like Java or C++.
# Python type hunting is a way to add type hints to your code not producing errors. 
# Pythont does not have Type Validation and Data Validation by default.

# def insert_patient_data(name: str, age: int):
    
#     if type(name) == str and type(age) == int:
#         if age < 0:
#             raise ValueError("Age cann't be negative, please add correct age.")
#         else:     
#             print(name)
#             print(age)
#             print("inserted into database")
#     else:
#         raise TypeError("Incorrect data type.")    


# insert_patient_data("Abdullah", 30)    

def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("inserted")


patient_info = {"name": "Abdullah", "email": "info@xpertswp.com", "linkedin_url": "https://www.linkedin.com/in/withabdullahshahzad/" ,  "age": 30, "weight": 80.0,  
                "allergies": ["pollen", "dust", "noise"], 
                "contact_details": {
                    "email": "a3tavengers@gmail.com",
                    "phone": "+1234567890",
                    "address": "123 Main St, City, Country"
}}

# create the object and unpack the dictionary
patient1 = Patient(**patient_info)

# call the function
insert_patient_data(patient1)

