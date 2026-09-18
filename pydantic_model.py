# Create a Pydantic model where we create schema for data.
from pydantic import BaseModel

class Patient(BaseModel):
    
    name: str
    age: int