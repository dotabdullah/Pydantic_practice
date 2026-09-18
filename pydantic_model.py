# Create a Pydantic model where we create schema for data.
# Field is a way to add extra custom validation and metadata to the model fields.
# Annotated is a way to add metadata to the model fields with the combination of Field.

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Schema
class Patient(BaseModel):
    
    name: Annotated[str, Field(min_length=2, max_length=50, title="Patient Name", description="Add the name of the patient that should be less than 50 characters", examples=["Abdullah", "Bilal"])]
    email: EmailStr
    linkedin_url : AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0)
    married: bool = False
    allergies: Optional[List[str]] = Field(max_length = 5)
    contact_details: Dict[str, str]