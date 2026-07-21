from pydantic import BaseModel, Field
from typing import List


class LeadQualificationOutput(BaseModel):
    lead_score: int = Field(..., ge=0, le=100, description="Score from 0-100 indicating lead quality")
    priority: str = Field(..., description="HOT, WARM, or COLD")
    buying_intent: str = Field(..., description="Level of buying intent, e.g. High/Medium/Low")
    intent: str = Field(..., description="Short description of what the lead wants")
    company_size: str = Field(..., description="Estimated company size category")
    estimated_deal_size: str = Field(..., description="Estimated deal value range")
    pain_points: List[str] = Field(..., description="List of pain points identified")
    recommended_next_action: str = Field(..., description="Suggested next step for sales team")
    sales_summary: str = Field(..., description="1-2 line summary for sales rep")
    confidence_score: float = Field(..., ge=0, le=1, description="AI's confidence in this analysis, 0 to 1")