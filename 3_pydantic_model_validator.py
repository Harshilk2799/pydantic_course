from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int 
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and "emergency" not in self.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return self
        
 
obj = {
    "name": "harshil", 
    "email": "harshil@hdfc.com", 
    "age": 62, 
    "weight": 50.8,
    "married": False,
    "allergies": ["abc", "cd"],
    "contact_details": 
    {
    "email": "harshil@gmail.com", 
    "emergency": "768464654"
    },
 }

patient = Patient(**obj)
print(patient)


def insert_patient_data(patient: Patient):
    print("name:",patient.name)

insert_patient_data(patient)