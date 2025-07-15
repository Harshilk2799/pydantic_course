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

# python_dict = patient_obj.model_dump()
# python_dict = patient_obj.model_dump(include=["name", "gender"])
# python_dict = patient_obj.model_dump(exclude=["name", "gender"])
python_dict = patient_obj.model_dump(exclude={"address":["city"]})
print("Data: ", python_dict)
print("Type: ", type(python_dict))

python_json = patient_obj.model_dump_json()
print("Data: ", python_json)
print("Type: ", type(python_json))

