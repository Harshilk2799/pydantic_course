from pydantic import BaseModel, Field, AnyUrl, EmailStr
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    age: int 
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=False, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None)]
    contact_details: Dict[str, str]

    # Data Validation
    email: EmailStr
    website_url: AnyUrl

obj = {
    "name": "harshil", 
    "age": 25, 
    "weight": 50.8,
    "contact_details": 
    {
    "email": "harshil@gmail.com", 
    "phone": "768464654"
    },
    "email": "harshil@gmail.com", 
    "website_url": "https://www.youtube.com/"
 }

patient = Patient(**obj)
print(patient)


def insert_patient_data(patient: Patient):
    print("name:",patient.name)

insert_patient_data(patient)