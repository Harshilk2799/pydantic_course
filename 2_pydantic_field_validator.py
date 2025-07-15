from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_domain = ["hdfc.com", "icici.com"]

        domain_name = value.split("@")[-1]

        if domain_name not in valid_domain:
            raise ValueError("Not a valid domain!")
        return value 
 
    @field_validator("name")
    # default value of mode is after in field_validator decorator
    # Runs after type conversion
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator("age", mode="before")
    # if mode is before runs before type conversion
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")



obj = {
    "name": "harshil", 
    "email": "harshil@hdfc.com", 
    "age": 25, 
    "weight": 50.8,
    "married": False,
    "allergies": ["abc", "cd"],
    "contact_details": 
    {
    "email": "harshil@gmail.com", 
    "phone": "768464654"
    },
 }

patient = Patient(**obj)
print(patient)


def insert_patient_data(patient: Patient):
    print("name:",patient.name)

insert_patient_data(patient)