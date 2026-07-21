from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class LeadInput(BaseModel):
    name: str = Field(..., min_length=1, description="Full name of the lead")
    email: EmailStr = Field(..., description="Email address of the lead")
    phone: Optional[str] = Field(None, description="Phone number of the lead")
    company: str = Field(..., min_length=1, description="Company name")
    designation: Optional[str] = Field(None, description="Job title/designation")
    industry: Optional[str] = Field(None, description="Industry the company belongs to")
    employees: Optional[str] = Field(None, description="Company size, e.g. '50-200'")
    country: Optional[str] = Field(None, description="Country of the lead")
    source: Optional[str] = Field(None, description="Where the lead came from, e.g. Website")
    message: str = Field(..., min_length=1, description="Message/inquiry written by the lead")

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Rahul Sharma",
                "email": "rahul@techcorp.com",
                "phone": "9876543210",
                "company": "TechCorp Solutions",
                "designation": "VP of Sales",
                "industry": "SaaS",
                "employees": "200-500",
                "country": "India",
                "source": "Website Contact Form",
                "message": "We're looking for an AI solution to qualify leads faster. Need something ASAP."
            }
        }