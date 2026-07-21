# LeadOnSpot - AI Lead Qualification Agent

A REST API built with FastAPI that accepts lead information and returns AI-generated lead qualification insights using an LLM (Groq - Llama 3.3 70B).

## Features

- POST endpoint to submit lead data and receive structured qualification insights
- AI-powered scoring: lead score, priority, buying intent, pain points, recommended next action
- Request validation using Pydantic (rejects malformed input automatically)
- Graceful error handling for AI failures, timeouts, and malformed AI responses
- Logging of requests and errors
- Unit tests with mocked AI responses
- Docker support

## Tech Stack

- **Backend:** FastAPI
- **LLM:** Groq API (Llama 3.3 70B Versatile)
- **Validation:** Pydantic

## Setup Instructions

**1. Clone the repository**

\`\`\`
git clone https://github.com/hardikm21/leadonspot-ai-agent.git
cd leadonspot-ai-agent
\`\`\`

**2. Create and activate virtual environment**

\`\`\`
python -m venv venv
venv\\Scripts\\activate
\`\`\`

**3. Install dependencies**

\`\`\`
pip install -r requirements.txt
\`\`\`

**4. Set up environment variables**

Create a `.env` file in the root folder:

\`\`\`
GROQ_API_KEY=your_groq_api_key_here
\`\`\`

Get a free API key from console.groq.com/keys

**5. Run the server**

\`\`\`
uvicorn app.main:app --reload
\`\`\`

**6. Access the API**

- Base URL: http://127.0.0.1:8000
- Interactive docs: http://127.0.0.1:8000/docs

## Run with Docker

\`\`\`
docker build -t leadonspot-ai-agent .
docker run -p 8000:8000 --env-file .env leadonspot-ai-agent
\`\`\`

## Run Tests

\`\`\`
pytest
\`\`\`

## API Endpoint

### POST /api/v1/lead/qualify

**Sample Request:**

\`\`\`json
{
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
\`\`\`

**Sample Response:**

\`\`\`json
{
  "lead_score": 85,
  "priority": "HOT",
  "buying_intent": "High",
  "intent": "AI Solution",
  "company_size": "Medium",
  "estimated_deal_size": "Moderate to High",
  "pain_points": ["Lead Qualification", "Time Efficiency"],
  "recommended_next_action": "Schedule Demo",
  "sales_summary": "TechCorp Solutions is seeking an AI solution for faster lead qualification, indicating a strong buying intent.",
  "confidence_score": 0.92
}
\`\`\`

## Error Handling

| Scenario | Status Code |
|---|---|
| Invalid input | 422 |
| AI returns invalid JSON | 502 |
| AI request times out | 504 |
| AI output fails schema validation | 502 |

## Project Structure

\`\`\`
app/
├── main.py
├── models/
│   ├── request_models.py
│   └── response_models.py
├── routers/
│   └── lead.py
├── services/
│   ├── llm_service.py
│   └── prompt_templates.py
tests/
Dockerfile
\`\`\`

## Author

Hardik Mittal