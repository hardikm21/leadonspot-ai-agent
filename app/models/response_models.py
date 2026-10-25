from typing import List, Literal

from pydantic import BaseModel, Field, field_validator


class LeadQualificationOutput(BaseModel):
    lead_score: int = Field(..., ge=0, le=100, description="Score from 0-100 indicating lead quality")
    priority: Literal["HOT", "WARM", "COLD"] = Field(..., description="Lead priority")
    buying_intent: Literal["High", "Medium", "Low"] = Field(..., description="Level of buying intent")
    intent: str = Field(..., description="Short description of what the lead wants")
    company_size: str = Field(..., description="Estimated company size category")
    estimated_deal_size: str = Field(..., description="Estimated deal value range")
    pain_points: List[str] = Field(..., description="List of pain points identified")
    recommended_next_action: str = Field(..., description="Suggested next step for sales team")
    sales_summary: str = Field(..., description="1-2 line summary for sales rep")
    confidence_score: float = Field(..., ge=0, le=1, description="AI's confidence in this analysis, 0 to 1")

    @field_validator("priority", mode="before")
    @classmethod
    def normalize_priority(cls, v):
        return v.strip().upper() if isinstance(v, str) else v

    @field_validator("buying_intent", mode="before")
    @classmethod
    def normalize_buying_intent(cls, v):
        return v.strip().capitalize() if isinstance(v, str) else v
