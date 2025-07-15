from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi = round(self.weight/(self.height**2), 2)
        print("BMI: ", bmi)
        return bmi

 
obj = {
    "name": "harshil", 
    "email": "harshil@hdfc.com", 
    "age": 62, 
    "weight": 50.8,
    "height": 1.8,
    "married": False,
    "allergies": ["abc", "cd"],
    "contact_details": 
    {
    "email": "harshil@gmail.com", 
    "emergency": "768464654"
    },
 }

patient = Patient(**obj)

def insert_patient_data(patient: Patient):
    print("name:",patient.name)
    print("Bmi: ", patient.calculate_bmi)

insert_patient_data(patient)

