from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

VALID_LEAD = {
    "name": "Rahul Sharma",
    "email": "rahul@techcorp.com",
    "phone": "9876543210",
    "company": "TechCorp Solutions",
    "designation": "VP of Sales",
    "industry": "SaaS",
    "employees": "200-500",
    "country": "India",
    "source": "Website Contact Form",
    "message": "We need an AI solution ASAP."
}

MOCK_AI_RESPONSE = {
    "lead_score": 85,
    "priority": "HOT",
    "buying_intent": "High",
    "intent": "AI Solution",
    "company_size": "Medium",
    "estimated_deal_size": "Moderate to High",
    "pain_points": ["Lead Qualification"],
    "recommended_next_action": "Schedule Demo",
    "sales_summary": "Strong buying intent.",
    "confidence_score": 0.9
}


def test_invalid_email_returns_422():
    bad_lead = VALID_LEAD.copy()
    bad_lead["email"] = "notanemail"
    response = client.post("/api/v1/lead/qualify", json=bad_lead)
    assert response.status_code == 422


def test_missing_required_field_returns_422():
    bad_lead = VALID_LEAD.copy()
    del bad_lead["company"]
    response = client.post("/api/v1/lead/qualify", json=bad_lead)
    assert response.status_code == 422


@patch("app.routers.lead.get_lead_qualification")
def test_valid_lead_returns_200(mock_ai):
    mock_ai.return_value = MOCK_AI_RESPONSE
    response = client.post("/api/v1/lead/qualify", json=VALID_LEAD)
    assert response.status_code == 200
    data = response.json()
    assert data["priority"] == "HOT"
    assert 0 <= data["lead_score"] <= 100


@patch("app.routers.lead.get_lead_qualification")
def test_ai_failure_returns_502(mock_ai):
    mock_ai.side_effect = Exception("AI down")
    response = client.post("/api/v1/lead/qualify", json=VALID_LEAD)
    assert response.status_code == 502