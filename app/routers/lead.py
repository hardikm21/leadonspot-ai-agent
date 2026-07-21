import json
import logging
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from app.models.request_models import LeadInput
from app.models.response_models import LeadQualificationOutput
from app.services.llm_service import get_lead_qualification

logger = logging.getLogger("lead_qualification")
router = APIRouter(prefix="/api/v1/lead", tags=["Lead Qualification"])


@router.post("/qualify", response_model=LeadQualificationOutput)
def qualify_lead(lead: LeadInput):
    try:
        result = get_lead_qualification(lead)
    except json.JSONDecodeError:
        logger.error("AI returned invalid JSON")
        raise HTTPException(status_code=502, detail="AI returned invalid JSON. Please retry.")
    except TimeoutError:
        logger.error("AI request timed out")
        raise HTTPException(status_code=504, detail="AI request timed out. Please retry.")
    except Exception as e:
        logger.error(f"Unexpected AI service error: {str(e)}")
        raise HTTPException(status_code=502, detail=f"AI processing failed: {str(e)}")

    try:
        return LeadQualificationOutput(**result)
    except ValidationError as e:
        logger.error(f"AI output failed schema validation: {str(e)}")
        raise HTTPException(status_code=502, detail="AI output did not match expected format.")