from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int = Field(..., description="Unique employee ID", example=1, ge=1)
    name: str = Field(..., description="Full name of the employee", example="Alice Johnson", min_length=2)
    department: str = Field(..., description="Department where the employee works", example="HR")
    age: int = Field(..., description="Age of the employee", example=30, ge=18, le=65)
