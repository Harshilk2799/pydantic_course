from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address = {"city": "Ahmedabad", "state": "Gujarat", "pincode": "382424"}

address_obj = Address(**address)

patient = {"name": "Harshil", "gender": "Male", "age": 25, "address": address_obj}

patient_obj = Patient(**patient)

print("Patien: ", patient_obj)




# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed