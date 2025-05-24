from pydantic import BaseModel,EmailStr, AnyUrl,field_validator,Field,model_validator,computed_field
from typing import List, Optional, Annotated

class Patient(BaseModel):
    name:str= Field(max_length=50)
    email: str 
    linkdin_url: AnyUrl
    age:int =Field(gt=0,lt=120)
    weight: float =Field(gt=0,) 
    height:float=Field(gt=0,lt=500)
    married:Optional[bool]=False
    allergies: Optional[List[str]]=None
    contact_details: dict[str,str]=None
    

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls,value):
        if 0 < value <100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/self.height**2,2)
        return bmi


def insert_patient_data(patient: Patient):
        print(patient.name)
        print(patient.age)
        print(patient.married)
        print(patient.allergies)
        print('BMI',patient.bmi)
        print('inserted')

patient_info={'name':'Bhargav','email':'ac@icici.com','linkdin_url':'https://errors.pydantic.dev/2.11/v/url_parsing','age':61,'weight':75.3,'height':1.72,'allergies':['pollen','dust'],'contact_details':{'email':'abc@gmail.com','phone':'23243','emergency':'235236'}}
patient1=Patient(**patient_info)
insert_patient_data(patient1)
